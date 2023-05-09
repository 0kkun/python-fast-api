include .env

MYSQL_ROOT_LOGIN_CMD = mysql -u root -p$(MYSQL_ROOT_PASSWORD)
MYSQL_USER_LOGIN_CMD = mysql -u $(MYSQL_USER_NAME) -p$(MYSQL_PASSWORD) $(MYSQL_DB_NAME)
DCE = docker-compose exec
DEI = docker exec -it

# *****************************
# *      For First Build      *
# *****************************
.PHONY: init
init:
	@make build
	@make up

# *****************************
# *      Python Command      *
# *****************************

.PHONY: migrate
migrate:
	$(DCE) app bash -c "cd db && alembic upgrade head"

.PHONY: migrate-rollback
migrate-rollback:
	@read -p "Enter the number of steps to rollback: " STEPS; \
	$(DCE) app bash -c "cd db && alembic downgrade $(STEPS)"

.PHONY: migrate-drop
migrate-drop:
	$(DCE) app bash -c "cd db && alembic downgrade base"

.PHONy: migrate-log
migrate-log:
	$(DCE) app bash -c "cd db && alembic history --verbose"

# *****************************
# *     Container Controll    *
# *****************************
.PHONY: build_c
build_c:
	docker-compose build --no-cache --force-rm

.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose stop

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: app
app:
	$(DCE) app bash

.PHONY: db
db:
	$(DCE) db bash

.PHONY: restart
restart:
	@make down
	@make up


# *****************************
# *           MySql           *
# *****************************
.PHONY: mysql
mysql:
	$(DCE) db bash -c '$(MYSQL_USER_LOGIN_CMD)'

.PHONY: mysql-root
mysql-root:
	$(DCE) db bash -c '$(MYSQL_ROOT_LOGIN_CMD)'

.PHONY: show-dbuser
show-dbuser:
	$(DEI) $(PROJECT_NAME)_db $(MYSQL_ROOT_LOGIN_CMD) --execute="SELECT user, host FROM mysql.user ORDER BY user, host"

.PHONY: show-dbgrants
show-dbgrants:
	$(DEI) $(PROJECT_NAME)_db $(MYSQL_USER_LOGIN_CMD) --execute="SHOW GRANTS"

.PHONY: show-databases
show-databases:
	$(DEI) $(PROJECT_NAME)_db $(MYSQL_USER_LOGIN_CMD) --execute="SHOW DATABASES"

.PHONY: grant-testdbuser
grant-testdbuser:
	$(DEI) $(PROJECT_NAME)_db $(MYSQL_ROOT_LOGIN_CMD) --execute="GRANT ALL ON $(MYSQL_DB_NAME)_testing.* TO $(MYSQL_USER_NAME)"

.PHONY: create-testdb
create-testdb:
	$(DEI) $(PROJECT_NAME)_db $(MYSQL_ROOT_LOGIN_CMD) --execute="CREATE DATABASE $(PROJECT_NAME)_db_testing"

.PHONY: test-init
test-init:
	@make create-testdb
	@make grant-testdbuser
	@make show-dbgrants
	@make show-databases


