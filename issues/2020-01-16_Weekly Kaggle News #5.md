# Weekly Kaggle News #5
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-5-220196
<h3><h2>News</h2><p>2019年4月に終了したKaggle「<a href="https://www.kaggle.com/c/petfinder-adoption-prediction" target="_blank">PetFinder.my Adoption Prediction</a>」コンペに関して10日、<a href="https://www.kaggle.com/c/petfinder-adoption-prediction/discussion/125436" target="_blank">不正発覚に伴い1位チームを失格にする</a>と公表されました。問題の背景や発覚の経緯などは<a href="https://medium.com/@u39kun/how-a-top-kaggle-grandmaster-cheated-and-got-permanently-banned-c86ca431f499" target="_blank">こちら</a>のブログ記事にまとまっています。</p><p>ハイパーパラメータ最適化ツール「Optuna」の<a href="https://medium.com/optuna/optuna-v1-86192cd09be5" target="_blank">v1.0.0が公開</a>されました。最近はKaggleで頻繁に用いられる「LightGBM」との連携も進み、ますます使いやすくなっている印象です。</p><p>テーブルデータに取り組む際に必須の「Pandas」は、<a href="https://mail.python.org/pipermail/pandas-dev/2020-January/001173.html" target="_blank">1.0.0rc版が公開</a>されました。整数での欠損値を示す型の追加、apply時の処理が高速になるNumbaの利用など、いくつかの更新があります。<a href="https://qiita.com/simonritchie/items/e28c52211890fef33810" target="_blank">日本語の解説記事</a>も出ています。</p><h2>Competitions</h2><p>ProbSpace「<a href="https://prob.space/competitions/ukiyoe-author" target="_blank">浮世絵作者予測</a>」コンペが13日に終了しました。画像コンペとしては、事前学習済モデルの使用が禁止されていた点が特徴的でした。<a href="https://prob.space/competitions/ukiyoe-author/discussions/ak1100-Post2b7eadf75b776093298a" target="_blank">1位解法</a>は既に公開されており、不正などがないか参加者によるレビュー期間が設けられています。</p><p>数理最適化問題を解くKaggle「<a href="https://www.kaggle.com/c/santa-workshop-tour-2019" target="_blank">Santa's Workshop Tour 2019</a>」が16日に終了し、1〜46位が最適解を出す結果となりました。この通称「サンタコンペ」の雰囲気を知るには、<a href="https://twitter.com/ultraistter/status/1217610620452790272?s=20" target="_blank">45位の方のtweet</a>や<a href="https://youtu.be/bM1Xtziy6xc" target="_blank">過去のKaggle Meetup Tokyoでの発表</a>を見ると良いかもしれません。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Hugging Face Introduces Tokenizers - dair.ai - Medium" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/425/801/thumb/1*Oqvvb3NYJaLDfJGYwFYzEg.jpeg?1578975598" />
<strong style='display: block;'><a href="https://medium.com/dair-ai/hugging-face-introduces-tokenizers-d792482db360?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Hugging Face Introduces Tokenizers - dair.ai - Medium</a> &mdash; <a href="https://medium.com/dair-ai/hugging-face-introduces-tokenizers-d792482db360">medium.com</a></strong>
Last year was huge for natural language processing (NLP). As far as improvements go, faster implementation of neural networks is now possible with the use of optimized libraries and high-performing…
</p>
<div style='clear: both;'></div>
<p><p>NLPモデルを扱うライブラリ「<a href="https://github.com/huggingface/transformers" target="_blank">Transformers</a>」で有名なHugging Face社が、文章をトークン化するためのライブラリ「Tokenizers」を公開。Transformersと合わせて、BERTをはじめとしたNLPモデルが使いやすくなりそうです。</p></p>
<p>
<img width="140" height="140" alt="Kaggler TV on Twitter: &quot;First episode of Kaggler TV on #YouTube, &quot;Introduction to Machine Learning Competitions&quot; will be uploaded to https://t.co/wIEvVb4th7 at 10am on Saturday, 1/19/2020 Pacific Time.&quot;" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/425/802/thumb/qVsRBG-w_400x400.png?1578975635" />
<strong style='display: block;'><a href="https://twitter.com/KagglerTV/status/1216903450757230592?s=20&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggler TV on Twitter: &quot;First episode of Kaggler TV on #YouTube, &quot;Introduction to Machine Learning Competitions&quot; will be uploaded to https://t.co/wIEvVb4th7 at 10am on Saturday, 1/19/2020 Pacific Time.&quot;</a> &mdash; <a href="https://twitter.com/KagglerTV/status/1216903450757230592?s=20">twitter.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>「Kaggler TV」と題したYouTubeチャンネルが開設されました。1月19日（PST）に最初の動画が投稿されると予告しています。</p></p>
<p>
<img width="140" height="140" alt="How Much Position Information Do Convolutional Neural Networks Encode?" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/425/804/thumb/20200110howmuchpositioninformationdoconvolutionalneuralnetworksencode-200112025125-thumbnail-4.jpg?1578975743" />
<strong style='display: block;'><a href="https://www.slideshare.net/KazuyukiMiyazawa/how-much-position-information-do-convolutional-neural-networks-encode?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">How Much Position Information Do Convolutional Neural Networks Encode?</a> &mdash; <a href="https://www.slideshare.net/KazuyukiMiyazawa/how-much-position-information-do-convolutional-neural-networks-encode">www.slideshare.net</a></strong>
Md Amirul, Sen Jia, and Neil D. B. Bruce, "How Much Position Information Do Convolutional Neural Networks Encode?," ICLR2020.
</p>
<div style='clear: both;'></div>
<p><p>CNNが画像の位置情報を学習しているという仮説を検証した論文のまとめスライド。実験を通じて、CNNが位置情報を学習するために必要な要素などを指摘しています。</p></p>
<p>
<strong style='display: block;'><a href="https://www.kaggle.com/terms?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Terms of Use | Kaggle</a></strong>
Download Open Datasets on 1000s of Projects + Share Projects on One Platform. Explore Popular Topics Like Government, Sports, Medicine, Fintech, Food, More. Flexible Data Ingestion.
</p>
<p><p>Kaggleの利用規約（Terms of Use）ページ。「Simulations Competitions」と呼ばれる新形式の<a href="https://www.kaggle.com/c/connectx" target="_blank">コンペ</a>の設立を受けて2019年12月に更新されています。</p></p>
<p>
<strong style='display: block;'><a href="https://qiita.com/omiita/items/90abe0799cf3efe8d93d?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">パラメータ数10億！最新の巨大画像認識モデル「BiT」爆誕 &amp;amp; 解説 - Qiita</a></strong>

</p>
<p><p>昨年末にGoogle Brainが発表した新たな画像認識モデル「BiT」の解説。パラメータ数が10億におよぶ巨大なモデルで、これまでの画像認識モデルが標準的に使っていた技術を使わずにSoTAを達成しているとのことです。</p></p>
