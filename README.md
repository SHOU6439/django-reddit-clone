![メイン画像](static/img/reddit_logo.jpeg)
## 概要
海外最大級のインターネット掲示板　『reddit』　をcloneしました

## URL

conoha:[reddit-clone.top](http://reddit-clone.top)

heroku:[django-reddit-clone-2022.herokuapp.com](https://django-reddit-clone-2022.herokuapp.com/)


## なぜ作ったのか
djangoを学習する際にdjangoで作られてるサービスを調べ、そこでredditがdjangoで作られてると知り、djangoの学習に最適だと判断したため作成した。

その他のdjangoが用いられてるサービスは
* Youtube
* Dropbox
* Google
* インスタグラム
* Spotify(音楽ストリーミングサービス)
* YahooMap
* Pinterest(画像シェアサービス)
* ワシントンポスト
* NASA
* Prezi (クラウド上のパワーポイントのようなサービス)<br>

がありましたが、自分はwebアプリケーションといえば掲示板というイメージがあったので、redditを作ることにしました。



## 実装した機能

* ユーザー機能(サインアップやログイン)
* 投稿のCRUD
* 投稿に対しての投票機能
* communityの機能
  * 作成
  * 詳細閲覧
  * 一覧
* community参加、離脱機能
* 参加中のcommunityに紐づいた投稿のCRUD
* 通知機能
* 検索機能
  * ユーザー
  * 投稿
  * コミュニティ
* 画像のアップロード機能(herokuでは不可)
  * プロフィールアイコン
  * プロフィールヘッダー
  * 投稿に紐づいた写真
* コメント機能（投稿に対してコメントができる）
* 返信機能（コメントに対して返信ができる）
* シェア機能（投稿をtwitterにシェアすることができる）
* 投稿保存機能
* プロフィール閲覧機能
  * 自分の投稿の一覧
  * 保存中の投稿の一覧
  * 投票で賛成した投稿の一覧
  * 投票で反対した投稿の一覧
  * 参加中のコミュニティの一覧
* チャット機能
  * DMルーム作成機能
  * DMルームの一覧
  * DMルーム作成招待の一覧
  * DMルーム作成招待の承認、拒否機能
  * DM作成機能

## 特に力を入れた点

### 充実した機能

できるだけ多くの機能を実装し、さまざまな機能の実装方法を勉強した。

### 本家と似たUIとオリジナリティ

できるだけ本家のUIに似せつつも良い感じにオリジナリティを出せるようにしました。



## 使用技術・環境
### 【フロントエンド】

* HTML
* CSS
* JavaScript
* Font Awesome


### 【バックエンド】

* Python 3.9.9(conohaのサーバーでは3.9.9がまだ対応されてないパッケージが多かったので3.6にした)
* Django 3.2.8



### 【データベース】

* Mysql



### 【開発環境】

* venv
* Git



### 【本番環境】

* conoHa VPS
* heroku
* Nginx, gunicorn



## 今後行いたいこと

短期的な目標はDRF&フロントのフレームワーク(Next.jsなど)を用いて１から自分でアイディアを考えて、成果物を作ってみたいです。LaravelやRailsなどのwebフレームワークも積極的に触っていきたいです。<br>
長期的な目標はWebエンジニアとして働いていくことです。自分でサービス作るとかも良いと考えてたりします。



## About me

* [twitter](https://twitter.com/SHOU175501281/)  
