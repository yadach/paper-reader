### DetCLIPv3: Towards Versatile Generative Open-vocabulary Object Detection
- authers: Lewei Yao · Renjie Pi · Jianhua Han · Xiaodan Liang · Hang Xu · Wei Zhang · Zhenguo Li · Dan Xu
- entry_id: http://arxiv.org/abs/2404.09216v1

**要約**

- 概要
    - 通常、事前に定義されたカテゴリーが必要な既存のオープンボキャブラリー物体検出器は、そのアプリケーションシナリオを大幅に制限している。本研究では、DetCLIPv3という高性能な検出器を導入し、オープンボキャブラリー物体検出だけでなく、検出されたオブジェクトの階層的ラベルの生成にも優れている。

- 先行研究と比較した際の優位点
    - DetCLIPv3は、汎用モデルアーキテクチャ、情報密度の高いデータ、効率的なトレーニング戦略という3つの中核的設計を特徴としており、これによりGLIPv2、GroundingDINO、DetCLIPv2を上回り、LVIS minivalベンチマークで47.0の注目すべきゼロショット固定APを達成している。

- 技術や手法のポイント
    - Versatile model architecture
        - キャプションヘッドの統合により、生成機能が強化された堅牢なオープンセット検出フレームワークを導出
    - High information density data
        - 大規模な画像テキストペアの自動注釈パイプラインの開発により、トレーニングを強化するために豊富で多粒度のオブジェクトラベルが提供
    - Efficient training strategy
        - 低解像度の入力を使用した事前トレーニング段階を採用し、広範囲の視覚コンセプトを効率的に学習させる。これに続く微調整段階では、少数の高解像度サンプルを活用して検出性能をさらに向上させる

- 有効性の検証方法
    - DetCLIPv3は、LVIS minivalベンチマークで他のモデルを上回る優れたオープンボキャブラリー検出パフォーマンスを実証しており、VGデータセットの密なキャプショニングタスクでのState-of-the-art 19.7 APを達成している。

- 議論はあるか
    - DetCLIPv3の効果的な設計により、高性能なオープンボキャブラリー検出が示されているが、さらなる応用や他のデータセットでの性能評価が必要かもしれない。
