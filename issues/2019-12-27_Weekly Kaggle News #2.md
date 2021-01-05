# Weekly Kaggle News #2
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-2-217200
<h3><h2>News</h2><p>株式会社Ristは、業務時間の一部を使いコンペに挑むKaggleチームを立ち上げました。24日には、<a href="https://prtimes.jp/main/html/rd/p/000000025.000023649.html" target="_blank">Kaggle Grandmasterの小野寺和樹氏がアドバイザーに就任</a>すると発表。年収1000万円〜1200万円の待遇で初期メンバーを募集しているとのことです。日本企業としては「<a href="https://dena.ai/kaggle/" target="_blank">Kaggle社内ランク制度</a>」を設けている株式会社ディー・エヌ・エーに次ぐ大きな事例になりそうです。</p><h2>Competitions</h2><p>20日に終了したKaggle「<a href="https://www.kaggle.com/c/ashrae-energy-prediction" target="_blank">ASHRAE - Great Energy Predictor III</a>」は、アメリカ太平洋標準時の26日午後（日本時間27日17時）までにPrivate LBが<a href="https://www.kaggle.com/c/ashrae-energy-prediction/discussion/122987" target="_blank">発表される予定</a>でしたが、現時点で公開されていません。エネルギー消費量を予測する時系列コンペで、shake upも予想されています。</p><p>ProbSpace「<a href="https://prob.space/competitions/salary-prediction" target="_blank">給与推定</a>」は23日に終了しました。綺麗なテーブルデータを用いた回帰問題で、Neural Networkが活躍したコンペでした。上位陣の取り組みは「<a href="https://upura.hatenablog.com/entry/2019/12/23/190300" target="_blank">ProbSpace給与推定コンペまとめ</a>」にまとめられています。</p><p>Kaggle「<a href="https://www.kaggle.com/c/bengaliai-cv19" target="_blank">Bengali.AI Handwritten Grapheme Classification</a>」が20日に始まりました。ベンガル語文字の手書き画像を分類するコンペです。同日には、SIGNATE「<a href="https://signate.jp/competitions/218" target="_blank">国立国会図書館の画像データレイアウト認識</a>」も開始。年末年始に取り組めるコンペの選択肢が増えてきました。</p><p>来年3月には、Walmartの売上データを用いた時系列予測コンペがKaggleで<a href="https://twitter.com/spyrosmakrid/status/1209153609432211457?s=20" target="_blank">開催予定</a>です。予測値だけではなく予測分布も提出する形式だと予告されています。</p></h3>
<hr>
<h2>Articles</h2>
<p>
<strong style='display: block;'><a href="https://qiita.com/khigashi02/items/b4b95714cae9e3f2a7be?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">生物学データの次元削減・可視化手法PHATEを使ってみる - Qiita</a></strong>

</p>
<p><p>PHATE (Potential of Heat diffusion for Affinity-based Transition Embedding) という次元削減手法を解説。Pythonの場合は <strong>pip install phate</strong> で簡単にインストールできます。</p></p>
<p>
<strong style='display: block;'><a href="https://qiita.com/hiromu166/items/507fc0fb466c7149dccf?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">高速でKaggle用のGCP環境を手軽に構築 - Qiita</a></strong>

</p>
<p><p>GCPの「AIプラットフォーム」機能を解説。手軽にJupyterLabの実行環境を構築できます。</p></p>
<p>
<strong style='display: block;'><a href="https://qiita.com/shinochin/items/8b6b7e76bf426ab86444?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">NLPerのための&amp;quot;CUDA out of memory&amp;quot;回避術 - Qiita</a></strong>

</p>
<p><p>GPUを用いて自然言語処理に取り組む際に直面する「CUDA out of memory」を回避するためのTipsをまとめた記事。「Embedding layerはCPUに載せる」など、いくつかのアイディアが列挙されています。</p></p>
<p>
<img width="140" height="140" alt="実務で使えるニューラルネットワークの最適化手法 - Taste of Tech Topics" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/371/689/thumb/20191224011352.png?1577417521" />
<strong style='display: block;'><a href="http://acro-engineer.hatenablog.com/entry/2019/12/25/130000?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">実務で使えるニューラルネットワークの最適化手法 - Taste of Tech Topics</a> &mdash; <a href="http://acro-engineer.hatenablog.com/entry/2019/12/25/130000">acro-engineer.hatenablog.com</a></strong>
メリークリスマス。 @tereka114です。本記事はDeep Learning論文紹介 Advent Calendar 2019の25日です。 qiita.com私はKaggleの画像コンペに頻繁に参加しています。 そのときに、毎度選定にこまるのがニューラルネットワークの最適化手法（Optimizer）です。 学習率やWeight Decayなどハイパーパラメータが多く、選択パタンが無数にあると感じています。そのため、Kaggleでよく利用される（されうる）最適化手法を振り返ります。 もちろん、実務でも十分使えるので、皆さんの学習に活かしてくれると幸いです。 最適化手法 SGD（Moment…
</p>
<div style='clear: both;'></div>
<p><p>Neural NetworkのOptimizerとして、SGD、Adam、AdamW、Adabound、RAdamを紹介。精度・収束速度・安定性の観点で比較し、CIFAR10を用いた実験結果も掲載しています。</p></p>
