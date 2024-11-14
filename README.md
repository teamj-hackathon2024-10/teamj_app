### ディレクトリ構成
```
.
├── ChatApp              # Jチーム開発ディレクトリ
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── static   # 静的ファイル用ディレクトリ
│   |   ├── css　 # cssを格納
|   |   ├── img　 # 画像ファイルを格納
|   |   └── js    # javascriptを格納
│   ├── templates       # Template(HTML)用ディレクトリ
|   |   ├── common     #管理者、ユーザーの共通画面を格納
|   |   ├── registration　# 新規会員登録用ディレクトリ
|   |   ├── management　# 管理用ディレクトリ
|   |   └── user　　　　# ユーザー用ディレクトリ
|   | 
│   └── util
├── Docker
│   ├── Flask
│   │   └── Dockerfile # Flask(Python)用Dockerファイル
│   └── MySQL
│       ├── Dockerfile  # MySQL用Dockerファイル
│       ├── init.sql    # MySQL初期設定ファイル
│       └── my.cnf
├── docker-compose.yml   # Docker-composeファイル
└── requirements.txt     # 使用モジュール記述ファイル
```
