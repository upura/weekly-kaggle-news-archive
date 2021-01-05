# Weekly Kaggle News #25
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-25-252615
<h3><h2>News</h2><p>ハイパーパラメータ調整ツール「Optuna」の<a href="https://github.com/optuna/optuna/releases/tag/v1.5.0" target="_blank">v1.5.0</a>が1日にリリースされ、LightGBMでの交差検証スコアを最適化する拡張機能「LightGBMTunerCV」が搭載されました。<a href="https://blog.amedama.jp/entry/optuna-lightgbm-tunercv" target="_blank">早速試している記事</a>では、簡単な使い方や学習済モデルの取り出し方などが紹介されています。</p><p>最先端の自然言語処理モデルを取り扱うHugging Faceのライブラリ「<a href="https://github.com/huggingface/transformers" target="_blank">Transformers</a>」に、今週も新たなモデルが追加されました。「<a href="https://twitter.com/huggingface/status/1267829830659174400?s=20" target="_blank">Longformer</a>」はBERTよりも長い文を扱えるモデルで、「<a href="https://twitter.com/huggingface/status/1267456127379349505?s=20" target="_blank">PruneBERT</a>」はBERT本来の性能を極力保ちながら軽量化したモデルです。</p><h2>Competitions</h2><p>「<a href="https://atma.connpass.com/event/175139/" target="_blank">atmaCup オンサイトデータコンペ#5</a>」が5月29日〜6月6日18時にオンライン開催されています。初の学術業界からの出題で、実験観測データを用いて実験結果を予測する2値分類問題です。200を超えるチームが参加中で、盛り上がりは<a href="https://guruguru.ml/competitions/10/leaderboard" target="_blank">公開順位表</a>やtwitterのハッシュタグ「<a href="https://twitter.com/search?q=%23atmaCup&amp;src=typed_query" target="_blank">#atmaCup</a>」などで確認できます。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="自然言語処理で活躍するTransformerを取り入れた物体認識モデルDETRの紹介 - ほろ酔い開発日誌" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/044/813/thumb/20200530180018.jpg?1590831715" />
<strong style='display: block;'><a href="https://blog.seishin55.com/entry/2020/05/30/175811?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">自然言語処理で活躍するTransformerを取り入れた物体認識モデルDETRの紹介 - ほろ酔い開発日誌</a> &mdash; <a href="https://blog.seishin55.com/entry/2020/05/30/175811">blog.seishin55.com</a></strong>
はじめに 今回は、自然言語界隈に発展をもたらし、デファクトスタンダードとなったTransformerのモデルを物体認識に取り入れた論文(End-to-End Object Detection with Transformers 2020/05/26 on arXiv)を紹介します。
</p>
<div style='clear: both;'></div>
<p><p>自然言語処理分野で飛躍的な成果を挙げている「Transformer」を用いて物体検出を解く「DETR」の紹介記事。モデル・損失関数・実験結果などの概要がまとまっています。</p></p>
<p>
<img width="140" height="140" alt="動的な計算グラフの型とshapeの“半”静的推論 | Preferred Networks Research &amp; Development" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/070/034/thumb/image2.png?1591281747" />
<strong style='display: block;'><a href="https://tech.preferred.jp/ja/blog/semi-static-type-shape-and-symbolic-shape-inference/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">動的な計算グラフの型とshapeの“半”静的推論 | Preferred Networks Research &amp; Development</a> &mdash; <a href="https://tech.preferred.jp/ja/blog/semi-static-type-shape-and-symbolic-shape-inference/">tech.preferred.jp</a></strong>
本記事は、2019年インターンとして勤務した服部桃子さんによる寄稿です。 こんにちは、2019年度PFN夏季インターン生の服部桃子と申します。 私は今回のインターンで、Chainerを用いてニューラルネットワークを記述しているPythonスクリプト中の式の型とshapeを
</p>
<div style='clear: both;'></div>
<p><p>ニューラルネットワークを記述しているPythonスクリプト中の式の型とshapeを推論する機能の開発に関する記事。一定の前提条件下でshapeなどを推論することで、開発者の「printデバッグ」の回避につながる機能です。</p></p>
<p>
<img width="140" height="140" alt="GitHub - imdeepmind/NeuralPy: NeuralPy: A Keras like deep learning library works on top of PyTorch" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/070/055/thumb/34741145?1591281949" />
<strong style='display: block;'><a href="https://github.com/imdeepmind/NeuralPy?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">GitHub - imdeepmind/NeuralPy: NeuralPy: A Keras like deep learning library works on top of PyTorch</a> &mdash; <a href="https://github.com/imdeepmind/NeuralPy">github.com</a></strong>
NeuralPy:  A Keras like deep learning library works on top of PyTorch - imdeepmind/NeuralPy
</p>
<div style='clear: both;'></div>
<p><p>Kerasのような仕組みで、PyTorchベースのNNモデルが構築できるライブラリ。モデルの学習・推論が手軽にできる利点がありそうです。</p></p>
<p>
<strong style='display: block;'><a href="https://www.kaggle.com/c/siim-isic-melanoma-classification/discussion/155672?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">SIIM-ISIC Melanoma Classification | Kaggle</a></strong>
Identify melanoma in lesion images
</p>
<p><p>先週始まったKaggle「<a href="https://www.kaggle.com/c/siim-isic-melanoma-classification" target="_blank">SIIM-ISIC Melanoma Classification</a>」コンペについて、Kaggleの全4カテゴリでGrandmasterの称号を持つ<a href="https://www.kaggle.com/abhishek" target="_blank">Abhishekさん</a>がチュートリアルのYouTube動画を公開。皮膚がんの一種「Melanoma」を画像から判定するコンペです。</p></p>
<p>
<img width="140" height="140" alt="NLP Colab Repository - Towards AI — Multidisciplinary Science Journal - Medium" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/070/189/thumb/0*wZjU9Hx8l6IpUmoT?1591282711" />
<strong style='display: block;'><a href="https://medium.com/towards-artificial-intelligence/nlp-colab-repository-65136d3e45da?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">NLP Colab Repository - Towards AI — Multidisciplinary Science Journal - Medium</a> &mdash; <a href="https://medium.com/towards-artificial-intelligence/nlp-colab-repository-65136d3e45da">medium.com</a></strong>
In January, we released the Big Bad NLP Database to help ML developers get exposed to quality and diverse datasets. And in that time, as the NLP industry continued to mature, we began to explore…
</p>
<div style='clear: both;'></div>
<p><p>さまざまな自然言語処理タスクに取り組むGoogle Colabリンクをまとめたデータベース「The Super Duper NLP Repo」の紹介記事。41ファイルが3日に<a href="https://twitter.com/Quantum_Stat/status/1268144084641878019?s=20" target="_blank">新規追加</a>されています。</p></p>
<p>
<img width="140" height="140" alt="regonn&amp;curry.fm@ポッドキャストやっています on Twitter: &quot;#regonn_curry_fm #80 2020/6/5 20時10分開始 https://t.co/1NSQdm1i2Q @YouTubeより 今日の80回目の収録で、本日、初のyoutubeでの生放送です。 よろしくお願いします。&quot;" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/072/597/thumb/0-NilqwP_400x400.jpg?1591317565" />
<strong style='display: block;'><a href="https://twitter.com/regonn_curry/status/1268686630480678913?s=20&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">regonn&amp;curry.fm@ポッドキャストやっています on Twitter: &quot;#regonn_curry_fm #80 2020/6/5 20時10分開始 https://t.co/1NSQdm1i2Q @YouTubeより 今日の80回目の収録で、本日、初のyoutubeでの生放送です。 よろしくお願いします。&quot;</a> &mdash; <a href="https://twitter.com/regonn_curry/status/1268686630480678913?s=20">twitter.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>Kaggle関連の話題を取り扱っているPodcastが第80回を迎え、基盤をYouTubeに変更。<a href="https://anchor.fm/regonn-curry-fm/episodes/079-Kaggler-eeucfr" target="_blank">第79回の放送</a>によると、<a href="https://www.kaggle.com/currypurin" target="_blank">currypurinさん</a>は1日に企業勤めになり、約2年間の「専業Kaggler」生活を終えました。専業Kaggler生活については、昨年末の「Kaggle Days Tokyo」でも<a href="https://youtu.be/Z0F7e5eidsk" target="_blank">講演</a>しています。</p></p>
