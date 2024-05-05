# trpy: Tools for reading papers.

## Install trpy

```bash
$ rye sync
```

## Example
An example of generating paper list of CVPR2024 is shown below.

```bash
$ source .venv/bin/activate
$ generate-paper-list confs/cvpr2024_3ddet.yaml \
    --output egs/cvpr2024/3ddet.csv
$ head -n 3 egs/cvpr2024/3ddet.csv
title,authers,url,entry_id,pdf_url,summary,summary_ja
UniMODE: Unified Monocular 3D Object Detection,Zhuoling Li · Xiaogang Xu · Ser-Nam Lim · Hengshuang Zhao,,,,,
GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection,Xiaotian Li · Baojie Fan · Jiandong Tian · Huijie Fan,,,,,
```

Convert to markdown.
```bash
$ convert-to-md egs/cvpr2024/3ddet.csv
```
