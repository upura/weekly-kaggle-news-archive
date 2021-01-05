# Weekly Kaggle News #11
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-11-228494
<h3><h2>News</h2><p><a href="https://developer.nvidia.com/rapids" target="_blank">NVIDIAのRAPIDSチーム</a>が、優秀なKagglerの積極採用を進めています。Competitionsのランキング3位（過去最高1位）の<a href="https://www.kaggle.com/titericz" target="_blank">Giba</a>さんは2月25日、<a href="https://twitter.com/Giba1/status/1231982874741612544?s=20" target="_blank">同社で働き始めたと報告</a>しました。2月11日にはCompetitionsで7位、Discussionで1位の<a href="http://CPMP" target="_blank">CPMP</a>さんも<a href="https://twitter.com/JFPuget/status/1226887982248087552?s=20" target="_blank">参画</a>しており、数多くのGrandmasterが在籍しています。<a href="https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Machine-Learning-Deep-Learning-Data-Scientist--RAPIDS---AI_JR1923952?utm_campaign=Weekly+Kaggle+News&amp;utm_medium=email&amp;utm_source=Revue+newsletter" target="_blank">募集要項</a>によると、業務内容にはKaggleコンペへの参加も含まれています。</p><p>PyTorchの学習用コードを簡潔に記述できるフレームワークの一つ「Catalyst」の<a href="https://github.com/catalyst-team/catalyst/releases/tag/v20.02.4" target="_blank">v20.02.4</a>がリリースされ、画像分類・自然言語処理・推薦・GANを扱った<a href="https://twitter.com/catalyst_core/status/1231638884037079040" target="_blank">デモが公開</a>されました。同一の枠組みで複数の分野を処理できるのは利便性が高そうです。</p><p>勾配ブースティング決定木の実装として根強い人気を誇る「XGBoost」は、<a href="https://github.com/dmlc/xgboost/releases/tag/v1.0.0" target="_blank">v1.0.0</a>がリリースされました。</p><h2>Competitions</h2><p>イオンチャネルの開閉状態を予測するKaggle「<a href="https://www.kaggle.com/c/liverpool-ion-switching" target="_blank">University of Liverpool - Ion Switching</a>」コンペが24日（UTC）に始まりました。当初の評価指標は「<a href="https://www.kaggle.com/aroraaman/quadratic-kappa-metric-explained-in-5-simple-steps" target="_blank">quadratic weighted kappa</a>」でしたが、1日経たずして1位のスコアが0.997にまで達した結果、<a href="https://www.kaggle.com/c/liverpool-ion-switching/discussion/132607" target="_blank">27日に「Macro F1」に変更されました</a>。</p><p>ProbSpace「<a href="https://prob.space/competitions/real_estate_2020" target="_blank">不動産取引価格予測</a>」コンペが26日に始まりました。ProbSpaceとしては初めて、順位表がpublicとprivateに分割されています。</p><p>SIGNATE「<a href="https://signate.jp/competitions/218" target="_blank">国立国会図書館の画像データレイアウト認識</a>」は27日に終わりました。<a href="https://twitter.com/coz_a_1980/status/1233180007381340160?s=20" target="_blank">優勝者によると</a>、物体検出のためのアンサンブル手法「<a href="https://www.kaggle.com/c/open-images-2019-object-detection/discussion/115086" target="_blank">Weighted Boxes Fusion (WBF)</a>」が効果的だったようです。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Google QUEST Q&amp;A Labeling コンペの反省文 - guchiBLO はてな" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/605/605/thumb/20200227083538.png?1582793580" />
<strong style='display: block;'><a href="https://guchio3.hatenablog.com/entry/2020/02/27/100505?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Google QUEST Q&amp;A Labeling コンペの反省文 - guchiBLO はてな</a> &mdash; <a href="https://guchio3.hatenablog.com/entry/2020/02/27/100505">guchio3.hatenablog.com</a></strong>
本記事の概要 kaggle の NLP コンペである Google QUEST Q&amp;A Labeling に参加し、その社内反省会を主催したので、その時の資料をブログに落としておきます。筆者は 1,571 チーム中 19 位でした。 shake 力たりんかったか... pic.twitter.com/L4bJGp5oil— ぐちお (@ihcgT_Ykchi) February 11, 2020 NLP コンペには初めて参加してのですが、系列データを NN でさばく上での学びが多く非常に楽しめました。個人的には良いコンペだったと感じていて、コンペ終了後にはブログ化する方々*1や勉強会を開催する…
</p>
<div style='clear: both;'></div>
<p><p>先日終了したKaggle「<a href="https://www.kaggle.com/c/google-quest-challenge" target="_blank">Google QUEST Q&amp;A Labeling</a>」の上位解法がまとめられた記事。コンペ概要や近年のNLPコンペで標準となっている基礎知識も解説されています。</p></p>
<p>
<img width="140" height="140" alt="How We Implement Hyperband in Optuna - Optuna - Medium" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/605/618/thumb/0*PQgHqRp7i77Tkjc_?1582793853" />
<strong style='display: block;'><a href="https://medium.com/optuna/optuna-supports-hyperband-93b0cae1a137?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">How We Implement Hyperband in Optuna - Optuna - Medium</a> &mdash; <a href="https://medium.com/optuna/optuna-supports-hyperband-93b0cae1a137">medium.com</a></strong>
Optuna has supported Hyperband since v1.1.0 as an experimental feature. In this post, some challenges in its implementation are described.
</p>
<div style='clear: both;'></div>
<p><p>ハイパーパラメータ調整ツール「Optuna」のv1.1.0から導入された探索アルゴリズム「<a href="http://jmlr.org/papers/volume18/16-558/16-558.pdf" target="_blank">Hyperband</a>」について、実装者による解説。実装方法や実験結果も含めて報告しています。</p></p>
<p>
<img width="140" height="140" alt="Kaggle「WiDS Datathon 2020」コンペ14位の取り組み - u++の備忘録" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/605/626/thumb/20200225130713.png?1582793985" />
<strong style='display: block;'><a href="https://upura.hatenablog.com/entry/2020/02/25/183400?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggle「WiDS Datathon 2020」コンペ14位の取り組み - u++の備忘録</a> &mdash; <a href="https://upura.hatenablog.com/entry/2020/02/25/183400">upura.hatenablog.com</a></strong>
Kaggleで開催されていた「WiDS Datathon 2020」コンペに参加して、public 7位、private 14位でした。shake downしてしまいましたが、ほぼベストの提出を選択できていたので悔いはありません。「検査データから1週間後の生死を当てる」というシンプルなテーブルコンペで、いろんな技術が検証できて面白かったです。 取り組み 既にdiscussionに投稿済の内容を日本語で掲載します。 チームメイトの方と共に、多様なモデルを作りました。それぞれがstackingモデルを作り、最後の2サブとして選択しています。 mtmt モデル u++ モデル LightGBMモデル…
</p>
<div style='clear: both;'></div>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/widsdatathon2020/" target="_blank">WiDS Datathon 2020</a>」コンペ14位解法。メダルなしでしたが、近年のKaggleには珍しいシンプルなテーブルコンペで、Discussionには上位解法も共有されています。</p></p>
<p>
<img width="140" height="140" alt="ML design: 機械学習を確かならしめる「メタ」な枠組み - 渋谷駅前で働くデータサイエンティストのブログ" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/605/631/thumb/20200212152810.png?1582794069" />
<strong style='display: block;'><a href="https://tjo.hatenablog.com/entry/2020/02/24/201203?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ML design: 機械学習を確かならしめる「メタ」な枠組み - 渋谷駅前で働くデータサイエンティストのブログ</a> &mdash; <a href="https://tjo.hatenablog.com/entry/2020/02/24/201203">tjo.hatenablog.com</a></strong>
(By Gufosowa - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=82298768)ここ最近、事あるごとに僕が色々な人たちに提案している概念として"ML design"というものがあります。これは元々"ML Ops"（DevOpsと同じように機械学習のシステム基盤などを包含する考え方）に対して「機械学習モデリングを運用する上で注意すべき点って多いよね」ということで、その注意点をまとめたものを一つの体系として扱えないかという趣旨で僕が勝手に言い出したものです。 言い方を変えると、統計分析に…
</p>
<div style='clear: both;'></div>
<p><p>機械学習モデルを運用する上での注意点について論じた記事。『<a href="https://www.amazon.co.jp/dp/B07YTDBC3Z" target="_blank">Kaggleで勝つデータ分析の技術</a>』を題材に、AutoMLを活用する観点で必要な機械学習に関する知見を簡潔にまとめています。</p></p>
<p>
<img width="140" height="140" alt="Google AI Blog: Open Images V6 — Now Featuring Localized Narratives" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/609/267/thumb/GoogleAI_logo_horizontal_color_rgb.png?1582852317" />
<strong style='display: block;'><a href="https://ai.googleblog.com/2020/02/open-images-v6-now-featuring-localized.html?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Google AI Blog: Open Images V6 — Now Featuring Localized Narratives</a> &mdash; <a href="https://ai.googleblog.com/2020/02/open-images-v6-now-featuring-localized.html">ai.googleblog.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>Googleの大規模画像データセット「Open Images」の最新版が公開されました。視覚的関係性・人間の行動などのラベル追加や、テキストも付与したマルチモーダルな「Localized Narratives」の新設などの更新があります。</p></p>
