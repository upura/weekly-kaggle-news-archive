# Weekly Kaggle Issue #40
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-issue-40-277265
<h3><p><strong>News</strong></p><p>機械学習関連の著名な国際会議の発表動画が公開されています。「<a href="https://slideslive.com/icml-2020" target="_blank">ICML (International Conference on Machine Learning) 2020</a>」や「<a href="https://www.aclweb.org/anthology/events/acl-2020/" target="_blank">ACL (Annual Meeting of the Association for Computational Linguistics) 2020</a>」など、コロナ禍で急遽オンライン開催になった影響もありそうです。昨年の「<a href="https://www.youtube.com/playlist?list=PLaZufLfJumb900qqAAPvyN8f9Wd8-ZbLw" target="_blank">RecSys (ACM Recommender Systems conference) 2019</a>」も、このたび公開されました。</p><p><strong>Competitions</strong></p><p>Kaggle「<a href="https://www.kaggle.com/c/birdsong-recognition" target="_blank">Cornell Birdcall Identification</a>」コンペと「<a href="https://www.kaggle.com/c/halite" target="_blank">Halite by Two Sigma</a>」コンペが15日に終了しました。</p><p>前者は鳴き声から鳥の種類を推定する音声処理の課題でした。コンペ概要は<a href="https://www.ai-shift.co.jp/techblog/1271" target="_blank">参加者のブログ</a>に分かりやすく記載されており、銅メダル獲得者による<a href="https://teyoblog.hatenablog.com/entry/2020/09/17/234520" target="_blank">日本語ブログ</a>も公開されています。</p><p>後者はゲームAIを作成する新形式のコンペでした。現在は参加者が提出したエージェント同士が対戦中で、22日に最終結果が判明する予定です。必ずしも強化学習を利用する必要はなく、細かい条件分岐を駆使する参加者も多かった印象です。暫定順位1位の解法・コードは<a href="https://www.kaggle.com/c/halite/discussion/183543" target="_blank">discussion</a>で公開されました。日本からの参加チームが強化学習に取り組んだ内容も共有（<a href="https://threecourse.hatenablog.com/entry/2020/09/17/014155" target="_blank">記事1</a>, <a href="https://higepon.hatenablog.com/entry/2020/09/17/103918" target="_blank">2</a>）されています。</p><p>GUIツールを活用して音声データを分析する「<a href="https://nnc-challenge.com/" target="_blank">Neural Network Console Challenge</a>」が始まりました。Sonyが開発した「Neural Network Console」を用いて、GUI操作でモデルを実装できるとのことです。</p><h2>Datasets</h2><p>9日開始のKaggle「<a href="https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter" target="_blank">RSNA-STR Pulmonary Embolism Detection</a>」コンペの縮小版のデータセットが参加者有志により<a href="https://www.kaggle.com/c/rsna-str-pulmonary-embolism-detection/discussion/182930" target="_blank">公開</a>されました。256×256の大きさで、元の912.92GBから約52GBになっています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="PyTorch Metric Learning: What’s New | by Kevin Musgrave | Sep, 2020 | Medium" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/524/946/thumb/1*48EYCz9WC_ECK-05A7tgBA.png?1600400238" />
<strong style='display: block;'><a href="https://medium.com/@tkm45/pytorch-metric-learning-whats-new-15d6c71a644b?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">PyTorch Metric Learning: What’s New | by Kevin Musgrave | Sep, 2020 | Medium</a> &mdash; <a href="https://medium.com/@tkm45/pytorch-metric-learning-whats-new-15d6c71a644b">medium.com</a></strong>
Loss functions are now highly customizable with the introduction of distances, reducers, and regularizers. where “d” represents L2 distance. But what if we want to use a different distance metric…
</p>
<div style='clear: both;'></div>
<p><p>距離学習のライブラリ「<a href="https://github.com/KevinMusgrave/pytorch-metric-learning" target="_blank">PyTorch Metric Learning</a>」の直近のリリース内容についてのまとめ。新規導入された損失関数やアルゴリズムなどが紹介されています。</p></p>
<p>
<img width="140" height="140" alt="Talks # 11: Jean-François Puget; Did you know GPUs are not just for Deep Learning?" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/525/095/thumb/maxresdefault_live.jpg?1600405043" />
<strong style='display: block;'><a href="https://www.youtube.com/watch?feature=youtu.be&amp;utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter&amp;v=hUlvFtuFqy8">Talks # 11: Jean-François Puget; Did you know GPUs are not just for Deep Learning?</a> &mdash; <a href="https://www.youtube.com/watch?v=hUlvFtuFqy8&amp;feature=youtu.be">www.youtube.com</a></strong>
<p>Abstract: It is well known that GPU changed the way deep learning models are trained.</p>
</p>
<div style='clear: both;'></div>
<p><p>Kaggle Grandmasterの<a href="https://www.kaggle.com/cpmpml" target="_blank">CPMP</a>さんが日本時間の19日午前1時より「Did you know GPU are not just for Deep Learning?」の題目で講演します。ニューラルネットワーク以外の機械学習アルゴリズムでもGPUを活用する方法についてです。</p></p>
<p>
<img width="140" height="140" alt="ハイパーパラメーター最適化フレームワークOptunaの実装解説 | AI tech studio" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/519/850/thumb/median-stopping.jpg?1600306547" />
<strong style='display: block;'><a href="https://cyberagent.ai/optuna-from-scratch?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">ハイパーパラメーター最適化フレームワークOptunaの実装解説 | AI tech studio</a> &mdash; <a href="https://cyberagent.ai/optuna-from-scratch">cyberagent.ai</a></strong>
<p>本記事ではPythonのハイパーパラメーター最適化ライブラリとして有名な Optunaの内部実装についてソフトウェア的な側面を中心に解説します。</p>
</p>
<div style='clear: both;'></div>
<p><p>ハイパーパラメーター最適化ツール「Optuna」の実装を仕組みを丁寧に解説している記事。簡略化版の「<a href="https://github.com/c-bata/minituna" target="_blank">Minituna</a>」も公開されており、各モジュールの役割が分かりやすく示されています。</p></p>
<p>
<img width="140" height="140" alt="お手軽で欲しい機能が揃っている実験管理ツールGuild AIの紹介 - kuromt blog" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/497/936/thumb/20200910212807.png?1599867701" />
<strong style='display: block;'><a href="https://kuromt.hatenablog.com/entry/2020/09/11/230142?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">お手軽で欲しい機能が揃っている実験管理ツールGuild AIの紹介 - kuromt blog</a> &mdash; <a href="https://kuromt.hatenablog.com/entry/2020/09/11/230142">kuromt.hatenablog.com</a></strong>
<p>機械学習の実験管理ツールにGuild AIというものがあります。特に大きな特徴はコード追加なしで実験管理ができるというものです。</p>
</p>
<div style='clear: both;'></div>
<p><p>機械学習の実験管理ツール「Guild AI」の紹介記事。コード追加なしで簡単に試せる点が特徴的です。</p></p>
<p>
<img width="140" height="140" alt="Googleが開発した多言語の埋め込みモデル「LaBSE」を使って多言語のテキスト分類 - Ahogrammer" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/519/853/thumb/20200916145423.png?1600306575" />
<strong style='display: block;'><a href="https://hironsan.hatenablog.com/entry/text-classification-with-labse?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Googleが開発した多言語の埋め込みモデル「LaBSE」を使って多言語のテキスト分類 - Ahogrammer</a> &mdash; <a href="https://hironsan.hatenablog.com/entry/text-classification-with-labse">hironsan.hatenablog.com</a></strong>
<p>本記事では、Googleが開発した多言語の埋め込みモデル「LaBSE」を使って、テキスト分類をする方法を紹介します。</p>
</p>
<div style='clear: both;'></div>
<p><p>Googleが「<a href="https://arxiv.org/abs/2007.01852" target="_blank">Language-agnostic BERT Sentence Embedding</a>」いう論文で提案した多言語の埋め込みモデル「LaBSE」に関する記事。文章分類問題についての性能を検証しています。「<a href="https://hironsan.hatenablog.com/entry/text-classification-with-multilingual-universal-sentence-encoder" target="_blank">Universal Sentence Encoder</a>」と比較した追記記事も公開されました。</p></p>
<p>
<img width="140" height="140" alt="社内でAI人材を発掘するJR西日本、物体認識コンペ優勝の裏側 | Ledge.ai" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/525/152/thumb/aaa.jpg?1600406726" />
<strong style='display: block;'><a href="https://ledge.ai/jr-west-ai-edge-contest-champion/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">社内でAI人材を発掘するJR西日本、物体認識コンペ優勝の裏側 | Ledge.ai</a> &mdash; <a href="https://ledge.ai/jr-west-ai-edge-contest-champion/">ledge.ai</a></strong>
<p>4月27日から6月30日に開催されたデータサイエンスコンペティション「AIエッジコンテスト（外部サイト）」で、JR西日本の若手社員二人が優勝を勝ち取った。</p>
</p>
<div style='clear: both;'></div>
<p><p>6月に終了したSIGNATE「<a href="https://signate.jp/competitions/256" target="_blank">第3回AIエッジコンテスト（アルゴリズムコンテスト②）</a>」コンペで優勝したJR西日本の社員インタビュー。解法の概要だけでなく、過去のコンペ実績を評価され社内のデータ分析チームに異動した話も紹介されています。</p></p>
