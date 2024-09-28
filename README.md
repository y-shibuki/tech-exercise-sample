# tech-exercise-sample

## 環境設定

### 1. リポジトリをローカルにクローン

```bash
git clone [このリポジトリのリンク]
```

### 2. Python の仮想環境を作成

ライブラリのインストールエラーを避ける・対応しやすくするために、仮想環境を作成するのがおすすめです。

```bash
cd tech-exercise
python -m venv .venv
source ./.venv/bin/activate
```

### 3. 必要なライブラリのインストール

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 環境変数の設定

GitLabにアップロードしてはいけない情報の管理方法  

**メンバーの誰か1人が行う**  

1. projectフォルダ内の```.env.sample```ファイルをコピーし、```.env.local```に名前を変更する。  
2. 以下のコマンドを順に実行する  

```bash
cd project
python manage.py shell
```

3. Pythonのインタラクティブコンソールになる（>>> の記号があるやつ）ので、以下のコードを貼り付けて実行し、表示されたランダムな文字列を```.env.local```ファイルの```SECRET_KEY=```の後にシングルクオテーションごと貼り付ける。  

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
exit()
```

4. ```.env.local```ファイルの```Debug=```を```Debug=True```に書き換える（ここをTrue以外の文字列にするとDebugモードが解除される）  

5. ```.env.local```ファイルをメンバ全員にチャットで展開する  

**メンバー全員が行う**  

1. 展開された```.env.local```ファイルを、projectフォルダ直下（.env.sampleがある場所）にコピーする

### 6. 動作確認

```bash
cd project
python manage.py runserver
```

ブラウザで、localhost:8000にアクセスして、サンプル画面が出てきたらOK。  

### 7. 実装

頑張れ！

## 開発の手順例

**絶対に**mainブランチでは作業をしないこと！  

```bash
git branch john/add_homepage
```

のように、ブランチ名は「名前/タイトル」にするなど、チームでブランチ名のルールを作成しましょう。  
必ずブランチを作成し、チェックアウトしたことを確認した上で作業してください。  

## 変更点

主な変更点は以下の通りです。

- Djangoのフォルダ構成の変更 [詳細はこちら](#フォルダ構成)  
  - テンプレートフォルダの位置などが変わっています。
- GitLabにアップロードしてはいけない情報に関する制限の追加
  - 大事な情報は環境変数を使用するように変更  
  - .gitignoreの追加  

## フォルダ構成

```bash
.
├── README.md
├── docker
│   ├── Dockerfile
│   └── mysql
│       └── my.cnf
├── docker-compose.yml
├── project
│   ├── app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── settings_MySQLを使う場合.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── static
│   │   └── css
│   │       └── styles.css
│   └── templates
│       ├── app
│       │   ├── footer.html
│       │   ├── index.html
│       │   └── navbar.html
│       └── base.html
└── requirements.txt
```
