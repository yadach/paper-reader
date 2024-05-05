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

**要約**

- 概要
    - 過去数年で、マルチカメラに基づく3D物体検出技術は notable な進歩を遂げてきたが、遠方領域など一部のケースでは、一般的な2D物体検出器の方が最先端の3D検出器よりも信頼性が高いことが観察されている。

- 先行研究と比較した際の優位点
    - QAF2D アプローチにより、2D検出結果から3Dクエリアンカーを推論することで、クエリベースの3D物体検出器の性能を向上させる。

- 技術や手法のポイント
    - 2D画像内のオブジェクトの2Dバウンディングボックスを、ボックス内の各サンプリング点を深度、ヨー角、サイズ候補と関連付けることにより3Dアンカーに変換する。
    - 各3Dアンカーの有効性は、その画像内での射影と対応する2Dボックスとの比較によって検証され、有効なアンカーのみが維持され、クエリの構築に使用される。
    - 各クエリに関連付けられた2Dバウンディングボックスのクラス情報は、セットベースの損失のために、推定ボックスを正解と一致させる際に利用される。
    - 3D検出器と2D検出器の画像特徴抽出バックボーンは、わずかなプロンプトパラメータを追加することで共有される。

- 有効性の検証方法
    - QAF2D を3つの人気のクエリベースの3D物体検出器に統合し、nuScenesデータセットで包括的な評価を実施。
    - QAF2D がもたらすnuScenesバリデーションサブセットでの最大改善は、NDS で2.3%、mAP で2.7% である。

- 議論はあるか
    - 議論：今後は、他のデータセットや異なる環境条件下でのパフォーマンスの評価、QAF2D の応用範囲の拡大など、さらなる検証と展望が必要である。
### Multi-View Attentive Contextualization for Multi-View 3D Object Detection
- authers: Xianpeng Liu · Ce Zheng · Ming Qian · Nan Xue · Chen Chen · Zhebin Zhang · Chen Li · Tianfu Wu
### Weak-to-Strong 3D Object Detection with X-Ray Distillation
- authers: Alexander Gambashidze · Aleksandr Dadukin · Maksim Golyadkin · Maria Razzhivina · Ilya Makarov
- entry_id: http://arxiv.org/abs/2404.00679v1

**要約**

- **概要**
    - この論文は、LiDARベースの3D物体検出におけるスパース性と遮蔽の課題に取り組んでいます。従来の方法は、補助モジュールや特定のアーキテクチャ設計に依存することが多く、新しいアーキテクチャには適用できない可能性があります。著者らは、既存のいかなるフレームワークにもシームレスに統合できる汎用的な技術を初めて提案しており、3DコンピュータビジョンにおけるWeak-to-Strong一般化の最初のインスタンスとしています。

- **先行研究と比較した際の優位点**
    - これまでの研究と比較して、任意のフレームワークに容易に統合可能な技術を提案している。
    - タイムラプス点群シーケンスのテンポラルな側面を利用し、オブジェクトを複数の視点から表すObject-Complete framesを生成する新しいフレームワークを導入している。

- **技術や手法のポイント**
    - LiDARフレームの前後から重要な情報を抽出し、オブジェクトを複数の視点で表現するObject-Complete framesを生成するX-Ray Distillation with Object-Complete Framesというフレームワークを使用している。
    - オンライン推論中にObject-Complete framesを生成できない制約に対応するために、Teacher-Studentフレームワーク内でのKnowledge Distillation手法を使用している。

- **有効性の検証方法**
    - 半教師あり学習において、既存の最先端手法を1-1.5 mAPで上回り、5つの確立された教師あり学習モデルを1-2 mAPで向上させることで、提案手法の効果を検証している。
    - 標準の自律走行データセットで、デフォルトのハイパーパラメータを使用しても、性能が向上している。

- **議論はあるか**
    - 議論の記載はない。
### VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection
- authers: Zihua Liu · Hiroki Sakuma · Masatoshi Okutomi
- url: http://www.ok.sc.e.titech.ac.jp/res/VSRD/index.html
- entry_id: http://arxiv.org/abs/2404.00149v1

**要約**

### 概要
- 単眼の3Dオブジェクト検出は、単眼深度推定における固有の不明確性のため、3Dシーン理解において重要な課題を提起している。
- 既存の手法は、典型的にはLiDARポイントクラウド上での高価かつ労力を要するアノテーションを通じて得られる豊富な3Dラベルに依存している。
- 本研究では、VSRD（Volumetric Silhouette Rendering for Detection）という新しい弱教師あり3Dオブジェクト検出フレームワークを提案し、3D検出器を3D教示ではなく弱い2D教示だけで訓練する。

### 先行研究と比較した際の優位点
- 他の弱教師あり3Dオブジェクト検出手法を凌駕する性能を示すKITTI-360データセットの実験を通じて、優れた性能を実証。

### 技術や手法のポイント
- VSRDは、マルチビュー3D自動ラベリングと、自動ラベリング段階で生成された擬似ラベルを使用して単眼3Dオブジェクト検出器をトレーニングすることから構成される。
- 各インスタンスの表面を符号付き距離場（SDF）として表現し、提案されたインスタンス感知型ボリューメトリックシルエットレンダリングによってそのシルエットをレンダリングする。
- インスタンスのSDFを直接最適化するため、各インスタンスのSDFを直方体のSDFと残余距離場（RDF）に分解する。
- レンダリングされたインスタンスマスクをグラウンドトゥルースのインスタンスマスクと比較することで、3Dバウンディングボックスを最適化する。

### 有効性の検証方法
- KITTI-360データセットでの包括的な実験を実施し、提案手法が既存の弱教師あり3Dオブジェクト検出手法を凌駕することを実証。

### 議論はあるか
- 現段階では、議論や課題については言及されていない。
### PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection
- authers: Kuan-Chih Huang · Weijie Lyu · Ming-Hsuan Yang · Yi-Hsuan Tsai
- entry_id: http://arxiv.org/abs/2312.08371v2

**要約**

### 概要
- 最近の時系列LiDARベースの3Dオブジェクト検出器は、2段階の提案ベースのアプローチに基づいて有望な性能を達成している。
- 本研究では、現在のフレームのオブジェクトの点群とその歴史的な軌跡だけを入力として利用し、メモリバンクの保存要件を最小限に抑えるためのポイント軌跡トランスフォーマーを提案。
- Waymoデータセットで豊富な実験を行い、提案手法が最先端の手法に対して優れたパフォーマンスを発揮することを示す。

### 先行研究と比較した際の優位点
- 既存手法では、各フレームのオブジェクトや全体の点群が必要であるため、メモリバンクの利用に関連する課題があるが、本手法は現在のフレームのオブジェクトの点群とその歴史的なトラジェクトリーのみを使用し、メモリバンクの要件を最小限に抑える。
- 点群とトラジェクトリー特徴量を単に連結によって結合する従来の手法と異なり、本手法は長短期記憶を持つポイント軌跡トランスフォーマーを導入し、効果的な相互作用を実現する。

### 技術や手法のポイント
- 点軌跡トランスフォーマーを提案し、長短期記憶および将来を意識した観点に焦点を当て、トラジェクトリー特徴をエンコードしてから点群特徴と効果的に集約する。
- 入力としては、現在のフレームのオブジェクトの点群とその歴史的なトラジェクトリーのみを使用し、メモリバンクの要件を最小限に抑える。

### 有効性の検証方法
- Waymoデータセットで幅広い実験を行い、提案手法が最先端の手法に対して優れたパフォーマンスを示す。

### 議論はあるか
- 提案手法の有効性や汎用性を示すために、さらなるデータセットや環境での評価や他の手法との比較が求められる。
### Decoupled Pseudo-labeling in Semi-Supervised Monocular 3D Object Detection
- authers: Jiacheng Zhang · Jiaming Li · Xiangru Lin · Wei Zhang · Xiao Tan · Junyu Han · Errui Ding · Jingdong Wang · Guanbin Li
### Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-dataset 3D Object Detection
- authers: Zhanwei Zhang · Minghao Chen · Shuai Xiao · Liang Peng · Hengjia Li · Binbin Lin · Ping Li · Wenxiao Wang · Boxi Wu · Deng Cai
- entry_id: http://arxiv.org/abs/2404.19384v1

**要約**

- 概要
  - 3D物体検出（3D UDA）のための自己学習技術が進化し、擬似ラベル（3Dボックス）を選択してモデルを教師付き学習する手法が注目されている。しかし、選択プロセスは信頼性の低い3Dボックスを導入する可能性があり、これらはトレーニングプロセスを妨げることがある。

- 先行研究と比較した際の優位点
  - 信頼性の低い擬似ボックスを改善するために、新しい擬似ラベルリファイナリーフレームワークを提案している。

- 技術や手法のポイント
  - 擬似ボックスの信頼性を向上させるために、互い補完的な増強戦略を提案している。これは、信頼性の低いボックス内のすべてのポイントを削除するか、それを高信頼ボックスで置き換えることによる。
  - 高ビームデータセット内のインスタンスのポイント数が低ビームデータセットよりも大幅に多く、これが訓練プロセス中の擬似ラベルの質を低下させる。様々なドメイン間でRoI特徴を整列させることで、提案を生成し、その問題を緩和している。

- 有効性の検証方法
  - 実験結果は、提案手法が擬似ラベルの品質を効果的に向上させ、自動車運転ベンチマークの6つで最新の手法を一貫して上回っていることを示している。

- 議論はあるか
  - 議論の記載はないが、提案手法には信頼性の低い擬似ボックスを扱う際の新しいアプローチが提示されており、今後の応用や拡張についてさらなる研究が期待される。
### RCBEVDet: Radar-camera Fusion in Bird’s Eye View for 3D Object Detection
- authers: Zhiwei Lin · Zhe Liu · Zhongyu Xia · Xinhao Wang · Yongtao Wang · Shengxiang Qi · Yang Dong · Nan Dong · Le Zhang · Ce Zhu
### $MonoDiff$: Monocular 3D Object Detection and Pose Estimation with Diffusion Models
- authers: Yasiru Ranasinghe · Deepti Hegde · Vishal M. Patel
### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection
- authers: Junbo Yin · Wenguan Wang · Runnan Chen · Wei Li · Ruigang Yang · Pascal Frossard · Jianbing Shen
- entry_id: http://arxiv.org/abs/2403.15241v1

**要約**

- 概要
    - BEV表現は、自動運転シナリオにおける3D空間を記述するための主要なソリューションとして浮上しています。
    - しかし、BEV表現におけるオブジェクトは通常小さく、関連するポイントクラウドコンテキストは疎であるため、信頼性のある3D認識には大きな課題があります。
    - 本論文では、Instance-およびScene-levelのコンテクスト情報を共に捉える革新的なマルチモーダル融合フレームワークであるIS-Fusionを提案しています。
- 先行研究と比較した際の優位点
    - IS-Fusionは、BEVシーンレベルの融合に焦点を当てる既存のアプローチとは異なり、明示的にインスタンスレベルのマルチモーダル情報を取り込むため、3Dオブジェクト検出などのインスタンス中心のタスクを容易にします。
- 技術や手法のポイント
    - IS-Fusionは、Hierarchical Scene Fusion（HSF）モジュールとInstance-Guided Fusion（IGF）モジュールから構成されています。
    - HSFは、Point-to-GridとGrid-to-Region transformersを適用して異なる粒度でマルチモーダルシーンコンテキストを捉えます。
    - IGFは、インスタンス候補を探索し、それらの関係を調査し、各インスタンスのためにローカルなマルチモーダルコンテキストを集約します。
- 有効性の検証方法
    - IS-Fusionは、厳しいnuScenesベンチマークで、これまでに公開されたすべてのマルチモーダルワークを上回る性能を発揮します。
    - このベンチマークにおいてIS-Fusionが優れた結果を出すことで、提案手法の有効性を示しています。
- 議論はあるか
    - 本論文においては、議論の項目が明示されていないため、議論そのものについての詳細は述べられていません。
### CaKDP: Category-aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection
- authers: Haonan Zhang · Longjun Liu · Yuqi Huang · YangZhao · Xinyu Lei · Bihan Wen
### SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection
- authers: Gang Zhang · Chen Junnan · Guohuan Gao · Jianmin Li · Si Liu · Xiaolin Hu
- entry_id: http://arxiv.org/abs/2403.05817v2

**要約**

- 概要
  - LiDARベースの3D物体検出は自律運転において重要である。
  - 従来の高性能な3D物体検出器は、背骨ネットワークと予測ヘッドで密な特徴マップを構築するが、認識範囲が増加すると計算コストが二次的に増加し、長距離検出にスケーリングしづらい。
  - SAFDNetは全く疎な3D物体検出に適した効果的なアーキテクチャで、特徴拡散戦略を用いて中心特徴欠落問題に対処する。

- 先行研究と比較した際の優位点
  - SAFDNetはシンプルかつ効果的なアーキテクチャであり、従来の手法よりも優れた性能を示す。
  - Argoverse2データセットにおいて、HEDNetに比べて2.6% mAP向上し、2.1倍高速である。
  - また、FSDv2に比べても2.1% mAP向上し、1.3倍高速である。

- 技術や手法のポイント
  - SAFDNetは全く疎な3D物体検出に特化したアーキテクチャで、中心特徴欠落問題に対処するための適応的特徴拡散戦略を採用している。

- 有効性の検証方法
  - Waymo Open、nuScenes、Argoverse2のデータセットで実験を行い、SAFDNetは最初の2つのデータセットではわずかに、最後のデータセットでははるかに優れたパフォーマンスを達成した。
  - 特にArgoverse2では、HEDNetに対して2.6% mAPの向上と1.3倍高速であり、FSDv2に対しても2.1% mAPの向上と1.3倍高速であることが示された。

- 議論
  - SAFDNetは長距離検出が必要なシナリオでの効果を検証し、従来の手法よりも優れた性能を示した。
### Learning Occupancy for Monocular 3D Object Detection
- authers: Liang Peng · Junkai Xu · Haoran Cheng · Zheng Yang · Xiaopei Wu · Wei Qian · Wenxiao Wang · Boxi Wu · Deng Cai
- entry_id: http://arxiv.org/abs/2305.15694v1

**要約**

- 概要
  - モノクル3D検出は正確な3D情報の不足から困難な課題であり、既存のアプローチは一般的にジオメトリ制約や密な深度推定に依存して学習を容易にするが、しばしばfrustumと3D空間における3次元特徴抽出の利点を十分に活用できない。

- 先行研究と比較した際の優位点
  - 既存のアプローチと比較して、直接frustumと3D空間で占有率を学習することで、より識別力と情報量が豊かな3D特徴と表現を生み出す。

- 技術や手法のポイント
  - 同期された生の疎なLiDARポイントクラウドを使用し、空間の状態を定義し、ボクセルベースの占有ラベルを生成する。
  - 占有率予測を単純な分類問題として定式化し、関連する占有損失関数を設計する。
  - 結果として得られる占有率の推定値は、元のfrustum/3D特徴を強化するのに使用される。

- 有効性の検証方法
  - KITTIおよびWaymoのオープンデータセットでの実験により、提案手法が新たな最先端を達成し、他の手法を大幅に上回ることを示した。

- 議論はあるか
  - 議論は提示されていない。
### Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection
- authers: Xiaohong Zhang · Huisheng Ye · Jingwen Li · Qinyu Tang · Yuanqi Li · Yanwen Guo · Jie Guo
### MonoCD: Monocular 3D Object Detection with Complementary Depths
- authers: Longfei Yan · Pei Yan · Shengzhou Xiong · Xuanyu Xiang · Yihua Tan
- entry_id: http://arxiv.org/abs/2404.03181v1

**要約**

1. 概要
   - Monocular 3D object detectionは、1枚の画像からオブジェクトの3D位置を正確に取得するため、低コストで注目を集めている。
   - 深度推定はMonocular 3D object detectionの重要かつ困難なサブタスクであり、2Dから3Dへのマッピングの不適切さに起因する。
   - 既存の多重深度の誤差は同じ符号を持ち、互いに相殺することが妨げられ、組み合わせた深度の総合的な精度を制限する。

2. 先行研究と比較した際の優位点
   - 新たな深度予測ブランチであるcomplementary depthを提案し、グローバルかつ効率的な深度手がかりを活用して深度予測の相関を低減させる。
   - 複数の深度手がかり間の幾何学的関係を十分に活用して形状の補完性を達成し、高い相補性を実現。

3. 技術や手法のポイント
   - 新たな深度予測ブランチの導入と、複数の深度手がかり間の幾何学的関係を活用することで、深度の相補性を向上させる。
   - グローバルかつ効率的な深度手がかりを利用することで、局所的な手がかりに頼ることなく深度を予測する。

4. 有効性の検証方法
   - KITTI benchmarkにおける実験により、提案手法が追加データを導入することなく最先端のパフォーマンスを達成したことを示す。
   - 既存のMonocular 3D object detectorsを向上させるために、complementary depthを軽量でプラグアンドプレイなモジュールとして利用可能であることを示す。

5. 議論はあるか
   - 既存手法との比較において、提案手法の計算コストや処理時間に関する議論が追加で考慮されるべきかもしれない。
### BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection
- authers: Zhenxin Li · Shiyi Lan · Jose M. Alvarez · Zuxuan Wu
- entry_id: http://arxiv.org/abs/2312.01696v2

**要約**

- 概要
  - クエリベースのTransformerデコーダーが台頭し、従来の密なBEV（Bird's Eye View）ベースの方法を上回っているが、密なBEVフレームワークは引き続き重要であり、3Dシーンを正確かつ包括的に表現するための優れた深度推定および物体位置特定の能力を持っている。本研究では、提案された改善されたコンポーネント（CRFモジュレーション深度推定モジュール、拡張された受容野を持つ長期的な時間集約モジュール、CRFモジュレーション深度埋め込みをパースペクティブ技術と組み合わせた2段階オブジェクトデコーダーなど）を導入することで、既存の密なBEVベースの3Dオブジェクト検出器の欠点を解消することを目的としている。これらの改良により、「近代化された」密なBEVフレームワークであるBEVNeXtが生まれる。

- 先行研究と比較した際の優位点
  - 密なBEVベースとクエリベースのフレームワークを比較した際、BEVNeXtはさまざまな設定でnuScenesベンチマークで最先端の64.2 NDSの結果を達成するなど、BEVベースおよびクエリベースのフレームワークを凌駕している。

- 技術や手法のポイント
  - CRFモジュレーション深度推定モジュールや長期的な時間集約モジュール、2段階オブジェクトデコーダーなど、提案された改善コンポーネントの導入がポイント。
  - これらの改良により、BEVNeXtと呼ばれる「近代化された」密なBEVフレームワークが生まれる。

- 有効性の検証方法
  - 提案手法の効果を評価するために、nuScenesベンチマークを使用し、BEVNeXtがBEVベースおよびクエリベースのフレームワークを上回ることを示す。
  - nuScenesテストセットで64.2 NDSという最先端の結果が得られ、提案手法の有効性が検証された。

- 議論はあるか
  - クエリベースのTransformerデコーダーと比較して、本研究ではBEVNeXtが有効であることが示されたが、今後の拡張や他のデータセットでの実証など、さらなる議論の余地があるかもしれない。
### 3DiffTection: 3D Object Detection with Geometry-aware Diffusion Features
- authers: Chenfeng Xu · Huan Ling · Sanja Fidler · Or Litany
### Commonsense Prototype for Outdoor Unsupervised 3D Object Detection
- authers: Hai Wu · Shijia Zhao · Xun Huang · Chenglu Wen · Xin Li · Cheng Wang
- entry_id: http://arxiv.org/abs/2404.16493v1

**要約**

- **概要**
    - 3D物体検出の従来の教師なしアプローチは、クラスタベースの疑似ラベル生成と反復的な自己学習プロセスに従っています。しかし、LiDARスキャンの疎な性質からくる課題があり、これが誤ったサイズや位置の疑似ラベルを生み出し、検出性能が低下させています。この論文では、Commonsense Prototype-based Detector（CPD）が紹介され、この問題に取り組みます。CPDは、Commonsense Prototype（CProto）を構築し、これは常識的直感に基づいて高品質のバウンディングボックスと密なポイントで特徴付けられます。その後、CPDはCProtoからのサイズ事前情報を活用して低品質の疑似ラベルを洗練します。さらに、CProtoからの幾何学的知識により、疎なスキャンオブジェクトの検出精度を向上させます。CPDは、Waymo Open Dataset（WOD）、PandaSet、およびKITTIデータセットで、既存の教師なし3D検出器を大きく凌駕します。また、WODでCPDを訓練してKITTIでテストすることで、CPDは、容易および中程度の車両クラスにおいて3D平均精度がそれぞれ90.85％、81.01％を達成します。これらの成果により、CPDは完全に教師付きの検出器に近い位置に配置され、我々の手法の重要性が強調されています。

- **先行研究と比較した際の優位点**
    - CPDはCommonsense Prototypeを活用し、疎なLiDARスキャンにおける誤った疑似ラベルの改善、サイズ事前情報の活用、幾何学的知識の利用により、既存の教師なし3D検出器よりも高い検出精度を達成している。

- **技術や手法のポイント**
    - CPDはCommonsense Prototypeを構築し、疑似ラベルの洗練、サイズ情報の活用、幾何学的知識の利用に焦点を当てている。

- **有効性の検証方法**
    - CPDはWaymo Open Dataset（WOD）、PandaSet、KITTIデータセットでの比較実験により、他の教師なし3D検出器よりも大幅に優れたパフォーマンスを示し、WODで訓練してKITTIでテストすることで有効性を検証している。

- **議論はあるか**
    - CPDは教師なしの環境で高い検出性能を達成していますが、さらなる実データでの検証や他のデータセットでの汎化能力の議論が今後必要となるかもしれません。
### HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection
- authers: Qiming Xia · Wei Ye · Hai Wu · Shijia Zhao · Leyuan Xing · Xun Huang · Jinhao Deng · Xin Li · Chenglu Wen · Cheng Wang
### Improving Distant 3D Object Detection Using 2D Box Supervision
- authers: Zetong Yang · Zhiding Yu · Christopher Choy · Renhao Wang · Anima Anandkumar · Jose M. Alvarez
- entry_id: http://arxiv.org/abs/2403.09230v1

**要約**

- 概要
    - 遠方の3D物体の検出は重要かつ難しい課題である。LiDARに頼ったカメラベースの3D認識では、正確な深度情報のために3D境界ボックスのアノテーションはLiDARに大きく依存している。しかし、遠くの物体にはLiDARポイントがまばらであるため、アノテーションの距離が制限されることがしばしばあり、既存の検出器の長距離シナリオでの能力を妨げる。
- 先行研究と比較した際の優位点
    - 遠方の物体の深度推定に2Dボックスのみの監督を考慮することで、従来より容易にアノテートできることを活かして遠方物体の深度を回復する学習フレームワークLR3Dを提案している。近距離物体の3D監督を使用して2Dボックスと深度のマッピングの生成を学習する暗黙的プロジェクションヘッドを採用し、2Dボックスに依存した遠方物体の深度推定を可能にしている。
- 技術や手法のポイント
    - LR3Dは、2Dボックスに基づく監督のみを使用して遠方物体の深度推定を実現するためのマッピングを学習する。これにより、2D監督付きの長距離3D検出が可能になる。
- 有効性の検証方法
    - 実験では、遠方3DアノテーションなしでもLR3Dを使用することで、カメラベースの手法が200m以上の遠方物体を、完全な3D監督と同等の精度で検出できることを示している。
- 議論はあるか
    - LR3Dは一般的なフレームワークであり、広範囲にわたって3D検出手法に利益をもたらす可能性がある。
