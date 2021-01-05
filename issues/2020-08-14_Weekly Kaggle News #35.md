# Weekly Kaggle News #35
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-35-269337
<h3><h2>News</h2><p>Kaggle上の実行環境「Notebooks」でのGPU利用時間の制限が緩和されました。時間は不確定ですが、需要に応じて現状の週30時間よりも多く利用できる<a href="https://www.kaggle.com/product-feedback/173129" target="_blank">仕組み</a>とのことです。利用可能な時間は<a href="http://kaggle.com/me/account" target="_blank">ユーザページ</a>で確認でき、今週は39時間が割り当てられています。Notebooks関連では<a href="https://www.kaggle.com/product-feedback/173801" target="_blank">UI/UXの更新</a>もあり、セル単位の出力がログでも確認できるようになりました。変更内容については、KaggleのProduct Managerによる<a href="https://twitter.com/MeganRisdal/status/1292897667249369088" target="_blank">一連の投稿</a>が分かりやすいです。</p><p>Kaggleで頻出の機械学習ライブラリ「LightGBM」の<a href="https://github.com/microsoft/LightGBM/releases/tag/v3.0.0rc1" target="_blank">v3.0.0rc1</a>の内容がプレリリースされています。交差検証時に個別の学習モデルを取り出せる機能などが実装されています。</p><h2>Competitions</h2><p>4日に終了したKaggle「<a href="https://www.kaggle.com/c/global-wheat-detection" target="_blank">Global Wheat Detection</a>」コンペでは、未だにPrivate Leaderboardの結果が公表されていません。一部のテストデータの更新と再計算が<a href="https://www.kaggle.com/c/global-wheat-detection/discussion/173586" target="_blank">予告</a>されており、14日現在で残り1日以内で終了すると表示されています。問題設計や上位解法などは、<a href="https://mhiro216.hatenablog.com/entry/2020/08/09/205640" target="_blank">参加者のブログ</a>に簡潔にまとまっています。</p><p>ProbSpace「<a href="https://prob.space/competitions/re_real_estate_2020" target="_blank">Re：不動産取引価格予測</a>」コンペが10日に終了しました。優勝解法は<a href="https://prob.space/competitions/re_real_estate_2020/discussions/Angus_Chang-Post5ac561a421209f743fc4" target="_blank">トピック</a>で公開されています。</p></h3>
<hr>
<p>
<strong style='display: block;'><a href="https://www.tensorflow.org/api_docs/python/tf/experimental/numpy?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Module: tf.experimental.numpy  |  TensorFlow Core v2.3.0</a></strong>
This module provides a subset of NumPy API, built on top of TensorFlow
operations. APIs are based on and have been tested with NumPy 1.16 version.
</p>
<p><p>GPUやTPUでNumPyを高速化できるモジュール。開発者がTwitterで<a href="https://twitter.com/fchollet/status/1292893864986984448?s=20" target="_blank">紹介</a>し、大きな反響を呼びました。</p></p>
<p>
<img width="140" height="140" alt="Kaggle のデータ分析コンペ TReNDS Neuroimaging で『3位 / 1,047チーム』を獲得しました :) | MoT Lab (Mobility Technologies Tech Blog)" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/365/710/thumb/og-image.png?1597159068" />
<strong style='display: block;'><a href="https://lab.mo-t.com/blog/kaggle-trends?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggle のデータ分析コンペ TReNDS Neuroimaging で『3位 / 1,047チーム』を獲得しました :) | MoT Lab (Mobility Technologies Tech Blog)</a> &mdash; <a href="https://lab.mo-t.com/blog/kaggle-trends">lab.mo-t.com</a></strong>
MoT Labは、Mobility Technologiesが技術情報などを紹介するテックブログです。
</p>
<div style='clear: both;'></div>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/trends-assessment-prediction?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">TReNDS Neuroimaging</a>」コンペに個人で3位入賞したKaggle Masterの<a href="https://www.kaggle.com/shimacos" target="_blank">shimacos</a>さんによる取り組み紹介。時系列に沿って具体的な内容が記載され、しばしば話題になる「実務でどのような役に立つのか」という観点についても言及しています。</p></p>
<p>
<img width="140" height="140" alt="第4回Tellus Satellite Challenge開催！テーマは「海岸線抽出」 | 宙畑" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/365/767/thumb/bbf34cf32c8da376fe7f8f0eeead9de1-1300x871.png?1597159223" />
<strong style='display: block;'><a href="https://sorabatake.jp/14130/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">第4回Tellus Satellite Challenge開催！テーマは「海岸線抽出」 | 宙畑</a> &mdash; <a href="https://sorabatake.jp/14130/">sorabatake.jp</a></strong>
衛星画像を用いたセグメンテーションのコンペ第4回Tellus Satellite Challengeについて、コンペの詳細と参考になる論文や資料をまとめました。
</p>
<div style='clear: both;'></div>
<p><p>SIGNATEで6日に始まった「<a href="https://signate.jp/competitions/284?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">The 4th Tellus Satellite Challenge</a>」コンペの紹介記事。画像から海岸線を抽出するタスクについて、コンペの意義や参考文献などがまとめられています。</p></p>
<p>
<img width="140" height="140" alt="Best Practices from Building a Machine Learning Bot for Halite | Two Sigma" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/370/333/thumb/Halite_2x1b.jpg?1597250881" />
<strong style='display: block;'><a href="https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Best Practices from Building a Machine Learning Bot for Halite | Two Sigma</a> &mdash; <a href="https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/">www.twosigma.com</a></strong>
An overview of best practices derived from building a machine-learning based starter bot for Halite, Two Sigma's public artificial intelligence programming challenge. 
</p>
<div style='clear: both;'></div>
<p><p>戦略ゲーム「Halite」を戦うAIを作るコンペから得られた知見をまとめた2018年公開の記事。「強化学習が必ずしも最良ではない」「小さな問題から取り組む」など至言が記されています。現在はKaggle上で「<a href="https://www.kaggle.com/c/halite" target="_blank">Halite by Two Sigma</a>」が開催中です。</p></p>
<p>
<img width="140" height="140" alt="language models まとめ - Speaker Deck" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/375/802/thumb/slide_0.jpg?1597372066" />
<strong style='display: block;'><a href="https://speakerdeck.com/sakami/language-models-matome?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">language models まとめ - Speaker Deck</a> &mdash; <a href="https://speakerdeck.com/sakami/language-models-matome">speakerdeck.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>Kaggle Masterの<a href="https://www.kaggle.com/sakami" target="_blank">sakami</a>さんによるニューラルネットワークを用いた近年の言語モデルの紹介スライド。Kaggle「<a href="https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification" target="_blank">Jigsaw Unintended Bias in Toxicity Classification</a>」コンペを題材に、BERT・GPT-2・XLNetなどの実験結果と所感を掲載しています。</p></p>
<p>
<img width="140" height="140" alt="ぐるぐる" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/375/837/thumb/guruguru_icon_reverse.png?1597373438" />
<strong style='display: block;'><a href="https://www.guruguru.ml/rankings/competition?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ぐるぐる</a> &mdash; <a href="https://www.guruguru.ml/rankings/competition">www.guruguru.ml</a></strong>
ぐるぐるはデータ解析者のための、データ分析プラットフォームです。
</p>
<div style='clear: both;'></div>
<p><p>atma社が開催しているコンペ「<a href="https://atma.connpass.com/" target="_blank">atmaCup</a>」に、ユーザーランキングシステムが<a href="https://www.guruguru.ml/rankings/competition" target="_blank">導入</a>されました。コンペとディスカッションに分かれており、<a href="https://www.guruguru.ml/rankings/help" target="_blank">算出方法</a>はこちらで公開されています。</p></p>
<p>
<img width="140" height="140" alt="Celebrating Four Years of SpaceNet" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/375/830/thumb/Slide1.jpg?1597372924" />
<strong style='display: block;'><a href="https://spacenet.ai/anniversary/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Celebrating Four Years of SpaceNet</a> &mdash; <a href="https://spacenet.ai/anniversary/">spacenet.ai</a></strong>
<p>SpaceNet was founded by IQT Labs’ CosmiQ Works and Maxar Technologies (then DigitalGlobe) in August 2016 as an informal collaboration aimed at accelerating the development of open source machine learning capabilities specifically for geospatial use cases. </p>
</p>
<div style='clear: both;'></div>
<p><p>過去6度のコンペを開催してきた「SpaceNet」が4周年を迎え、ユーザランキングを公開。日本からはKaggle Grandmasterの<a href="https://www.kaggle.com/confirm" target="_blank">Kohei</a>さんが2位に入っています。</p></p>
