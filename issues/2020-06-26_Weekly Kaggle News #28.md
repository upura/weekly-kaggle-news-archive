# Weekly Kaggle News #28
https://www.getrevue.co/profile/upura/issues/weekly-kaggle-news-28-257755
<h3><h2>News</h2><p>文部科学省は23日、新学習指導要領に対応した高校の「情報」の教員研修用教材を<a href="https://www.mext.go.jp/a_menu/shotou/zyouhou/detail/1416746.htm" target="_blank">公開</a>しました。「情報Ⅱ」の「<a href="https://www.mext.go.jp/content/20200609-mxt_jogai01-000007843_007.pdf" target="_blank">第3章 情報とデータサイエンス後半</a>」では機械学習が題材となっており、決定木による分類の項目では<a href="https://www.kaggle.com/c/titanic" target="_blank">KaggleのTitanic</a>も登場しています。</p><p>株式会社Preferred Networksは19日、特徴量エンジニアリングのライブラリ「<a href="https://github.com/pfnet-research/xfeat" target="_blank">xfeat</a>」を公開しました。いくつかの頻出の処理が含まれており、主に同社が開発する最適化ツール「<a href="https://optuna.org/" target="_blank">Optuna</a>」を用いた特徴量選択の手法も実装されています。</p><h2>Competitions</h2><p>「RecSys Challenge 2020」の最終結果が23日に<a href="https://recsys-twitter.com/final_leaderboard/results" target="_blank">発表</a>されました。1位は優秀なKagglerが大量に在籍している<a href="https://developer.nvidia.com/rapids" target="_blank">NVIDIAのRAPIDS</a>チームで、3位には日本から<a href="https://www.wantedly.com/companies/wantedly/post_articles/249713" target="_blank">Wantedy</a>チームが入りました。推薦システムに関する国際会議「ACM Recommender Systems conference (RecSys)」で毎年開催されているコンペで、今年はツイートへのユーザのエンゲージメントを予測するタスクでした。具体的な内容については、<a href="https://www.wantedly.com/companies/wantedly/post_articles/249713" target="_blank">Wantedly</a>や<a href="https://note.com/myaun/n/ndcbd9a4e7150" target="_blank">11位の方</a>が公開した記事にまとまっています。</p><p>Kaggle「<a href="https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification" target="_blank">Jigsaw Multilingual Toxic Comment Classification</a>」コンペが23日に終了しました。多言語の文章の有害度を判定する題材で、<a href="https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/discussion/160862" target="_blank">1位</a>など上位チームには言語別の処理の工夫が見られました。</p><p>ProbSpace「<a href="https://prob.space/competitions/re_real_estate_2020" target="_blank">Re：不動産取引価格予測</a>」コンペが26日に始まりました。今年2〜4月に開催していた「<a href="https://prob.space/competitions/real_estate_2020" target="_blank">不動産取引価格予測</a>」コンペと同様のデータセットを利用し、評価指標のみ外れ値に比較的頑健な「RMSLE(Root Mean Squared Logarithmic Error)」に変更しています。先のコンペの優勝コードも<a href="https://prob.space/topics/chun1182-Post3748b67697bb27cb59e8" target="_blank">公開</a>されている中で、評価指標のみを差し替えたコンペがどのように推移するか注目です。</p><p>米ライドシェア大手Lyftは25日、自動運転の研究向けデータセットを<a href="https://medium.com/lyftlevel5/fueling-self-driving-research-with-level-5s-open-prediction-dataset-f0175e2b0cf8" target="_blank">公開</a>しました。車両の移動ログや地形情報などが含まれており、8月からKaggleでコンペを開催すると予告しています。</p></h3>
<hr>
<p>
<img width="140" height="140" alt="kaggle tweet コンペの闇と光 (コンペ概要と上位解法) - guchiBLO はてな" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/145/802/thumb/20200620004744.png?1592624211" />
<strong style='display: block;'><a href="https://guchio3.hatenablog.com/entry/2020/06/20/115616?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">kaggle tweet コンペの闇と光 (コンペ概要と上位解法) - guchiBLO はてな</a> &mdash; <a href="https://guchio3.hatenablog.com/entry/2020/06/20/115616">guchio3.hatenablog.com</a></strong>
概要 先日 to be twitter masters というチーム名で Tweet Sentiment Extraction コンペ (以下 tweet コンペ) に参加したので、まとめに記事を書いておきます。チームメンバーは筆者と @fuz_qwa @Kenmatsu4 @tkm2261 @yiemon773 の 5 人で、結果は 5 位となり見事金メダルを獲得できました。 本記事では上位解法の紹介と、これを理解するために必要なコンペ概要の紹介を主眼とします。また、チームでやったことはもう少し軽めの記事として後日まとめようと思っています。 いつも文字数多すぎてごちゃごちゃするので、できるだ…
</p>
<div style='clear: both;'></div>
<p><p>17日に終了したKaggle「<a href="https://www.kaggle.com/c/tweet-sentiment-extraction" target="_blank">Tweet Sentiment Extraction</a>」コンペで5位に入った方による上位解法のまとめ記事。5位のチームメンバーらによる<a href="https://youtu.be/gdhqdDwLuU0" target="_blank">YouTube配信</a>のアーカイブも公開されています。配信にも飛び入り参加した2位チームの方は<a href="https://www.i.nagoya-u.ac.jp/kaggle%E3%81%AEtweet-sentiment-extraction%E3%81%A72%E4%BD%8D%E3%82%92%E5%8F%97%E8%B3%9E%E3%81%97%E3%81%BE%E3%81%97%E3%81%9F%E3%80%82%EF%BC%88%E8%A4%87%E9%9B%91%E7%B3%BB%E5%8C%96%E5%AD%A6%E5%B0%82/" target="_blank">大学の広報</a>で取り上げられており、Kaggleの認知度が高まっていると感じさせます。</p></p>
<p>
<strong style='display: block;'><a href="http://mathshingo.chillout.jp/blog24.html?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggle失敗談 ~Tweet Sentiment Extraction~</a></strong>

</p>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/tweet-sentiment-extraction" target="_blank">Tweet Sentiment Extraction</a>」コンペで銀メダルからメダル圏外に転落した方の振り返り記事。コンペの特徴を踏まえて思い当たる原因を列挙している貴重な「失敗談」です。</p></p>
<p>
<img width="140" height="140" alt="Kaggleコンペティション「iMet Collection 2020 - FGVC7」で、DeNAのデータサイエンティストチームが優勝しました | DeNA×AI" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/157/774/thumb/cover1.png?1592901771" />
<strong style='display: block;'><a href="https://dena.ai/news/202005-imet/?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">Kaggleコンペティション「iMet Collection 2020 - FGVC7」で、DeNAのデータサイエンティストチームが優勝しました | DeNA×AI</a> &mdash; <a href="https://dena.ai/news/202005-imet/">dena.ai</a></strong>
Kaggleコンペティション「iMet Collection 2020 - FGVC7」において、DeNAのデータサイエンティストである横尾、矢野、大越によるチームが優勝しました。
本コンペティションは、メトロポリタン美術館に所蔵されている美術品の画像に対して作品の内容や文化的背景などの観点から複数のタグ付けを行うコンペティションで、コンピュータビジョン分野のトップ会議であるCVPR2020のワークショップ The Seventh Workshop on Fine-Grained Visual Categorization の一部として開催されました。
本コンペティションの特徴は一般物体認識と
</p>
<div style='clear: both;'></div>
<p><p>Kaggle「<a href="https://www.kaggle.com/c/imet-2020-fgvc7" target="_blank">iMet Collection 2020 - FGVC7</a>」コンペで優勝したDeNAチームの解法に関する発表資料が掲載された記事。コンピュータビジョン分野の国際会議「CVPR2020」内で開催されたコンペです。</p></p>
<p>
<img width="140" height="140" alt="財務・非財務情報を活用した株主価値予測　コンペ振り返り｜Nishika株式会社｜note" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/160/950/thumb/rectangle_large_type_2_9d88e616f1894db440aaa49ea7d750fc.png?1592964103" />
<strong style='display: block;'><a href="https://note.com/nishika_inc/n/n8678212cb614?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">財務・非財務情報を活用した株主価値予測　コンペ振り返り｜Nishika株式会社｜note</a> &mdash; <a href="https://note.com/nishika_inc/n/n8678212cb614">note.com</a></strong>
 こんにちは。Nishika CTOの松田です。  先日終了した「財務・非財務情報を活用した株主価値予測」コンペについて、コンペ開催に至る背景や上位ソリューションのご紹介をしながら、振り返りたいと思います。 本コンペは、述べ260名の方にご参加いただきました。改めて感謝申し上げます。  本コンペの概要  本コンペは、TIS株式会社にて作成・公開いただいているCoARiJデータセットを活用し、会計年度2014-2017年の各企業の財務・非財務情報から、会計年度2018年の期末時価総額を予測するモデルを構築する、というものでした。  ただし目的変数は、各企業の会計年度2018年の期末時価総
</p>
<div style='clear: both;'></div>
<p><p>先日終了したNishika「<a href="https://www.nishika.com/competitions/4/summary" target="_blank">財務・非財務情報を活用した株主価値予測</a>」コンペについての運営の振り返り記事。コンペ開催に至る背景や上位解法を紹介しています。</p></p>
<p>
<img width="140" height="140" alt="物体検出フレームワークMMDetectionで快適な開発" style="float: right; margin-left: 20px; margin-bottom: 20px;" src="https://s3.amazonaws.com/revue/items/images/006/157/115/thumb/20200622mmdetection-200622120059-thumbnail-4.jpg?1592885485" />
<strong style='display: block;'><a href="https://www.slideshare.net/TatsuyaSuzuki16/mmdetection-236032837?utm_campaign=Weekly%20Kaggle%20News&amp;utm_medium=email&amp;utm_source=Revue%20newsletter">物体検出フレームワークMMDetectionで快適な開発</a> &mdash; <a href="https://www.slideshare.net/TatsuyaSuzuki16/mmdetection-236032837">www.slideshare.net</a></strong>
社内勉強会での発表資料です。 MMDetection: https://github.com/open-mmlab/mmdetection
</p>
<div style='clear: both;'></div>
<p><p>PyTorchベースの物体検出フレームワーク「<a href="https://github.com/open-mmlab/mmdetection" target="_blank">MMDetection</a>」の紹介スライド。具体的な動かし方や、独自モデルへの拡張方法などが詳細にまとめられています。</p></p>
