# trpy: Tools for reading papers.

## Install trpy

```bash
$ rye sync
```

## Example
An example of generating paper list of CVPR2024 is shown below.

```bash
$ source .venv/bin/activate
$ generate-paper-list confs/cvpr2024.yaml
$ head -n 3 egs/cvpr2024/paper_list.csv
title,authers,url
UniMODE: Unified Monocular 3D Object Detection,Zhuoling Li · Xiaogang Xu · Ser-Nam Lim · Hengshuang Zhao,
GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection,Xiaotian Li · Baojie Fan · Jiandong Tian · Huijie Fan,
```

Get paper data from arXiv.
```bash
$ search-papers egs/cvpr2024/paper_list.csv --output egs/cvpr2024/arxiv_list.csv
```