# 准备工作（2023/3/26）

## 购买了 T4 云主机
- https://url.cn/jT9XFbJu 
- 咸鱼上可以买到配置更高更便宜的，但是当前由于不熟悉先用这个相对便宜一点的试试。

## 安装远程修改的编辑器/ 在ubuntu下准备 cuda
```bash
vscode 

# https://yinguobing.com/install-cuda113-cudnn8-ubuntu20-04/

```

## 安装 python3.10和 pytorch
```bash

wget -c -N https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh && \
    bash Anaconda3-2023.03-Linux-x86_64.sh -b -p /usr/local/anaconda3

/usr/local/anaconda3/bin/pip install protobuf==3.20.0 transformers==4.27.3 icetk cpm_kernels peft datasets
```

## 下载数据源
```bash 
#!/bibn/bash
#filename download_thuglm-6b_model.sh

cd ./thuglm

wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/208d44ca-5f51-4aa0-9faf-a9dde7835672/pytorch_model-00001-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/bb7269bd-3fc7-4dae-a0c6-ee7083825e03/pytorch_model-00002-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/19e12341-dc70-40f1-b7b4-9e31a198a927/pytorch_model-00003-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/4586ff5d-de04-4417-afc9-f561525f4a59/pytorch_model-00004-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/e89e9d7f-11ca-4260-a0c9-5e6f28f92f29/pytorch_model-00005-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/72cd6d26-e48a-4f19-8156-fa386effe819/pytorch_model-00006-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/14238f1b-8d56-44fd-8699-3f22a3a90c64/pytorch_model-00007-of-00008.bin
wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/2a5c5a5c-560d-471d-bea1-04a51049fc7a/pytorch_model-00008-of-00008.bin

wget -c -N https://cloud.tsinghua.edu.cn/seafhttp/files/e08d3be3-23c6-449f-9beb-a215cd94b189/ice_text.model

```


