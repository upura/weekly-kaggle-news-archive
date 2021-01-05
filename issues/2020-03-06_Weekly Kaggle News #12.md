# Weekly Kaggle News #12
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-12-229928
<h3><h2>News</h2><p>新型コロナウイルスによる感染症（COVID-19）の世界的流行に歯止めがかからず、各種イベントの中止・延期・オンライン開催が決まっています。4月に開催予定だった「<a href="https://kaggledays.com/sanfrancisco2020/" target="_blank">Kaggle Days San Francisco</a>」は、<a href="https://twitter.com/mlaass1/status/1234851067470471168?s=20" target="_blank">開催の中止が決まりました</a>。</p><p>優秀なKagglerの積極採用を進めている<a href="https://developer.nvidia.com/rapids" target="_blank">NVIDIAのRAPIDS</a>チームに、日本人Grandmasterの<a href="https://twitter.com/0verfit/status/1235044137793015810?s=20" target="_blank">ONODERAさんが参画</a>しました。先月にも2人の世界的に著名なKaggler（<a href="https://www.kaggle.com/titericz?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">Giba</a>さん、<a href="http://cpmp/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">CPMP</a>さん）が入社しており、数多くのGrandmasterが在籍しています。</p><h2>Competitions</h2><p>事前に予告されていたWalmartのデータセットを用いた時系列予測コンペが始まりました。「<a href="https://www.kaggle.com/c/m5-forecasting-accuracy" target="_blank">M5 Forecasting - Accuracy</a>」「<a href="https://www.kaggle.com/c/m5-forecasting-uncertainty" target="_blank">M5 Forecasting - Uncertainty</a>」の2コンペ同時開催で、それぞれ予測値と予測分布を提出します。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="不均衡データ分類問題をDNNで解くときの under sampling + bagging 的なアプローチ - BASE開発チームブログ" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/615/342/thumb/20200228192229.png?1582946905" />
<strong style='display: block;'><a href="https://devblog.thebase.in/entry/2020/02/29/110000?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">不均衡データ分類問題をDNNで解くときの under sampling + bagging 的なアプローチ - BASE開発チームブログ</a> &mdash; <a href="https://devblog.thebase.in/entry/2020/02/29/110000">devblog.thebase.in</a></strong>
不均衡データ分類タスクをDNNで解きたくなった際、under sampling + bagging 的なアプローチをしている論文を見つけたのでご紹介。
</p>
<div style='clear: both;'></div>
<p><p>論文 "<a href="https://users.cs.fiu.edu/~chens/PDF/ISM15.pdf" target="_blank">Deep Learning for Imbalanced Multimedia Data Classification</a>" を参考にした不均衡データへのDNN適用事例。失敗例も含めてコードと共に分かりやすく解説しています。</p></p>
<p>
<img width="140" height="140" alt="事前学習済言語モデルの動向 (2) / Survey of Pretrained Language Models - Speaker Deck" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/615/258/thumb/slide_0.jpg?1582942119" />
<strong style='display: block;'><a href="https://speakerdeck.com/kyoun/survey-of-pretrained-language-models-f6319c84-a3bc-42ed-b7b9-05e2588b12c7?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">事前学習済言語モデルの動向 (2) / Survey of Pretrained Language Models - Speaker Deck</a> &mdash; <a href="https://speakerdeck.com/kyoun/survey-of-pretrained-language-models-f6319c84-a3bc-42ed-b7b9-05e2588b12c7">speakerdeck.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>「BERT」に代表される自然言語処理の事前学習済言語モデルの網羅的なサーベイ。2019年11月30日から情報を更新した資料で、最新の話題まで取り扱っています。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2003.00415?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2003.00415] Advanced kNN: A Mature Machine Learning Series</a></strong>

</p>
<p><p>kNNを拡張した「Advanced kNN」を提案。学習データ内に存在しないクラスに属するデータに対して "unknown" と判定する機構を備えています。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2002.11940?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2002.11940] How Much Can A Retailer Sell? Sales Forecasting on Tmall</a></strong>

</p>
<p><p>アリババの金融関連会社から出た論文。小売業の売上を分析して季節性とTweedie分布の特徴を見い出し、NNとGBDTに適用することで時系列予測の精度を高めたと報告しています。</p></p>
<p>
<img width="140" height="140" alt="Kaggle「WiDS Datathon 2020」コンペ解法まとめ - u++の備忘録" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/615/594/thumb/20200229122426.png?1582961732" />
<strong style='display: block;'><a href="https://upura.hatenablog.com/entry/2020/02/29/134230?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggle「WiDS Datathon 2020」コンペ解法まとめ - u++の備忘録</a> &mdash; <a href="https://upura.hatenablog.com/entry/2020/02/29/134230">upura.hatenablog.com</a></strong>
先日まで参加していたKaggle「WiDS Datathon 2020」コンペの解法まとめです。「検査データから1週間後の生死を当てる」というシンプルなテーブルコンペでした。本記事では、自分の復習用にザッとまとめたメモを共有します。 Place Link 2 https://www.kaggle.com/c/widsdatathon2020/discussion/132387 3 https://www.kaggle.com/c/widsdatathon2020/discussion/132292 4 https://www.kaggle.com/c/widsdatathon2020/disc…
</p>
<div style='clear: both;'></div>
<p><p>Kaggleで開催されていた「WiDS Datathon 2020」コンペの解法まとめ。「検査データから1週間後の生死を当てる」というシンプルなテーブルコンペでした。</p></p>
<p>
<img width="140" height="140" alt="“The 3 ingredients to our success.” | Winners dish on their solution to Google’s QUEST Q&amp;A Labeling | Kaggle Winner’s Interview" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/635/604/thumb/1*uW8T1LXPpma7P_FMBFgJqg.jpeg?1583391166" />
<strong style='display: block;'><a href="https://medium.com/kaggle-blog/the-3-ingredients-to-our-success-winners-dish-on-their-solution-to-googles-quest-q-a-labeling-c1a63014b88?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">“The 3 ingredients to our success.” | Winners dish on their solution to Google’s QUEST Q&amp;A Labeling | Kaggle Winner’s Interview</a> &mdash; <a href="https://medium.com/kaggle-blog/the-3-ingredients-to-our-success-winners-dish-on-their-solution-to-googles-quest-q-a-labeling-c1a63014b88">medium.com</a></strong>
Congratulations to the (four!) first-place winners of the Quest Q&amp;A Labeling competition, Dmitriy Danevskiy, Yury Kashnitsky, Oleg Yaroshevskiy, and Dmitry Abulkhanov who make up the team…
</p>
<div style='clear: both;'></div>
<p><p>Kaggle公式ブログに掲載された、Kaggle「<a href="https://www.kaggle.com/c/google-quest-challenge" target="_blank">Google QUEST Q&amp;A Labeling</a>」1位チームへのインタビュー。鍵となった言語モデルの事前学習・Pseudo-labeling・後処理について解説しています。</p></p>
<p>
<img width="140" height="140" alt="【Kaggle】DSBコンペ 反省会 備忘録 | うみろぐ" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/617/727/thumb/a565eff4102f6da9c0f7d78f676f13a8.png?1583045638" />
<strong style='display: block;'><a href="https://umi-log.com/kaggle-dsb-mtg/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">【Kaggle】DSBコンペ 反省会 備忘録 | うみろぐ</a> &mdash; <a href="https://umi-log.com/kaggle-dsb-mtg/">umi-log.com</a></strong>
DSBコンペ(DataScienceBowl 2019)の反省会を2/29 (土) に開催しました。金メダルチームが3チームも参加するなど、非常に学びの多い会でした。簡単ですが、備忘として記録を残しておきます。shirokane_frien
</p>
<div style='clear: both;'></div>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/data-science-bowl-2019" target="_blank">2019 Data Science Bowl</a>」コンペの反省会の資料の一覧や発表メモ。2位の方の解法、10位の方の「shake up」に関する知見、カスタムロスを用いた評価指標の最適化など、盛りだくさんの内容です。</p></p>
<p>
<img width="140" height="140" alt="Python: Optuna を使って QWK の閾値を最適化してみる - CUBE SUGAR CONTAINER" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/617/622/thumb/41zp6hN7f_L._SL160_.jpg?1583036285" />
<strong style='display: block;'><a href="https://blog.amedama.jp/entry/optuna-qwk-optimization?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Python: Optuna を使って QWK の閾値を最適化してみる - CUBE SUGAR CONTAINER</a> &mdash; <a href="https://blog.amedama.jp/entry/optuna-qwk-optimization">blog.amedama.jp</a></strong>
最近、Twitter のタイムラインで QWK (Quadratic Weighted Kappa: 二次の重み付きカッパ係数) の最適化が話題になっていたので個人的に調べていた。 QWK は順序つきの多値分類問題を評価するための指標で、予測を大きく外すほど大きなペナルティが与えられるようになっている。 また、予測値の分布が結果に影響する点も特徴的で、この点が今回取り扱う最適化にも関係してくる。 QWK の最適化については、Kaggle 本と、その著者 @Maxwell_110 さんによる次のブログエントリが詳しい。 ようするに、真のラベルの分布に沿った形で予測しないと最適な結果が得られない、…
</p>
<div style='clear: both;'></div>
<p><p>ハイパーパラメータ調整ツール「Optuna」を用いて、評価指標「QWK」の最適化を試みる記事。連続値を離散値に変換するための閾値を探索しています。</p></p>
<p>
<img width="140" height="140" alt="「Linear Quiz Blending」の概説 - u++の備忘録" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/626/142/thumb/20200229111523.png?1583372622" />
<strong style='display: block;'><a href="https://upura.hatenablog.com/entry/2020/03/01/190400?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">「Linear Quiz Blending」の概説 - u++の備忘録</a> &mdash; <a href="https://upura.hatenablog.com/entry/2020/03/01/190400">upura.hatenablog.com</a></strong>
"Linear Quiz Blending" や "Netflix Blending" と呼ばれる技法について、少し前にまとめたスライドを公開しました。 少し前からKaggleをやっている方だと「Kaggle Tokyo Meetup #5」*1での、Kaggle Grandmasterのsmlyさんの発表が印象的かもしれません。 Kaggle Avito Demand Prediction Challenge 9th Place Solution from Jin Zhan 実装はたとえば次のライブラリのものがあるそうです。 Linear Quiz Blending、実装はこんな感じ htt…
</p>
<div style='clear: both;'></div>
<p><p>"Linear Quiz Blending" や "Netflix Blending" と呼ばれるアンサンブル技法についてまとめた記事。数式を交えて解説しています。</p></p>
<p>
<img width="140" height="140" alt="CatBoostのテキストカラム指定機能を試す - u++の備忘録" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/635/852/thumb/20200303195115.png?1583395877" />
<strong style='display: block;'><a href="https://upura.hatenablog.com/entry/2020/03/03/195929?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">CatBoostのテキストカラム指定機能を試す - u++の備忘録</a> &mdash; <a href="https://upura.hatenablog.com/entry/2020/03/03/195929">upura.hatenablog.com</a></strong>
CatBoostの（カテゴリカラム指定ならぬ）テキストカラム指定機能を試してみました。本記事の内容は、discussion*1に投稿済です。 Kaggle「Real or Not? NLP with Disaster Tweets」*2コンペのデータセットを利用しました。 target_col = 'target' text_cols = ['text'] categorical_cols = ['keyword', 'location'] train_pool = Pool( X_tr, y_tr, cat_features=categorical_cols, text_features=t…
</p>
<div style='clear: both;'></div>
<p><p>CatBoostの（カテゴリカラム指定ならぬ）テキストカラム指定機能を試した記事。生の文章が入ったカラムを指定できるので、サクッとベンチマークを作るには便利だと感じました。</p></p>
<p>
<img width="140" height="140" alt="Semi supervised, weakly-supervised, unsupervised, and active learning" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/635/776/thumb/semi-supervisedweakly-supervisedunsupervisedandactivelearning-200305074544-thumbnail-4.jpg?1583395040" />
<strong style='display: block;'><a href="https://www.slideshare.net/ren4yu/semi-supervised-weaklysupervised-unsupervised-and-active-learning?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Semi supervised, weakly-supervised, unsupervised, and active learning</a> &mdash; <a href="https://www.slideshare.net/ren4yu/semi-supervised-weaklysupervised-unsupervised-and-active-learning">www.slideshare.net</a></strong>
An overview of semi supervised learning, weakly-supervised learning, unsupervised learning, and active learning. Focused on recent deep learning-based image re…
</p>
<div style='clear: both;'></div>
<p><p>「半教師あり学習」周りのサーベイ。Semi-supervised Learning、Weakly-supervised Learning、Unsupervised Learning、Active Learning について、画像処理に関する事例を中心に手法をまとめています。</p></p>
<p>
<strong style='display: block;'><a href="https://hanshakaijin.booth.pm/items/1870011?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">特徴量モンスター - 反社会人サークル - BOOTH</a></strong>
現代のITエンジニアには欠かせないスキル、機械学習をカードゲーム化！ 技術書典8で頒布予定でした。
</p>
<p><p>「タイタニック号の生存者予測」を題材にしたカードゲーム。特徴量モンスター＆アルゴリズムマシンを駆使して、最終的には実際に特設サイト上で精度計算を実行する枠組みになっています。</p></p>
