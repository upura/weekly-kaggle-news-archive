# Weekly Kaggle News #33
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-33-266095
<h3><h2>News</h2><p>20日に終了した「<a href="https://www.kaggle.com/c/alaska2-image-steganalysis?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">ALASKA2 Image Steganalysis</a>」コンペの最終順位が確定し、優勝した<a href="https://www.kaggle.com/wowfattie?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">Guanshuo Xu</a>さんがKaggleのCompetitionsランキング1位に躍り出ました。2019年以降は<a href="https://www.kaggle.com/bestfitting?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">bestfitting</a>さんが1位を維持しており、約1年半ぶりの首位交代となりました。</p><p>深層学習ライブラリ「TensorFlow」の<a href="https://github.com/tensorflow/tensorflow/releases/tag/v2.3.0" target="_blank">v2.3.0</a>が27日に公開されました。データ読み込みや前処理に関する機能などが<a href="https://blog.tensorflow.org/2020/07/whats-new-in-tensorflow-2-3.html" target="_blank">追加</a>されています。同じく深層学習ライブラリ「PyTorch」は<a href="https://github.com/pytorch/pytorch/releases/tag/v1.6.0" target="_blank">v.1.6.0</a>が28日に公開されました。精度を保ちつつメモリ消費量を軽減する混合精度学習の機構などが<a href="https://pytorch.org/blog/pytorch-1.6-released/" target="_blank">導入</a>されています。同日には、MicrosoftがWindows版のPyTorch開発に協力すると<a href="https://pytorch.org/blog/microsoft-becomes-maintainer-of-the-windows-version-of-pytorch/" target="_blank">発表</a>されました。</p><p>Preferred Networksは29日、ハイパーパラメータ調整ツールの「Optuna」の<a href="https://github.com/optuna/optuna/releases/tag/v2.0.0" target="_blank">v2.0.0</a>を公開しました。ハイパーパラメータの重要度を評価する機能が追加され、v0.18.0で実験的に追加されていた「<a href="https://tech.preferred.jp/ja/blog/hyperparameter-tuning-with-optuna-integration-lightgbm-tuner/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">LightGBMTuner</a>」も正式に<a href="https://medium.com/optuna/optuna-v2-3165e3f1fc2" target="_blank">導入</a>されています。同社は30日、PyTorch向け深層強化学習ライブラリ「<a href="https://github.com/pfnet/pfrl" target="_blank">PFRL</a>」を<a href="https://preferred.jp/ja/news/pr20200730/" target="_blank">公開</a>しました。既に公開している深層強化学習ライブラリ「ChainerRL」の後継に当たります。同社は自社開発の深層学習ライブラリ「Chainer」から<a href="https://preferred.jp/ja/news/pr20191205/" target="_blank">PyTorchへの移行</a>を進めています。</p><h2>Competitions</h2><p>Kaggle「<a href="https://www.kaggle.com/c/landmark-recognition-2020/" target="_blank">Google Landmark Recognition 2020</a>」コンペが29日に始まりました。画像認識のタスクで、過去2年の開催と異なり今年は実行コードを提出する形式となっています。</p><p>SIGNATE「<a href="https://signate.jp/competitions/274" target="_blank">ひろしまQuest2020#stayhome：プロ野球データを用いた配球予測</a>」コンペは28日に終了しました。<a href="https://signate.jp/competitions/275" target="_blank">球種予測部門</a>と<a href="https://signate.jp/competitions/276" target="_blank">コース予測部門</a>の結果は即日発表され、<a href="https://signate.jp/competitions/277" target="_blank">アイデア部門</a>の審査結果は8月下旬に公開予定です。9月上旬には成果発表会が予定されています。</p><p>学生対象の「<a href="https://signate.jp/student-cup" target="_blank">SIGNATE Student Cup 2020</a>」コンペの概要が公開されています。8月5〜26日の比較的短期間の開催で、求人情報から職種を判別するタスクです。</p><p>Microsoftは「<a href="https://msnews.github.io/competition.html" target="_blank">MIND News Recommendation Competition</a>」を20日に開始しました。同社が公開した大規模英語ニュースのデータセットを用いた推薦タスクです。<a href="https://github.com/microsoft/recommenders" target="_blank">GitHub</a>でサンプルコードなども公開されています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Modern Data Augmentation Techniques for Computer Vision" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/303/040/thumb/preview.png?1595840176" />
<strong style='display: block;'><a href="https://app.wandb.ai/authors/tfaugmentation/reports/Modern-Data-Augmentation-Techniques-for-Computer-Vision--VmlldzoxODA3NTQ?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Modern Data Augmentation Techniques for Computer Vision</a> &mdash; <a href="https://app.wandb.ai/authors/tfaugmentation/reports/Modern-Data-Augmentation-Techniques-for-Computer-Vision--VmlldzoxODA3NTQ">app.wandb.ai</a></strong>
A comparison between Cutout, mixup, CutMix, and AugMix augmentations and their impact on model robustness. 
</p>
<div style='clear: both;'></div>
<p><p>さまざまな画像のデータ水増し手法を紹介している記事。TensorFlow実装とともに、検証結果を掲載しています。</p></p>
<p>
<img width="140" height="140" alt="Train HuggingFace models twice as fast" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/318/466/thumb/preview.png?1596121663" />
<strong style='display: block;'><a href="https://app.wandb.ai/pommedeterresautee/speed_training/reports/Train-HuggingFace-models-twice-as-fast--VmlldzoxMDgzOTI?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Train HuggingFace models twice as fast</a> &mdash; <a href="https://app.wandb.ai/pommedeterresautee/speed_training/reports/Train-HuggingFace-models-twice-as-fast--VmlldzoxMDgzOTI">app.wandb.ai</a></strong>
... with dynamic padding and uniform length batching. This reports summarizes our 14 experiments + 5 reproducibility experiments regarding 2+1 optimizations to reduce training time.
</p>
<div style='clear: both;'></div>
<p><p>最先端の自然言語処理モデルを提供する「<a href="https://github.com/huggingface/transformers" target="_blank">transformers</a>」の学習時間を短縮する手法を検証している記事。文章をトークン化する際のバッチの作り方などを工夫しています。</p></p>
<p>
<strong style='display: block;'><a href="https://www.kaggle.com/marketneutral/julia-live-on-kaggle?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Julia Live on Kaggle</a></strong>
Explore and run machine learning code with Kaggle Notebooks | Using data from House Property Sales Time Series
</p>
<p><p>科学計算処理に秀でたプログラミング言語「Julia」をKaggle Notebook上で実行するチュートリアル。Juliaに関するイベント「<a href="https://juliacon.org/2020/" target="_blank">JuliaCon 2020</a>」は29〜31日にオンライン開催されています。</p></p>
<p>
<img width="140" height="140" alt="機械学習なdockerfileを書くときに気をつけとくと良いこと - nykergoto’s blog" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/297/308/thumb/1595675269?1595687132" />
<strong style='display: block;'><a href="https://nykergoto.hatenablog.jp/entry/2020/07/25/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AAdockerfile%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%A8%E3%81%8D%E3%81%AB%E6%B0%97%E3%82%92%E3%81%A4%E3%81%91%E3%81%A8%E3%81%8F%E3%81%A8%E8%89%AF%E3%81%84%E3%81%93?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">機械学習なdockerfileを書くときに気をつけとくと良いこと - nykergoto’s blog</a> &mdash; <a href="https://nykergoto.hatenablog.jp/entry/2020/07/25/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AAdockerfile%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%A8%E3%81%8D%E3%81%AB%E6%B0%97%E3%82%92%E3%81%A4%E3%81%91%E3%81%A8%E3%81%8F%E3%81%A8%E8%89%AF%E3%81%84%E3%81%93">nykergoto.hatenablog.jp</a></strong>
みなさん機械学習系の環境構築はどうやってますか? 僕は最近は Docker を使った管理を行っています。 特に師匠も居なかったので、ぐぐったり人のイメージを見たり手探りで docker をつかいつかいしている中で、最初からやっとけばよかったなーということがいくつかあるのでメモとして残しておきます。 大きく2つです。 キャッシュは消す テストを書く キャッシュは消す ライブラリをいろいろと install すると大抵の場合ダウンロードしたファイルを保存されている場合が多いです。何かのタイミングで再びそのライブラリをインストールする際にはダウンロードしたファイルを使って、素早くインストールすること…
</p>
<div style='clear: both;'></div>
<p><p>Pythonの環境構築にDockerを用いる場合のTipsを紹介している記事。キャッシュの意図的な削除とビルド時のテストを勧めています。</p></p>
<p>
<img width="140" height="140" alt="ディープラーニングは万能なのか l DataRobot" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/317/013/thumb/The-Best-and-Worst-of-Deep-Learning_blog_Image_JP_v.1.0-1.jpg?1596102197" />
<strong style='display: block;'><a href="https://www.datarobot.com/jp/blog/is-deep-learning-almighty/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ディープラーニングは万能なのか l DataRobot</a> &mdash; <a href="https://www.datarobot.com/jp/blog/is-deep-learning-almighty/">www.datarobot.com</a></strong>
AI（人工知能）技術が注目をあつめる昨今、ディープラーニング（深層学習）という単語を耳にする機会も増えてきました。一方で、従来の機械学習との違いや詳細な仕組みはわからないという方も多いのではないでしょうか。 そこで本稿ではディープラーニングとAI、マシンラーニングとの違い、kaggleコンペ優勝者が使ったモデルかつ産業応用事例に基づいて、どちらの領域でディープラーニングが優れているか、優れてないかを紹介します。
</p>
<div style='clear: both;'></div>
<p><p>Kaggle Grandmasterの<a href="https://www.kaggle.com/senkin13" target="_blank">senkin13</a>さんによる直近3年間のKaggleの優勝解法の分析記事。非構造化データを扱う場合の主要モデルはディープラーニングが圧倒的な一方で、テーブルデータの場合は勾配ブースティングが根強い人気です。</p></p>
<p>
<img width="140" height="140" alt="Deep Learning入門：マルチタスク学習" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/303/222/thumb/maxresdefault.jpg?1595842326" />
<strong style='display: block;'><a href="https://www.youtube.com/watch?feature=youtu.be&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter&amp;v=2R7CurdWmSY">Deep Learning入門：マルチタスク学習</a> &mdash; <a href="https://www.youtube.com/watch?v=2R7CurdWmSY&amp;feature=youtu.be">www.youtube.com</a></strong>
Deep Learningを用いてマルチタスク学習と呼ばれる、複数の機能を1つのモデルに学習する方法について解説します。 前回の動画：Attention（注意） https://www.youtube.com/watch?v=g5DSLeJozdw ニューラルネットワーク学習の仕組み https://www.yo...
</p>
<div style='clear: both;'></div>
<p><p>ディープラーニングを用いた「マルチタスク学習」の解説動画。複数の機能を1つのモデルに学習させる方法について、利点や課題を紹介しています。</p></p>
<p>
<img width="140" height="140" alt="たった数行でpandasを高速化する2つのライブラリ(pandarallel/swifter) - フリーランチ食べたい" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/299/559/thumb/20200726173057.png?1595770340" />
<strong style='display: block;'><a href="https://blog.ikedaosushi.com/entry/2020/07/26/173109?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">たった数行でpandasを高速化する2つのライブラリ(pandarallel/swifter) - フリーランチ食べたい</a> &mdash; <a href="https://blog.ikedaosushi.com/entry/2020/07/26/173109">blog.ikedaosushi.com</a></strong>
pandas はデータ解析やデータ加工に非常に便利なPythonライブラリですが、並列化されている処理とされていない処理があり、注意が必要です。例えば pd.Sereis.__add__ のようなAPI(つまり df['a'] + df['b'] のような処理です)は処理が numpy に移譲されているためPythonのGILの影響を受けずに並列化されますが、 padas.DataFrame.apply などのメソッドはPythonのみで実装されているので並列化されません。 処理によってはそこがボトルネックになるケースもあります。今回は「ほぼimportするだけ」で pandas の並列化され…
</p>
<div style='clear: both;'></div>
<p><p>Pandasの処理を並列化し高速化できる2つのライブラリの紹介記事。比較実験の結果も掲載しています。</p></p>
<p>
<img width="140" height="140" alt="Kaggle | 株式会社Rist | Rist Inc." style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/303/016/thumb/ogimage.jpg?1595839806" />
<strong style='display: block;'><a href="https://www.rist.co.jp/kaggle/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggle | 株式会社Rist | Rist Inc.</a> &mdash; <a href="https://www.rist.co.jp/kaggle/">www.rist.co.jp</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>Kagglerの採用に力を入れるRistのKaggleに関するページが27日に公開されました。所属社員の実績や、業務時間を利用したKaggle参加制度を紹介しています。</p></p>
<p>
<strong style='display: block;'><a href="https://qiita.com/tachyon777/items/e1e4eac8cbaa3e308ff4?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[Kaggle]PANDAコンペ参加記 - Qiita</a></strong>

</p>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/prostate-cancer-grade-assessment" target="_blank">Prostate cANcer graDe Assessment (PANDA) Challenge</a>」コンペで銅メダルを獲得した方の参加録。画像コンペ初参加での取り組みが事細かに綴られています。</p></p>
<p>
<img width="140" height="140" alt="PyTorchを用いたディープラーニング実装の学習方法 (Part 1) | by 小川 雄太郎（電通国際情報サービスISID） | PyTorch | Aug, 2020 | Medium" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/431/822/thumb/1*69TA76SX_eN4kKHncDVZYg.png?1598555429" />
<strong style='display: block;'><a href="https://medium.com/pytorch/pytorch%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E5%AE%9F%E8%A3%85%E3%81%AE%E5%AD%A6%E7%BF%92%E6%96%B9%E6%B3%95-part-1-e5f6ad77e0ff?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">PyTorchを用いたディープラーニング実装の学習方法 (Part 1) | by 小川 雄太郎（電通国際情報サービスISID） | PyTorch | Aug, 2020 | Medium</a> &mdash; <a href="https://medium.com/pytorch/pytorch%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E5%AE%9F%E8%A3%85%E3%81%AE%E5%AD%A6%E7%BF%92%E6%96%B9%E6%B3%95-part-1-e5f6ad77e0ff">medium.com</a></strong>
PyTorchを用いて画像処理から自然言語処理など、様々なDeepLearningの実装手法を学習する方法を解説します(Part 1)。[1] 機械学習そのものが初心者の方へ
[2] これからPyTorchを学びはじめる方へ
[3] 画像分類の転移学習とファインチューニング
機械学習の実装手法の学習
</p>
<div style='clear: both;'></div>
<p>
<img width="140" height="140" alt="新型コロナウイルス感染症等のワクチンの世界的な研究開発の促進のためエピトープ予測データセットとソースコードを無償公開｜フューチャー株式会社のプレスリリース" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/314/228/thumb/d4374-406-444242-0.png?1596037960" />
<strong style='display: block;'><a href="https://prtimes.jp/main/html/rd/p/000000406.000004374.html?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">新型コロナウイルス感染症等のワクチンの世界的な研究開発の促進のためエピトープ予測データセットとソースコードを無償公開｜フューチャー株式会社のプレスリリース</a> &mdash; <a href="https://prtimes.jp/main/html/rd/p/000000406.000004374.html">prtimes.jp</a></strong>
フューチャー株式会社のプレスリリース（2020年7月29日 11時00分）新型コロナウイルス感染症等のワクチンの世界的な研究開発の促進のためエピトープ予測データセットとソースコードを無償公開
</p>
<div style='clear: both;'></div>
<p><p>新型コロナウイルス感染症のワクチンの研究開発を促す目的で、Kaggle上にデータセットとソースコードを無償公開。Kaggleに関するプレスリリースは増えている印象で、27日にはSIGNATE「<a href="https://signate.jp/competitions/256" target="_blank">第3回AIエッジコンテスト（アルゴリズムコンテスト②）</a>」での優勝に関する<a href="https://www.westjr.co.jp/press/article/2020/07/page_16377.html" target="_blank">発表</a>がJR西日本から出ています。</p></p>
