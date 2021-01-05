# Weekly Kaggle News #16
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-16-236171
<h3><h2>News</h2><p>直近の多くのコンペで「The Zoo」としてチームを組んで優れた成績を収めているCompetitionランク4位の<a href="https://www.kaggle.com/philippsinger" target="_blank">Psi</a>さんと5位の<a href="https://www.kaggle.com/dott1718" target="_blank">dott</a>さんが、4月1日付で<a href="https://www.h2o.ai/" target="_blank">H2O.ai</a>のKaggle Grandmasterが集まるチームへ参画しました。それぞれ自身のtwitterで発表しました（<a href="https://twitter.com/ph_singer/status/1245415606804938753?s=20" target="_blank">リンク1</a>、<a href="https://twitter.com/dott1718/status/1245417941165801473?s=20" target="_blank">リンク2</a>）。2月ごろに著名Kagglerの加入で注目を集めた<a href="https://developer.nvidia.com/rapids?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">NVIDIAのRAPIDS</a>チームと並び、世界有数のKaggleチームになりそうです。</p><p>日本の機械学習コンペプラットフォーム「SIGNATE」は、過去に終了済みのコンペで順位を競う「<a href="https://signate.jp/features/state-of-the-art-challenge" target="_blank">State-of-the-Art Challenge</a>」を開始しました。特定コンペに限定されていますが、Kaggleと同様にコンペ終了後も提出スコアを確認できるようになりました。同じく機械学習コンペプラットフォーム「Nishika」は、<a href="https://www.nishika.com/qa" target="_blank">データサイエンスに特化したQ&amp;Aサービス</a>を公開しました。サービス開始の背景は、<a href="https://mhiro216.hatenablog.com/entry/2020/03/31/210814" target="_blank">こちら</a>にまとまっています。</p><p><strong>Competitions</strong></p><p>Kaggle「<a href="https://www.kaggle.com/c/deepfake-detection-challenge" target="_blank">Deepfake Detection Challenge</a>」コンペが日本時間4月1日に終了しました。<a href="https://www.kaggle.com/c/deepfake-detection-challenge/discussion/140417" target="_blank">数週間程度で最終結果が報告</a>される予定です。社会問題にも発展しているディープフェイク検知を目的としたコンペで、1位チームに50万ドルが授与される賞金額の大きさも話題となっています。</p><p>「<a href="https://www.kdd.org/kdd2020/kdd-cup" target="_blank">KDD CUP 2020</a>」コンペの課題が公開されています。教師あり学習2件、AutoML1件、強化学習1件の計4つの課題が設定されています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Python: 時系列データの交差検証と TimeSeriesSplit の改良について - CUBE SUGAR CONTAINER" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/734/679/thumb/20200327180723.png?1585311242" />
<strong style='display: block;'><a href="https://blog.amedama.jp/entry/time-series-cv?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Python: 時系列データの交差検証と TimeSeriesSplit の改良について - CUBE SUGAR CONTAINER</a> &mdash; <a href="https://blog.amedama.jp/entry/time-series-cv">blog.amedama.jp</a></strong>
一般的に、時系列データを扱うタスクでは過去のデータを使って未来のデータを予測することになる。 そのため、交差検証するときも過去のデータを使ってモデルを学習させた上で未来のデータを使って検証しなければいけない。 もし、未来のデータがモデルの学習データに混入すると、本来は利用できないデータにもとづいた楽観的な予測が得られてしまう。 今回は、そんな時系列データの交差検証と scikit-learn の TimeSeriesSplit の改良について書いてみる。 使った環境は次のとおり。 $ sw_vers ProductName: Mac OS X ProductVersion: 10.14.6 B…
</p>
<div style='clear: both;'></div>
<p><p>TimeSeriesSplitを特定のカラムで時系列ソートできるようなコードを公開。痒いところに手が届く改良です。</p></p>
<p>
<img width="140" height="140" alt="GANs for tabular data | Towards Data Science" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/734/767/thumb/0*7MOeXbZqEbDVuBrE?1585312557" />
<strong style='display: block;'><a href="https://towardsdatascience.com/review-of-gans-for-tabular-data-a30a2199342?gi=3b347c068100&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">GANs for tabular data | Towards Data Science</a> &mdash; <a href="https://towardsdatascience.com/review-of-gans-for-tabular-data-a30a2199342?gi=3b347c068100">towardsdatascience.com</a></strong>
We well know GANs for success in the realistic image generation. However, they can be applied in tabular data generation. We will review and examine some recent papers about tabular GANs in action…
</p>
<div style='clear: both;'></div>
<p><p>テーブルデータへのGANの適用に関する記事。2つのライブラリを検証しており、<a href="https://github.com/Diyago/GAN-for-tabular-data" target="_blank">GitHub</a>でコードも公開しています。</p></p>
<p>
<img width="140" height="140" alt="abhishek thakur on Twitter: &quot;I have made two tutorial videos using the data of two on-going @kaggle competitions. Both use BERT!!! Check them out here: @Jigsaw Multilingual Toxic Classification: https://t.co/OmPfNiGxUy Tweet Sentiment Text Extraction: https://t.co/fbAVRZzrXh :)&quot;" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/738/056/thumb/TTh9wb8T_400x400.jpg?1585380621" />
<strong style='display: block;'><a href="https://twitter.com/abhi1thakur/status/1243607938784256007?s=20&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">abhishek thakur on Twitter: &quot;I have made two tutorial videos using the data of two on-going @kaggle competitions. Both use BERT!!! Check them out here: @Jigsaw Multilingual Toxic Classification: https://t.co/OmPfNiGxUy Tweet Sentiment Text Extraction: https://t.co/fbAVRZzrXh :)&quot;</a> &mdash; <a href="https://twitter.com/abhi1thakur/status/1243607938784256007?s=20">twitter.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>Competitions、Kernels、Discussion、Datasetsの全カテゴリでGrandmasterの称号を持つ<a href="https://kaggle.com/abhishek?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">Abhishek</a>さんが、Kaggleで開催中の2つのNLPコンペについてのチュートリアル動画を公開。BERTを用いて、具体的なコードと共に解法方針を解説しています。</p></p>
<p>
<img width="140" height="140" alt="ReZeroの収束性と精度を画像認識(Cifar100)で試した記録 - statsuのblog" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/740/900/thumb/20200329025620.png?1585463736" />
<strong style='display: block;'><a href="https://st1990.hatenablog.com/entry/2020/03/29/144230?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ReZeroの収束性と精度を画像認識(Cifar100)で試した記録 - statsuのblog</a> &mdash; <a href="https://st1990.hatenablog.com/entry/2020/03/29/144230">st1990.hatenablog.com</a></strong>
ReZeroという最近提案されたDeep learning関連の手法を画像認識(Cifar100)で試したのでその記録です。 結論としては、Cifar100での画像認識では効果なかったです。 本記事の概要 ReZeroの概要 ReZeroの実装 ReZeroの検証 まとめ ReZeroの概要 ReZeroは"ReZero is All You Need: Fast Convergence at Large Depth"という論文で提案された手法です。（〇〇 is All You Needって言ってみたい…） [2003.04887] ReZero is All You Need: Fast C…
</p>
<div style='clear: both;'></div>
<p><p>論文「<a href="https://arxiv.org/abs/2003.04887" target="_blank">ReZero is All You Need: Fast Convergence at Large Depth</a>」の概説。データセット「CIFAR-10」に適用して、論文が謳う効果も確認しています。</p></p>
<p>
<img width="140" height="140" alt="Kaggleで戦いたい人のためのpandas実戦入門 - ML_BearのKaggleな日常" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/757/404/thumb/1585698662?1585712598" />
<strong style='display: block;'><a href="https://naotaka1128.hatenadiary.jp/entry/pandas-start-guide?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggleで戦いたい人のためのpandas実戦入門 - ML_BearのKaggleな日常</a> &mdash; <a href="https://naotaka1128.hatenadiary.jp/entry/pandas-start-guide">naotaka1128.hatenadiary.jp</a></strong>
元々pandasが苦手だった筆者が「これだけ知っていればKaggleでそこそこ戦えるかな」と思って集めたpandasの主要機能を紹介した記事です。Kaggleで戦いたい人も、仕事でデータ分析する人も、pandasに苦手意識がある人はぜひ一度読んでみてください。
</p>
<div style='clear: both;'></div>
<p><p>Kaggleのテーブルデータに取り組む際に必要不可欠なPandasの主要操作をまとめた記事。網羅性が高いので、一読して抜け漏れを確認する使い方もできそうです。</p></p>
<p>
<img width="140" height="140" alt="Semantic segmentation 振り返り - Speaker Deck" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/757/405/thumb/slide_0.jpg?1585712609" />
<strong style='display: block;'><a href="https://speakerdeck.com/motokimura/semantic-segmentation-zhen-rifan-ri?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Semantic segmentation 振り返り - Speaker Deck</a> &mdash; <a href="https://speakerdeck.com/motokimura/semantic-segmentation-zhen-rifan-ri">speakerdeck.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>CNNを用いたSemantic segmentationのまとめスライド。「Receptive Field（見る範囲）」と解像度の天秤を題材に、提唱されてきたモデルについて概説しています。</p></p>
<p>
<img width="140" height="140" alt="Release v1.3.0 · optuna/optuna · GitHub" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/762/884/thumb/57251745?1585809584" />
<strong style='display: block;'><a href="https://github.com/optuna/optuna/releases/tag/v1.3.0?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Release v1.3.0 · optuna/optuna · GitHub</a> &mdash; <a href="https://github.com/optuna/optuna/releases/tag/v1.3.0">github.com</a></strong>
A hyperparameter optimization framework. Contribute to optuna/optuna development by creating an account on GitHub.
</p>
<div style='clear: both;'></div>
<p><p>ハイパーパラメータ調整ツール「Optuna」のv1.3.0がリリース。ハイパーパラメータの重要度を見る機能など、Kaggleでも使えそうな更新がいくつかあります。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2003.12796?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2003.12796] Correlated daily time series and forecasting in the M4 competition</a></strong>

</p>
<p><p>「M4」コンペ参加者の論文で、解法を紹介。「We identify data leakage as one reason for its success」とあり、今後のコンペ設計に関する提唱もしています。</p></p>
