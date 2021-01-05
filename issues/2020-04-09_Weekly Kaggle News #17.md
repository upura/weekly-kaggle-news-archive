# Weekly Kaggle News #17
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-17-237965
<h3><h2>News</h2><p>「<a href="https://nlp100.github.io/ja/" target="_blank">言語処理100本ノック 2020</a>」が4月6日に公開されました。<a href="https://nlp100.github.io/ja/about.html" target="_blank">5年ぶりの改訂</a>で、深層ニューラルネットワークに関する問題が追加されるなど、時代に即した内容が盛り込まれた印象です。</p><p>ハイパーパラメータ調整ツール「Optuna」が<a href="https://twitter.com/PreferredNet/status/1247715380145111048?s=20" target="_blank">「PyTorch」のエコシステム</a>に正式に加わりました。4月6日に東大で開かれた講義では、Preferred Networksの開発者が<a href="https://www.slideshare.net/pfi/optuna" target="_blank">概要や今後の展望などを語りました</a>。</p><p>KaggleのNotebookの実行画面のUI/UXが4月初旬に変更されました。ソースコードを実行せずにNotebookを保存できるようになり、利便性が向上したと感じます。新UI/UXでの操作方法は、書籍『<a href="https://github.com/upura/python-kaggle-start-book" target="_blank">PythonではじめるKaggleスタートブック</a>』の<a href="https://youtu.be/2kMzUfajj1U" target="_blank">サポート動画</a>として公開しています。</p><h2>Competitions</h2><p>英語の文中から感情を表す部分を抽出するKaggle「<a href="https://www.kaggle.com/c/tweet-sentiment-extraction?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">Tweet Sentiment Extraction</a>」コンペについて、提出を一時中断しデータセットを更新すると10日に<a href="https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/142291" target="_blank">発表</a>されました。終了日は2週間延長されます。コンペ開催当初から、データセットの乱雑さが議論されていました。</p><p>3月23日に開始した2つのNLPコンペを最後に、Kaggleではメダルが付与されるコンペは始まっていません。新型コロナウイルスの流行を予測する「COVID19 Global Forecasting」コンペは毎週開催されており、9日には「<a href="https://www.kaggle.com/c/covid19-global-forecasting-week-4" target="_blank">Week 4</a>」が開始しました。以前よりKaggle上での開催が予告されていたゲームAIを作成する「<a href="https://www.kaggle.com/c/halite/rules" target="_blank">Halite by Two Sigma</a>」コンペも、8日に始まっています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Confident Learningは誤った教師から学習するか？ ~ tf-idfのデータセットでノイズ生成から評価まで ~ - 学習する天然ニューラルネット" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/777/200/thumb/20200404120350.png?1586031695" />
<strong style='display: block;'><a href="https://aotamasaki.hatenablog.com/entry/reuter_with_confident_learning?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Confident Learningは誤った教師から学習するか？ ~ tf-idfのデータセットでノイズ生成から評価まで ~ - 学習する天然ニューラルネット</a> &mdash; <a href="https://aotamasaki.hatenablog.com/entry/reuter_with_confident_learning">aotamasaki.hatenablog.com</a></strong>
概要 現実の判別問題において教師が完璧であることは珍しい。ラベリング作業において、知識不足や勘違いなどで引き起こされるヒューマンエラーはデータセットを汚染する。 このような間違った教師のことを、noisy label (corrupted label や polluted labelとも)という。誤った教師を用いると学習はうまく行かず判別性能は下がってしまう。近年ではこれに対処しようという研究が増えている。 ICML2020に Confident Learning: Estimating Uncertainty in Dataset Labels という論文が投稿された。しかも、よく整備された…
</p>
<div style='clear: both;'></div>
<p><p>データセット内の誤ったラベルの検知を試みる「Confident Learning (CL)」の実際に使って考察した記事。CLで検知したデータに代わりの擬似ラベルを付与するなど、Kaggleでも活用できそうなアプローチを試しています。</p></p>
<p>
<img width="140" height="140" alt="kaggleで強化学習をやってみた - 機械学習 Memo φ(・ω・ )" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/780/419/thumb/20200401191514.png?1586121825" />
<strong style='display: block;'><a href="https://yukoishizaki.hatenablog.com/entry/2020/04/05/202935?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">kaggleで強化学習をやってみた - 機械学習 Memo φ(・ω・ )</a> &mdash; <a href="https://yukoishizaki.hatenablog.com/entry/2020/04/05/202935">yukoishizaki.hatenablog.com</a></strong>
概要 現在、kaggle に Connect X という強化学習の Getting Started コンペ があります。このコンペを通じて強化学習を少し勉強したので、その内容を記載したいと思います。こちらの書籍をもとに強化学習について理解したことと、Connect Xコンペでの実装を解説した記事になります。間違いがあれば、コメントいただけたら嬉しいです。bookclub.kodansha.co.jp 強化学習とは 強化学習とは、行動から報酬が得られる環境において、各状況で報酬に繋がるような行動を出力するように、モデルを作成すること。教師あり学習との違いは連続した行動によって得られる報酬を最大化…
</p>
<div style='clear: both;'></div>
<p><p>Kaggleで開催中の強化学習コンペ「<a href="https://www.kaggle.com/c/connectx" target="_blank">Connect X</a>」の実装を解説した体験記。書籍『<a href="https://bookclub.kodansha.co.jp/product?item=0000324909" target="_blank">Pythonで学ぶ強化学習</a>』を用いて強化学習の概要も紹介しています。</p></p>
<p>
<img width="140" height="140" alt="SIGANTE Quest | 実践形式で学ぶ100%オンライン形式のAI・データサイエンス講座" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/786/796/thumb/for-sns-img.png?1586229324" />
<strong style='display: block;'><a href="https://quest.signate.jp/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">SIGANTE Quest | 実践形式で学ぶ100%オンライン形式のAI・データサイエンス講座</a> &mdash; <a href="https://quest.signate.jp/">quest.signate.jp</a></strong>
SIGNATE Quest は、国内最大のAI人材コミュティ、AI開発コンペティションを運営するSIGNATEが提供する、実践形式で学ぶ100%オンライン形式のAI・データサイエンス講座です。実データ・実課題へ取り組み、実践的なスキルを身につけることができます。
</p>
<div style='clear: both;'></div>
<p><p>SIGNATEがデータサイエンス講座「SIGNATE Quest」をリリース。動画・スライドで学び、コードを書く演習問題に挑戦する構成。月額1980円で、無料で途中まで受けられる講座「<a href="https://quest.signate.jp/quests/10001/" target="_blank">自動車環境性能の改善</a>」もあります。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2004.02621?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2004.02621] Managing Diversity in Airbnb Search</a></strong>

</p>
<p><p>Airbnbから出た論文。関連度順に出すと似たような物件ばかりが上位に来がちな問題があり、価格・場所・人数・タイプなどの多様性が損なわれる問題に対して、関連度と多様性の両者を考慮できるロス関数を提唱。設計の中では表示するK個の順番も考慮しており、課題をロス関数に落とし込む考え方が参考になりました。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2004.03045?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2004.03045] Adversarial Validation Approach to Concept Drift Problem in Automated Machine Learning Systems</a></strong>

</p>
<p><p>Uberから出た論文。trainとtestの性質が異なってしまう機械学習のよくある課題に対して、Kaggleで頻出な「Adversarial Validation」を使って対応しています。</p></p>
<p>
<img width="140" height="140" alt="Graph Neural Networksを完全に理解したい - Speaker Deck" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/800/244/thumb/slide_0.jpg?1586461006" />
<strong style='display: block;'><a href="https://speakerdeck.com/shimacos/graph-neural-networkswowan-quan-nili-jie-sitai?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Graph Neural Networksを完全に理解したい - Speaker Deck</a> &mdash; <a href="https://speakerdeck.com/shimacos/graph-neural-networkswowan-quan-nili-jie-sitai">speakerdeck.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>近年のKaggleで時おり解法に登場するGNNの解説。「Deep Graph Library」を用いた具体的な実装方法も紹介しています。</p></p>
