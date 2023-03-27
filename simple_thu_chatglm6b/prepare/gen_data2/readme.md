# 2023/3/26 开始测试笔趣阁小说的训练效果

-  [`biqukan.py`](./biqukan.py) 数据抓取脚本
   - 2023/3/37 舍弃，直接使用别人弄好的语料，aliyundrive




## 批处理文件utf-8
```bash

#!/bin/bash

# 遍历指定目录下的所有文本文件
for file in /root/txt/*; do
    # 检查文件是否为文本文件
    if [ $(file -b --mime-type "$file") = "text/plain" ]; then
        # 将文件转换为UTF-8编码
        iconv -f $(file -b --mime-encoding "$file") -t UTF-8 "$file" -o "$file"
        echo "Converted $file to UTF-8"
    else
        echo "$file is not a text file"
    fi
done


```
