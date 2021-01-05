# Weekly Kaggle News #8
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-8-224267
<h3><h2>News</h2><p>2020年中の「<a href="https://kaggledays.com/china2020en/" target="_blank">Kaggle Days China</a>」の開催が告知されました。開催日や開催地は現時点で未定です。中国での開催は2019年10月に次いで2回目で、<a href="https://kaggledays.com/china/" target="_blank">前回</a>はKaggle Grandmasterらによるプレゼンテーションや、<a href="https://japan.zdnet.com/article/35145947/" target="_blank">オフラインコンペ</a>が実施されました。</p><p>PyTorchライブラリ「Transformers」の<a href="https://github.com/huggingface/transformers/releases" target="_blank">v2.4.0</a>が1日にリリースされ、テキストだけでなく画像も扱えるマルチモーダルなモデル「<a href="https://github.com/facebookresearch/mmbt/" target="_blank">MultiModal BiTransformers (MMBT)</a>」が利用可能になりました。ハイパーパラメータ調整ライブラリ「Optuna」の<a href="https://github.com/optuna/optuna/releases/tag/v1.1.0" target="_blank">v1.1.0</a>は6日にリリースされ、逐次的に優良な値を探索する「LightGBM Tuner」機能の実装例が盛り込まれるなどの更新がありました。</p><h2>Competitions</h2><p>富士フイルムの研究開発機関「FUJIFILM AI Academy」が主催した「<a href="http://fujifilmdatasciencechallnge.mystrikingly.com/" target="_blank">アナログ写真の撮影年推定</a>」コンペの表彰式が3日に開催されました。コンペの概要や解法に関する参加者のブログ記事も公開されています（<a href="https://sh1r09.hatenablog.com/entry/2020/02/04/003136" target="_blank">記事1</a>、<a href="https://hrhr08hrhr.hatenablog.com/entry/2020/02/05/010219" target="_blank">記事2</a>、<a href="https://www.inoichan.com/entry/fujifilm3rd-competition" target="_blank">記事3</a>）。</p><p>1月25日に開催されたオフラインコンペ「<a href="https://atma.connpass.com/event/161251/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">CA × atmaCup</a>」の振り返り記事が、データセットを提供した<a href="https://developers.cyberagent.co.jp/blog/archives/24684/" target="_blank">サイバーエージェントAI事業本部のブログ</a>に掲載されました。運営目線でのイベントの考察が記されています。</p><p>国文学研究資料館発行の「ふみ」第13号（2020年1月）の特集「<a href="https://www.nijl.ac.jp/pages/cijproject/images/fumi_13.pdf" target="_blank">AIがくずし字を読む時代がやってきた</a>」では、データセットの公開やKaggleでの「<a href="https://www.kaggle.com/c/kuzushiji-recognition" target="_blank">Kuzushiji Recognition</a>」コンペの開催など、くずし字プロジェクトの経緯が紹介されています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="Introducing PyTorch3D: An open-source library for 3D deep learning" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/523/654/thumb/85247966_186385585753674_7571124583672053760_n.jpg?1581042171" />
<strong style='display: block;'><a href="https://ai.facebook.com/blog/-introducing-pytorch3d-an-open-source-library-for-3d-deep-learning/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Introducing PyTorch3D: An open-source library for 3D deep learning</a> &mdash; <a href="https://ai.facebook.com/blog/-introducing-pytorch3d-an-open-source-library-for-3d-deep-learning/">ai.facebook.com</a></strong>
We just released PyTorch3D, a new toolkit for researchers and engineers that’s fast and modular for 3D deep learning research.
</p>
<div style='clear: both;'></div>
<p><p>Facebook AIが6日に、3次元モデルを扱うためのPyTorchライブラリ「PyTorch3D」を公開。短編動画でライブラリの特徴が簡潔に紹介されています。</p></p>
<p>
<img width="140" height="140" alt="LightGBM with the Focal Loss for imbalanced datasets" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/515/125/thumb/1*nz3rZGJxF2df77-BTzKTTA_2x.png?1580853681" />
<strong style='display: block;'><a href="https://towardsdatascience.com/lightgbm-with-the-focal-loss-for-imbalanced-datasets-9836a9ae00ca?gi=7b8fb1af1f08&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">LightGBM with the Focal Loss for imbalanced datasets</a> &mdash; <a href="https://towardsdatascience.com/lightgbm-with-the-focal-loss-for-imbalanced-datasets-9836a9ae00ca?gi=7b8fb1af1f08">towardsdatascience.com</a></strong>
The Focal loss (hereafter FL) was introduced by Tsung-Yi Lin et al., in their 2018 paper “Focal Loss for Dense Object Detection”[1]. It is designed to address scenarios with extreme imbalanced…
</p>
<div style='clear: both;'></div>
<p><p>不均衡データに対応するためにLightGBMでFocal Lossを使う方法を解説。題材としてKaggle「<a href="https://www.kaggle.com/mlg-ulb/creditcardfraud" target="_blank">Credit Card Fraud Detection</a>」データセットを利用しています。</p></p>
<p>
<img width="140" height="140" alt="keras tunerでtf.kerasのハイパーパラメータを探索する - メモ帳" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/503/419/thumb/1580521455?1580610196" />
<strong style='display: block;'><a href="https://tksmml.hatenablog.com/entry/2020/02/01/093000?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">keras tunerでtf.kerasのハイパーパラメータを探索する - メモ帳</a> &mdash; <a href="https://tksmml.hatenablog.com/entry/2020/02/01/093000">tksmml.hatenablog.com</a></strong>
keras tuner 2019年10月末にメジャーリリースされたkeras tunerを試してみたいと思います。 github.com できること 機械学習モデルのハイパーパラメータの探索 対応フレームワーク・ライブラリ tensorflow sckit-learn 使用可能な探索アルゴリズム ランダムサーチ Bayesian optimization hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization. (2018) 参考: Hyper-parameter optimization algorith…
</p>
<div style='clear: both;'></div>
<p><p>kerasのハイパーパラメータを探索できる「<a href="https://github.com/keras-team/keras-tuner" target="_blank">keras-tuner</a>」を紹介。kerasを利用する際には、連携面で他のライブラリと比べた優位性がありそうです。</p></p>
<p>
<strong style='display: block;'><a href="https://qiita.com/Minyus86/items/70622a1502b92ac6b29c?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">PythonのPipelineパッケージ比較：Airflow, Luigi, Gokart, Metaflow, Kedro, PipelineX - Qiita</a></strong>

</p>
<p><p>PythonのPipelineライブラリを比較した記事。「Apache Airflow」「Luigi」「gokart」「Metaflow」「Kedro」「PipelineX」を扱っています。発表4件中3件が「gokart」を題材にしていた「<a href="https://m3-engineer.connpass.com/event/159721/" target="_blank">MLOps勉強会</a>」の資料もライブラリの実運用の観点で参考になります。</p></p>
<p>
<strong style='display: block;'><a href="https://arxiv.org/abs/2002.00838?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">[2002.00838] Improving Generalizability of Fake News Detection Methods using Propensity Score Matching</a></strong>
<p><br></p>
</p>
<p><p>傾向スコアの考え方を利用した特徴選択手法を提案。<a href="https://github.com/Arstanley/fakenews_pscore_match" target="_blank">GitHub</a>でソースコードも公開されています。</p></p>
<p>
<img width="140" height="140" alt="WikiResearch on Twitter: &quot;&quot;Wikipedia2Vec: An Efficient Toolkit for Learning and Visualizing the Embeddings of Words and Entities from Wikipedia&quot; Python-based open tool for learning word and entity embeddings from #Wikipedia, now with a web demo. demo: https://t.co/Gv5EBXWbuX paper: https://t.co/GGbQjQolJe… https://t.co/cUMp0kUqLs&quot;" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/523/637/thumb/EQAvt5pWsAgSWKv.jpg_large?1581041801" />
<strong style='display: block;'><a href="https://twitter.com/WikiResearch/status/1225031571864018946?s=20&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">WikiResearch on Twitter: &quot;&quot;Wikipedia2Vec: An Efficient Toolkit for Learning and Visualizing the Embeddings of Words and Entities from Wikipedia&quot; Python-based open tool for learning word and entity embeddings from #Wikipedia, now with a web demo. demo: https://t.co/Gv5EBXWbuX paper: https://t.co/GGbQjQolJe… https://t.co/cUMp0kUqLs&quot;</a> &mdash; <a href="https://twitter.com/WikiResearch/status/1225031571864018946?s=20">twitter.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>wikipediaの情報で単語埋め込みした「Wikipedia2Vec」のデモ。日本語版もあり、類似単語などの検索を体験できます。</p></p>
