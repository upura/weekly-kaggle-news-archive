# Weekly Kaggle News #9
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-9-225707
<h3><h2>News</h2><p>KaggleのNotebooks環境で<a href="https://www.kaggle.com/mgornergoogle/getting-started-with-100-flowers-on-tpu/" target="_blank">TPUが利用可能</a>になりました。チュートリアルとして「<a href="https://www.kaggle.com/c/flower-classification-with-tpus" target="_blank">Flower Classification with TPUs</a>」コンペが開催されています。TPUの概要は「<a href="https://speakerdeck.com/shimacos/pytorchdeshi-meruhazimetefalsetpu" target="_blank">Pytorchで始めるはじめてのTPU</a>」などに分かりやすくまとまっています。</p><p>Competitions、Kernels、Discussionの3カテゴリでGrandmasterだった<a href="https://kaggle.com/abhishek?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">Abhishekさん</a>が、2019年11月に追加されたDatasetsでも<a href="https://twitter.com/abhi1thakur/status/1227884188646416385?s=20" target="_blank">Grandmasterの称号を獲得</a>しました。AbhishekさんはDatasetsの称号が登場する以前にKaggle初のトリプルGrandmasterを達成していましたが、このたび初めて全カテゴリで称号を制覇したことになります。</p><h2>Competitions</h2><p>Kaggle「<a href="https://www.kaggle.com/c/google-quest-challenge" target="_blank">Google QUEST Q&amp;A Labeling</a>」コンペが、11日に終了しました。質問・回答のペアに対する30項目の評価値を予測する自然言語処理コンペでした。BERTやRoBERTaなどの言語モデルの活用、評価指標に応じた後処理の工夫が目立った印象です。個人で<a href="https://www.kaggle.com/c/google-quest-challenge/discussion/129927" target="_blank">3位に入賞したsakamiさん</a>ら、上位陣の取り組みがDiscussionに投稿されています。日本語のブログ記事も出ています（<a href="https://yukoishizaki.hatenablog.com/entry/2020/02/11/090908" target="_blank">記事1</a>、<a href="https://www.ai-shift.jp/techblog/635" target="_blank">記事2</a>、<a href="https://bluexleoxgreen.hatenablog.com/entry/2020/02/11/173831" target="_blank">記事3</a>、<a href="https://st1990.hatenablog.com/entry/2020/02/13/011629" target="_blank">記事4</a>、<a href="https://nmaviv.hatenablog.com/entry/2020/02/14/002317" target="_blank">記事5</a>）。</p><p>Kaggle「<a href="https://www.kaggle.com/c/abstraction-and-reasoning-challenge/" target="_blank">Abstraction and Reasoning Challenge</a>」コンペが14日に始まりました。推論タスクの入力・出力のペアから規則性を捉えるAIを作るコンペです。過去に例の無い形式で、どのような解法が導かれるかに注目が集まります。</p><p>Two Sigmaが運営するゲームAIプラットフォーム「<a href="https://halite.io/" target="_blank">Halite</a>」は、<a href="https://twitter.com/kaggle/status/1228004401312227328?s=20" target="_blank">新シーズンをKaggle上で開催</a>すると告知しました。Two Sigmaは過去に<a href="https://www.kaggle.com/c/two-sigma-financial-news" target="_blank">Kaggleコンペの開催経験</a>があり、「Halite」は過去3シーズンの実績があります。</p></h3>
<hr>
<p>
<strong style='display: block;'><a href="https://colab.research.google.com/signup?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Colab Pro</a></strong>

</p>
<p><p>Google Colaboratoryの月額$9.99の課金オプション。「良いGPUが割り当てられやすくなる」「実行可能時間が12-&gt;24h」「メモリ&amp;CPUも2倍まで設定可能」などの利点があります。現時点でUSAのみでの提供と記載されています。</p></p>
<p>
<img width="140" height="140" alt="nyaggle - Google Slides" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/529/252/thumb/uDuHG0cHfb5ZQIQSPHN8_YpRf9vTg7V5ZgiIf01btFY-OqgohsgYJRZIIBi_4XaGqnlNu-lK9A_w1200-h630-p?1581122180" />
<strong style='display: block;'><a href="https://docs.google.com/presentation/d/1jv3J7DISw8phZT4z9rqjM-azdrQ4L4wWJN5P-gKL6fA/edit?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">nyaggle - Google Slides</a> &mdash; <a href="https://docs.google.com/presentation/d/1jv3J7DISw8phZT4z9rqjM-azdrQ4L4wWJN5P-gKL6fA/edit">docs.google.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>コンペ支援ライブラリ「<a href="https://github.com/nyanp/nyaggle" target="_blank">nyaggle</a>」の紹介資料。ライブラリの設計思想が詳しく語られており参考になります。特徴量の保存、CVの評価、ログの書き出し、「MLflow」と連携した実験管理などをサポートしています。</p></p>
<p>
<img width="140" height="140" alt="ハイパラ管理のすすめ -ハイパーパラメータをHydra+MLflowで管理しよう- - やむやむもやむなし" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/531/881/thumb/20200209034558.png?1581236927" />
<strong style='display: block;'><a href="https://ymym3412.hatenablog.com/entry/2020/02/09/034644?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ハイパラ管理のすすめ -ハイパーパラメータをHydra+MLflowで管理しよう- - やむやむもやむなし</a> &mdash; <a href="https://ymym3412.hatenablog.com/entry/2020/02/09/034644">ymym3412.hatenablog.com</a></strong>
機械学習をやっている人なら誰もが遭遇したであろうこの光景 (※写真はPyTorchのLanguage ModelのExampleより) Pythonのargparseでシェルから引数を受け取りPythonスクリプト内でパラメータに設定するパターンは、記述が長くなりがちな上、どのパラメータがmodel/preprocess/optimizerのものなのか区別がつきにくく見通しが悪いといった課題があります。 私は実験用のパラメータ類は全てYAMLに記述して管理しています。 YAMLで記述することでパラメータを階層立てて構造的に記述することができ、パラメータの見通しがぐっとよくなります。 prepr…
</p>
<div style='clear: both;'></div>
<p><p>「Hydra」と「MLflow」を用いてパラメータ・実験を管理する方法の紹介。Livedoorのニュースコーパスのテキスト分類を題材にしています。</p></p>
<p>
<img width="140" height="140" alt="Fast AutoAugment - Speaker Deck" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/535/703/thumb/slide_0.jpg?1581316292" />
<strong style='display: block;'><a href="https://speakerdeck.com/inoichan/fast-autoaugment?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Fast AutoAugment - Speaker Deck</a> &mdash; <a href="https://speakerdeck.com/inoichan/fast-autoaugment">speakerdeck.com</a></strong>

</p>
<div style='clear: both;'></div>
<p><p>強化学習を用いてデータセットに適したデータ水増し方法を探索する「AutoAugment」を高速化した「Fast AutoAugment」を紹介。ベイズ最適化を組み合わせて、計算時間の大幅な短縮に成功しています。</p></p>
<p>
<img width="140" height="140" alt="グラフデータ分析 入門編" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/005/548/387/thumb/20200212graph-200212111050-thumbnail-4.jpg?1581560000" />
<strong style='display: block;'><a href="https://www.slideshare.net/ssuser0c8361/20200212-227754437?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">グラフデータ分析 入門編</a> &mdash; <a href="https://www.slideshare.net/ssuser0c8361/20200212-227754437">www.slideshare.net</a></strong>
グラフ分析ナイト (エンジニア向け) https://dllab.connpass.com/event/159148/ グラフ畳み込みネットワークなど、グラフ上の機械学習/深層学習技術の概要についてご説明します。
</p>
<div style='clear: both;'></div>
<p><p>グラフのデータ分析に関する概説。グラフの表現学習、グラフ畳み込みニューラルネットワークや、近年の学会での傾向などをまとめています。&nbsp;</p><p><br></p></p>
