# tech-exercise-sample

## 環境設定

### 1. リポジトリをローカルにコピー

任意の手順です。あくまでも参考にするだけという場合には飛ばしてください。  

**メンバの誰か1人が行う**  
*※ GitHubのリポジトリをGitLabの既存のリポジトリにフォークする方法が分からなかったので、ちょっと面倒な方法になってます。*  

1. GitHubのページから「Code -> Download ZIP」を選択し、ソースコード一式をダウンロードする。  
2. zipファイルを展開する。  
3. チームの代表リポジトリ（GitLabにすでに用意されているもの）を、ローカルにクローンする。  
4. クローンしたフォルダに、zipファイルの中身を全てコピーする。  
5. ブランチを作成し、チェックアウトする（ブランチ名はなんでもいいです。feat/initial_setupとか？）  
6. 全てのファイルをステージングし、コミットする（コミット名はなんでもいいですが、初期設定であることがわかるようにすると良いです。）  
7. リモートへプッシュし、mainブランチへマージする（マージリクエスト）。  

**メンバー全員が行う**  

1. チームの代表リポジトリをローカルにクローンし、ソースコード一式がコピーされていることを確認する。

### 2. Python の仮想環境を作成

以降、ローカルリポジトリのトップフォルダ名が「tech-exercise-sample」だという前提で説明をします。[フォルダ構成はこちら](#フォルダ構成)  
ライブラリのインストールエラーを避ける・対応しやすくするために、仮想環境を作成するのがおすすめです。

```bash
cd tech-exercise-sample
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

**メンバの誰か1人が行う**  

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

あくまでも一例です。調べると色々とパターンが出てきます。

```bash
tech-exercise-sample
├── .venv
├── README.md
├── .gitignore               <- Gitの管理対象外とするファイルを定義する。ここに書かれたファイルはステージングされない。
├── project
│   ├── app                  <- アプリの具体的な実装がまとまっているフォルダ。
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config               <- アプリの設定がまとまっているフォルダ。
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py      <- アプリの設定ファイル。
│   │   ├── urls.py          <- URLパターンの登録ファイル。
│   │   └── wsgi.py
│   ├── static
│   │   └── css
│   │       └── styles.css   <- 自分でCSSを設定したい場合はここに追記する。ファイルを分けても良いが、その場合はbase.htmlを変更する必要がある。
│   ├── media                <- 画像を扱う場合には、ここに画像が保存される。Gitの管理対象外なので、ソースコード一式には存在していない。
│   ├── templates
│   │   ├── app
│   │   │   ├── footer.html
│   │   │   ├── index.html
│   │   │   └── navbar.html
│   │   └── base.html        <- bootstrapを用いたテンプレートファイル。ナビゲーション、フッタがいい感じに配置されてるはず。
│   ├── .env.local           <- ここに環境変数を記載する。Gitの管理対象外。
│   ├── .env.sample          <- どういう環境変数を定義すべきかを記載する。ここには絶対に値を書かない。
│   ├── db.sqlite3
│   └── manage.py
└── requirements.txt         <- 使用するPythonのライブラリ一覧。チームで開発環境を統一するために。
```
