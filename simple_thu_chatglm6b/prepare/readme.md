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

# wget -c -N https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh && \
#     bash Anaconda3-2023.03-Linux-x86_64.sh -b -p /usr/local/anaconda3

wget -c -N https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh  && \
bash Miniconda3-py310_22.11.1-1-Linux-x86_64.sh -b -p /usr/local/miniconda3

/usr/local/miniconda3/bin/pip install protobuf==3.20.0 transformers==4.27.3 icetk cpm_kernels peft datasets


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


## 附录
### 挂载数据盘
```bash

docker run -it --rm messense/aliyundrive-webdav aliyundrive-webdav qr login

docker run -d --name=aliyundrive-webdav --restart=unless-stopped -p 8080:8080 \
  -v /etc/aliyundrive-webdav/:/etc/aliyundrive-webdav/ \
    -e REFRESH_TOKEN='xxxx' \
    -e WEBDAV_AUTH_USER=admin \
        -e WEBDAV_AUTH_PASSWORD=password \
          messense/aliyundrive-webdav


```

## 使用模型
- 模型下需要加载配置文件；覆盖到 `checkpoint-500`下
- 接着进行操作就行了。

```bash

{
  "_name_or_path": "THUDM/chatglm-6b",
  "architectures": [
    "ChatGLMModel"
  ],
  "auto_map": {
    "AutoConfig": "configuration_chatglm.ChatGLMConfig",
    "AutoModel": "modeling_chatglm.ChatGLMForConditionalGeneration",
    "AutoModelForSeq2SeqLM": "modeling_chatglm.ChatGLMForConditionalGeneration"
  },
  "bos_token_id": 150004,
  "eos_token_id": 150005,
  "hidden_size": 4096,
  "inner_hidden_size": 16384,
  "layernorm_epsilon": 1e-05,
  "max_sequence_length": 2048,
  "model_type": "chatglm",
  "num_attention_heads": 32,
  "num_layers": 28,
  "position_encoding_2d": true,
  "torch_dtype": "float16",
  "transformers_version": "4.23.1",
  "use_cache": true,
  "vocab_size": 150528
}


```
