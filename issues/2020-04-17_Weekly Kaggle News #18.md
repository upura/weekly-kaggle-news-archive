# Weekly Kaggle News #18
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-18-239563
<h3><h2>News</h2><p>4月9日に開催されたNVIDIAのセッション「Winning Kaggle Competitions with GPUs: Reflections from Kaggle Grandmasters」の<a href="https://developer.nvidia.com/gtc/2020/video/cwe22495" target="_blank">動画</a>が公開されています。同社に所属する10人のGrandmaster（うち3部門Grandmasterが1人、2部門Grandmasterが5人）が寄せられた質問に答える形式で、多くの知見が詰まっています。</p><p><strong>※初出時、NVIDIAの会社名に誤りがありました。お詫びして訂正します。</strong></p><p>KaggleのNotebooks環境を支えるバックエンドチームの取り組みが16日に<a href="https://medium.com/google-cloud/a-multi-cluster-grpc-architecture-on-gke-365bbd757df" target="_blank">公開</a>されました。GCPプロジェクトで複数regionに負荷分散する仕組みを設計しているとのことです。2020年2月ごろの改修で、Notebooks環境はかなり快適になった印象があります。</p><h2>Competitions</h2><p>3月23日に開始した2つのNLPコンペを最後に、Kaggleではメダルが付与されるコンペは始まっていません。憶測の域を出ませんが、新型コロナウイルスの影響を受けてコンペ開催に必要なスポンサーが集まりにくくなっているのかもしれません。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Data Processing For Question &amp; Answering Systems: BERT vs. RoBERTa" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/829/745/thumb/maxresdefault.jpg?1587019270" />
<strong style='display: block;'><a href="https://www.youtube.com/watch?feature=youtu.be&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter&amp;v=6a6L_9USZxg">Data Processing For Question &amp; Answering Systems: BERT vs. RoBERTa</a> &mdash; <a href="https://www.youtube.com/watch?v=6a6L_9USZxg&amp;feature=youtu.be">www.youtube.com</a></strong>
In this video I explain how to process data for question and answering systems. I start with BERT and show how one can easily transfer it to other transforme...
</p>
<div style='clear: both;'></div>
<p><p>「BERT」を用いて質問応答モデルを構築するためのデータ前処理についての解説動画。「RoBERTa」などに切り替える方法についても紹介しています。</p></p>
<p>
<img width="140" height="140" alt="Deep Learning精度向上テクニック：様々な最適化手法 #1" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/813/881/thumb/maxresdefault.jpg?1586759844" />
<strong style='display: block;'><a href="https://www.youtube.com/watch?feature=youtu.be&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter&amp;v=q933reMpvX8">Deep Learning精度向上テクニック：様々な最適化手法 #1</a> &mdash; <a href="https://www.youtube.com/watch?v=q933reMpvX8&amp;feature=youtu.be">www.youtube.com</a></strong>
Deep Learning精度向上テクニック：様々な最適化手法 #1 この動画では、Deep Learningを学習する際のパラメータの更新に用いるソルバ、ミニバッチ勾配降下法、Stochastic Gradient Descentと、その改良手法としてMomentum SGD、Nesterov Accelera...
</p>
<div style='clear: both;'></div>
<p><p>Deep Learning学習時のパラメータの更新に用いる最適化手法について解説した動画。ミニバッチ勾配降下法、Stochastic Gradient Descent、Momentum SGD、Nesterov Accelerated Gradient、RMSprop、Adamを紹介しています。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2004.04938?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2004.04938] Identifying Cultural Differences through Multi-Lingual Wikipedia</a></strong>

</p>
<p><p>wikipediaから文化の違いを捉えようとする試みで、wikipediaにある文を正例、反対の意の文を負例にしてBERTをfine-tuning。単純に正例の文の単語を変換するだけでは文章が似すぎてしまうため、それぞれEN→DE→ENと翻訳しています。Kaggleの自然言語処理コンペでも頻出の翻訳・再翻訳によるデータセット水増しテクニックです。</p></p>
<p>
<img width="140" height="140" alt="What to do when you didn’t get any medal in a Kaggle competition?" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/829/536/thumb/1*z-uXGSiGZlI5d-sOF5pKdg.png?1587016157" />
<strong style='display: block;'><a href="https://towardsdatascience.com/what-to-do-when-you-dont-get-any-medal-in-a-kaggle-competition-b54cc433da3?gi=458782e3d00e&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">What to do when you didn’t get any medal in a Kaggle competition?</a> &mdash; <a href="https://towardsdatascience.com/what-to-do-when-you-dont-get-any-medal-in-a-kaggle-competition-b54cc433da3?gi=458782e3d00e">towardsdatascience.com</a></strong>
Several weeks ago one more Kaggle Competition has ended — Bengali.AI Handwritten Grapheme Classification. Bengali is the 5th most spoken language in the world. This challenge hoped to improve on…
</p>
<div style='clear: both;'></div>
<p><p>Notebooksランク1位の<a href="https://www.kaggle.com/artgor" target="_blank">Andrew Lukyanenkoさん</a>によるKaggle「<a href="https://www.kaggle.com/c/bengaliai-cv19" target="_blank">Bengaliコンペ</a>」の振り返り。実行環境・GPU・Pipelineなどの観点で知見をまとめています。</p></p>
<p>
<img width="140" height="140" alt="Identifying Leakage in Computer Vision on Medical Images" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/829/560/thumb/Identifying_20Leakage_20in_20Computer_20Vision_20on_20Medical_20Images_20for_20COVID-19_ResourceCard-01.png?1587017629" />
<strong style='display: block;'><a href="https://blog.datarobot.com/identifying-leakage-in-computer-vision-on-medical-images?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Identifying Leakage in Computer Vision on Medical Images</a> &mdash; <a href="https://blog.datarobot.com/identifying-leakage-in-computer-vision-on-medical-images">blog.datarobot.com</a></strong>
In this post we explain why target leakage issues occurred within image datasets used for COVID-19 research, using interpretability tools to detect them.
</p>
<div style='clear: both;'></div>
<p><p>COVID-19の画像データセットが含有する "Leakage" を議論しているDataRobotのブログ。分類器が見ている箇所を可視化しながら、正例・負例の画像撮影状況に由来する特徴が判別に使われている点を指摘しています。</p></p>
