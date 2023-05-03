# 概要

- Python - FastAPIの練習リポジトリ

# 環境情報

|*Tool*|*Version*|
|---|---|
|python|3.9.16|
|FastAPI|0.95.1|
|pip|22.0.4|

# 環境構築

```
$ make build
```

```
$ make up
```

# APIドキュメント

- 自動でSwaggerUIにて出力されている

> http://localhost:8080/docs

# コード規約

`PEP 8`が指針。
https://pep8-ja.readthedocs.io/ja/latest/

name|case|example
|---|---|---
変数名|スネークケース|user_name
メソッド名|スネークケース|get_name
クラス名|キャメルケース|UserProfile
ファイル名|スネークケース|user_profile.py

# ディレクトリ構成

```
.
├── .docker
│   ├── Dockerfile
│   └── requirements.txt
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── endpoints
│   │       ├── __init__.py
│   │       └── some_endpoint.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └──  some_model.py
│   └── main.py
└── docker-compose.yml
```

- appディレクトリ: FastAPIアプリケーションのメインディレクトリで、以下のサブディレクトリを持ちます。
- apiディレクトリ: APIのエンドポイントを定義するサブディレクトリ。
- coreディレクトリ: 設定やセキュリティなどのコアな機能を定義するサブディレクトリ。
- dbディレクトリ: データベースセッションを管理するサブディレクトリ。
- main.py: FastAPIアプリケーションのエントリーポイントとなるファイル。
- .docker: DockerコンテナをビルドするためのDockerfile。
- .docker/requirements.txt: 必要なPythonパッケージのリストを定義するファイル。
- docker-compose.yml: Dockerコンテナを起動するためのdocker-composeファイル。