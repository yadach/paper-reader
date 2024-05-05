### UniMODE: Unified Monocular 3D Object Detection
- authers: Zhuoling Li · Xiaogang Xu · Ser-Nam Lim · Hengshuang Zhao
### GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection
- authers: Xiaotian Li · Baojie Fan · Jiandong Tian · Huijie Fan
### BEVSpread: Spread Voxel Pooling for Bird’s-Eye-View Representation in Vision-based Roadside 3D Object Detection
- authers: Wenjie Wang · Yehao Lu · Guangcong Zheng · Shuigenzhan · Xiaoqing Ye · Zichang Tan · Zichang Tan · Jingdong Wang · Gaoang Wang · Xi Li
### Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions
- authers: Yujeong Chae · Hyeonseong Kim · Kuk-Jin Yoon
### Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors
- authers: Haoxuanye Ji · Pengpeng Liang · Erkang Cheng
- entry_id: http://arxiv.org/abs/2403.06093v1
- summary_ja: 数年間、マルチカメラを基盤とした３次元物体検出技術は顕著な進歩を遂げてきました。しかし、一部の状況（例：遠方領域）では、主要な２次元物体検出器が最先端の３次元検出器よりも信頼性が高いということを観察しています。本論文では、クエリベースの３次元物体検出器の性能を向上させるために、QAF2Dという新しいクエリ生成アプローチを提案します。これは２次元の検出結果から３次元のクエリアンカーを推論するものです。画像内の物体の２次元のバウンディングボックスを、ボックス内の各サンプリング点と深度、ヨー角度、サイズ候補を関連付けることで、３次元のアンカーのセットに変換します。その後、各３次元アンカーが画像内での射影と対応する２次元ボックスを比較して、有効なアンカーのみを保持し、クエリを構築に使用します。各クエリに関連付けられた２次元バウンディングボックスのクラス情報を利用して、予測されたボックスをグラウンドトゥルースと一致させるためのセットベースの損失関数を適用します。３次元検出器と２次元検出器の画像特徴抽出バックボーンは、プロンプトパラメータを追加することで共有されています。私たちはQAF2Dを３つの人気のあるクエリベースの３次元物体検出器に統合し、nuScenesデータセットで包括的な評価を行いました。nuScenes検証サブセットでQAF2Dがもたらす最大の改善は、NDSで$2.3\%$、mAPで$2.7\%$です。コードは以下のリンクから入手可能です： https://github.com/nullmax-vision/QAF2D。
### Multi-View Attentive Contextualization for Multi-View 3D Object Detection
- authers: Xianpeng Liu · Ce Zheng · Ming Qian · Nan Xue · Chen Chen · Zhebin Zhang · Chen Li · Tianfu Wu
### Weak-to-Strong 3D Object Detection with X-Ray Distillation
- authers: Alexander Gambashidze · Aleksandr Dadukin · Maksim Golyadkin · Maria Razzhivina · Ilya Makarov
- entry_id: http://arxiv.org/abs/2404.00679v1
- summary_ja: この論文は、LiDARを利用した3D物体検出におけるスパース性と遮蔽の重要な課題に取り組んでいます。現在の手法は、補助モジュールや特定のアーキテクチャ設計に依存することが多く、新しい進化するアーキテクチャへの適用範囲を制限する可能性があります。私たちの知る限り、3Dオブジェクト検出のための任意の既存フレームワークにシームレスに統合される多目的な手法を最初に提案したので、3DコンピュータビジョンにおけるWeak-to-Strongの一般化の最初の例となります。これには、点群シーケンスの時間的側面を活用する監督および半監督設定の両方に適した、新しいフレームワークであるObject-Complete Framesを備えたX-Ray Distillationを導入します。この手法は、過去および後続のLiDARフレームから重要な情報を抽出し、複数の視点からオブジェクトを表現するObject-Completeフレームを作成することで、遮蔽とスパース性に対処します。オンライン推論中にObject-Completeフレームを生成することができないという制限に鑑み、私たちはTeacher-Studentフレームワーク内でKnowledge Distillationを利用しています。この手法は、シンプルで情報豊かなObject-Completeフレームを処理する弱いTeacherの挙動を真の強いStudentモデルが模倣することを促し、X線ビジョンを通して見たかのようにオブジェクトの包括的な視点を提供します。私たちの提案手法は、半監督学習においてstate-of-the-artを1-1.5 mAP超え、標準の自動運転データセットにおいて、デフォルトのハイパーパラメータを使用しても5つの確立された監督モデルの性能を1-2 mAP向上させます。Object-Complete framesのコードはこちらで入手可能です：https://github.com/sakharok13/X-Ray-Teacher-Patching-Tools。
### VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection
- authers: Zihua Liu · Hiroki Sakuma · Masatoshi Okutomi
- url: http://www.ok.sc.e.titech.ac.jp/res/VSRD/index.html
- entry_id: http://arxiv.org/abs/2404.00149v1
- summary_ja: モノキュラー3Dオブジェクト検出は、モノキュラー深度推定において本来不適切な性質から3Dシーン理解における著しい課題を提起します。既存の方法は一般的に、LiDARポイントクラウド上で高価かつ労力を要するアノテーションを通じて取得された豊富な3Dラベルを使用した教師あり学習に大きく依存しています。この問題に対処するため、我々はVSRD（Volumetric Silhouette Rendering for Detection）という新しい弱教師あり3Dオブジェクト検出フレームワークを提案しており、3D監督なしでの3Dオブジェクト検出器のトレーニングを2D弱教師のみを用いて行うことが可能です。VSRDは、多視点3D自動ラベリングと自動ラベリング段階で生成された擬似ラベルを使用してモノキュラー3Dオブジェクト検出器をトレーニングすることを可能にします。自動ラベリング段階では、各インスタンスの表面を符号付き距離場（SDF）として表現し、当該インスタンスを示すマスクを提案されたインスタンス認識のためのボリューメトリックシルエットレンダリングによって生成します。レンダリングを介して3D境界ボックスを直接最適化するために、各インスタンスのSDFを立体および残差距離フィールド（RDF）に分解します。このメカニズムにより、レンダリングされたインスタンスマスクをグラウンドトゥルーインスタンスマスクと比較することで、エンドツーエンドの方法で3D境界ボックスを最適化することが可能となります。最適化された3D境界ボックスは、3Dオブジェクト検出の効果的なトレーニングデータとして機能します。我々はKITTI-360データセットで幅広い実験を行い、弱教師あり3Dオブジェクト検出方法よりも我々の手法が優れていることを示しています。コードは https://github.com/skmhrk1209/VSRD で入手可能です。
### PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection
- authers: Kuan-Chih Huang · Weijie Lyu · Ming-Hsuan Yang · Yi-Hsuan Tsai
### Decoupled Pseudo-labeling in Semi-Supervised Monocular 3D Object Detection
- authers: Jiacheng Zhang · Jiaming Li · Xiangru Lin · Wei Zhang · Xiao Tan · Junyu Han · Errui Ding · Jingdong Wang · Guanbin Li
### Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-dataset 3D Object Detection
- authers: Zhanwei Zhang · Minghao Chen · Shuai Xiao · Liang Peng · Hengjia Li · Binbin Lin · Ping Li · Wenxiao Wang · Boxi Wu · Deng Cai
- entry_id: http://arxiv.org/abs/2404.19384v1
- summary_ja: 最近のセルフトレーニング技術は、3D物体検出（3D UDA）における教師なしドメイン適応の顕著な改善を示しています。これらの技術は通常、擬似ラベル、つまり3Dボックスを選択して、ターゲットドメインのモデルを監督しています。ただし、この選択プロセスにより、3Dポイントを前景または背景に明確に割り当てることができない信頼性の低い3Dボックスが避けられません。以前の技術は、これらのボックスを擬似ラベルとして再重み付けすることで、この問題を緩和してきましたが、これらのボックスはトレーニングプロセスに依然として悪影響を及ぼす可能性があります。この問題を解決するために、本論文では新しい擬似ラベルのリファイナリーフレームワークを提案しています。具体的には、擬似ボックスの信頼性を向上させるために、補完的な拡張戦略を提案しています。この戦略は、信頼性の低いボックス内のすべてのポイントを削除するか、高信頼なボックスでそれを置き換えるということを含みます。さらに、ハイビームデータセット内のインスタンスのポイント数は低ビームデータセットよりもかなり高く、トレーニングプロセス中の擬似ラベルの品質を低下させることもあります。この問題を解決するために、追加の提案を生成し、異なるドメイン間でRoIフィーチャを整列させます。実験結果は、当社の手法が擬似ラベルの品質を効果的に向上させ、6つの自動運転ベンチマークで最新技術を常に上回ることを示しています。コードは次の場所で入手可能です：https://github.com/Zhanwei-Z/PERE.
### RCBEVDet: Radar-camera Fusion in Bird’s Eye View for 3D Object Detection
- authers: Zhiwei Lin · Zhe Liu · Zhongyu Xia · Xinhao Wang · Yongtao Wang · Shengxiang Qi · Yang Dong · Nan Dong · Le Zhang · Ce Zhu
### $MonoDiff$: Monocular 3D Object Detection and Pose Estimation with Diffusion Models
- authers: Yasiru Ranasinghe · Deepti Hegde · Vishal M. Patel
### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection
- authers: Junbo Yin · Wenguan Wang · Runnan Chen · Wei Li · Ruigang Yang · Pascal Frossard · Jianbing Shen
- entry_id: http://arxiv.org/abs/2403.15241v1
- summary_ja: 鳥瞰図（BEV）表現は、自動運転シナリオで3D空間を記述するための主要なソリューションとして登場しています。しかし、BEV表現内のオブジェクトは通常小さなサイズであり、関連するポイントクラウドコンテキストは本質的に疎なため、信頼性の高い3D知覚には大きな課題が生じます。本論文では、Instance-およびScene-levelのコンテキスト情報を共に捉える革新的なマルチモーダル融合フレームワークであるIS-Fusionを提案します。IS-Fusionは、従来のBEVシーンレベルの融合に焦点を当てた手法とは基本的に異なり、インスタンスレベルのマルチモーダル情報を明示的に取り込むことで、3Dオブジェクト検出などのインスタンス中心のタスクを支援します。それは、階層的なScene Fusion（HSF）モジュールとInstance-Guided Fusion（IGF）モジュールから構成されます。HSFは、Point-to-GridおよびGrid-to-Regionトランスフォーマーを適用して、異なる粒度でのマルチモーダルなシーンコンテキストを捉えます。IGFはインスタンス候補を選定し、それらの関係を探索し、各インスタンスのローカルなマルチモーダルコンテキストを集約します。これらのインスタンスは、シーン特徴を強化し、インスタンスに対応するBEV表現を生み出すためのガイドとして機能します。難解なnuScenesベンチマークでは、IS-Fusionはこれまでに公開されているすべてのマルチモーダル作品を上回っています。コードはこちらで入手可能です：https://github.com/yinjunbo/IS-Fusion。
### CaKDP: Category-aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection
- authers: Haonan Zhang · Longjun Liu · Yuqi Huang · YangZhao · Xinyu Lei · Bihan Wen
### SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection
- authers: Gang Zhang · Chen Junnan · Guohuan Gao · Jianmin Li · Si Liu · Xiaolin Hu
### Learning Occupancy for Monocular 3D Object Detection
- authers: Liang Peng · Junkai Xu · Haoran Cheng · Zheng Yang · Xiaopei Wu · Wei Qian · Wenxiao Wang · Boxi Wu · Deng Cai
- entry_id: http://arxiv.org/abs/2305.15694v1
- summary_ja: モノキュラー3D検出は、正確な3D情報の欠如により難しい課題です。既存の手法は、一般的に幾何学的制約や密な深度推定に依存して学習を容易にしますが、しばしばフラスタムと3D空間での3次元特徴抽出の利点を十分に活用できません。本論文では、モノキュラー3D検出のための占有学習手法である\textbf{OccupancyM3D}を提案します。これは、フラスタムと3D空間での占有を直接学習し、より区別力があり情報量豊かな3D特徴と表現をもたらします。具体的には、同期した生の疎なLiDAR点群を使用して、空間の状態を定義し、ボクセルベースの占有ラベルを生成します。占有予測を簡単な分類問題として定式化し、関連する占有損失を設計します。得られた占有推定値は、元のフラスタム/3D特徴を強化するために使用されます。その結果、KITTIおよびWaymoオープンデータセットでの実験により、提案手法が最先端技術を実現し、他の手法を大幅に凌駕することが示されました。コードおよび事前学習済みモデルは以下のURLから入手できます：\url{https://github.com/SPengLiang/OccupancyM3D}。
### Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection
- authers: Xiaohong Zhang · Huisheng Ye · Jingwen Li · Qinyu Tang · Yuanqi Li · Yanwen Guo · Jie Guo
### MonoCD: Monocular 3D Object Detection with Complementary Depths
- authers: Longfei Yan · Pei Yan · Shengzhou Xiong · Xuanyu Xiang · Yihua Tan
- entry_id: http://arxiv.org/abs/2404.03181v1
- summary_ja: モノキュラー3D物体検出は、一枚の画像からオブジェクトの3D位置を正確に取得する潜在能力を持ち、低コストで実現可能であるため、広く注目されています。奥行き推定は、2Dから3Dへのマッピングの不適切さから、モノキュラー3D物体検出の重要かつ難しいサブタスクです。さまざまな手法では、オブジェクトの高さやキーポイントなどの複数の局所的な奥行き手がを探索し、オブジェクトの奥行き推定を、単一の奥行き情報の不足を緩和するために複数の奥行き予測のアンサンブルとして定式化しています。しかし、既存の複数の奥行きの誤差は、同じ符号を持ちがちであり、それらが互いに中和するのを阻害し、組み合わせた奥行きの全体的な精度を制限しています。この問題を緩和するために、我々は奥行きの相補性を高めるために、2つの新しい設計を提案します。まず、局所的な手掛かりではなく画像全体からのグローバルで効率的な奥行き手がを利用する、相互補完的な奥行きという新しい深度予測ブランチを追加します。次に、複数の奥行き手間の幾何学的関係を十分に利用することで、形式上の相補性を実現します。これらの設計の恩恵を受けて、私たちの手法はより高い相補性を実現しています。KITTIベンチマークでの実験では、当社の手法が追加データを導入せずに最先端の性能を達成していることが示されています。また、相互補完的な奥行きは、既存のモノキュラー3D物体検出器を向上させるための軽量かつプラグアンドプレイなモジュールにもなり得ます。コードは https://github.com/elvintanhust/MonoCD で入手できます。
### BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection
- authers: Zhenxin Li · Shiyi Lan · Jose M. Alvarez · Zuxuan Wu
- entry_id: http://arxiv.org/abs/2312.01696v2
- summary_ja: 最近、クエリベースのトランスフォーマーデコーダーの台頭により、カメラベースの3Dオブジェクト検出が変革されつつあります。これらのクエリベースのデコーダーは、従来の密なBEV（Bird's Eye View）ベースの手法を凌駕しています。しかし、私たちは、密なBEVフレームワークが、優れた深さ推定およびオブジェクトの位置特定能力を持つため、3Dシーンを正確かつ包括的に描写する点で重要であると主張します。本論文は、提案された改良されたコンポーネントを導入することで既存の密なBEVベースの3Dオブジェクト検出器の欠点に対処することを目的としています。これらの改良点には、オブジェクトレベルの整合性を強制するCRFモジュレーション深さ推定モジュール、拡張された受容野を持つ長期時間集積モジュール、およびCRFモジュレーション深度埋め込みを採用した、透視テクニックと組み合わせた2段階オブジェクトデコーダーが含まれています。これらの改良により、「モダナイズされた」密なBEVフレームワークであるBEVNeXtが生み出されます。nuScenesベンチマークにおいて、BEVNeXtはさまざまな設定で、BEVベースおよびクエリベースのフレームワークを凌駕し、nuScenesテストセットにおける64.2 NDSという最先端の結果を達成します。\url{https://github.com/woxihuanjiangguo/BEVNeXt} でコードが利用可能となります。
### 3DiffTection: 3D Object Detection with Geometry-aware Diffusion Features
- authers: Chenfeng Xu · Huan Ling · Sanja Fidler · Or Litany
### Commonsense Prototype for Outdoor Unsupervised 3D Object Detection
- authers: Hai Wu · Shijia Zhao · Xun Huang · Chenglu Wen · Xin Li · Cheng Wang
- entry_id: http://arxiv.org/abs/2404.16493v1
- summary_ja: 非教師あり3D物体検出の主要なアプローチは、クラスターベースの擬似ラベル生成と反復的な自己学習プロセスに従います。しかし、LiDARスキャンのまばらさによる課題が生じ、誤ったサイズと位置を持つ疑似ラベルが生成され、検出性能が低下します。この問題に対処するため、本論文では非教師あり3D物体検出用のCommonsense Prototypeベースの検出器、CPDと呼ばれるものを紹介します。CPDは最初に、Commonsense Prototype（CProto）を構築し、高品質な境界ボックスと密な点で特徴付けます。その後、CPDはCProtoからのサイズ事前情報を活用して、低品質の擬似ラベルを改良します。さらに、CPDはCProtoからの幾何学的知識により、まばらにスキャンされた物体の検出精度を向上させます。CPDは、Waymo Open Dataset（WOD）、PandaSet、およびKITTIデータセットで、最先端の非教師あり3D検出器を大きく上回る性能を発揮します。また、WODでの訓練およびKITTIでのテストにより、CPDはそれぞれ容易な車両クラスと適度な車両クラスに対して、3D平均精度がそれぞれ90.85％、81.01％を達成します。これらの成果により、CPDは完全な教師あり検出器に近い位置に配置され、当社の手法の重要性が強調されます。コードはhttps://github.com/hailanyi/CPD で入手可能です。
### HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection
- authers: Qiming Xia · Wei Ye · Hai Wu · Shijia Zhao · Leyuan Xing · Xun Huang · Jinhao Deng · Xin Li · Chenglu Wen · Cheng Wang
### Improving Distant 3D Object Detection Using 2D Box Supervision
- authers: Zetong Yang · Zhiding Yu · Christopher Choy · Renhao Wang · Anima Anandkumar · Jose M. Alvarez
- entry_id: http://arxiv.org/abs/2403.09230v1
- summary_ja: 遠隔の3Dオブジェクトの検出の向上は重要かつ困難なタスクです。カメラベースの3D認識において、3D境界ボックスのアノテーションは正確な深度情報のためにLiDARに大きく依存しています。そのため、遠距離のオブジェクトのLiDARポイントのまばらさにより、アノテーションの距離が制限されることが多く、既存の検出器が長距離シナリオのための機能を阻害しています。私たちは、遠隔のオブジェクトについては簡単にアノテーションできるため、遠隔オブジェクトに対して2Dボックスの監督のみを考慮することでこの課題に取り組んでいます。私たちはLR3Dという、遠隔のオブジェクトの欠損深度を回復することを学習するフレームワークを提案しています。LR3Dは、2Dボックスと深度の間のマッピングの生成を学習するために暗黙の射影ヘッドを採用し、近距離のオブジェクトに対する3D監督を使用します。このマッピングにより、2Dボックスに依存した遠隔オブジェクトの深度推定が可能となり、2D監督に基づく長距離3D検出が可能となります。実験結果では、遠隔の3DアノテーションなしでLR3Dを使用すると、カメラベースの方法が遠隔のオブジェクト（200m以上）を完全な3D監督に匹敵する精度で検出できることが示されます。私たちのフレームワークは一般的であり、広範囲にわたる3D検出方法に多大な利益をもたらす可能性があります。2022年10月4日
