# coding:utf-8
import os
import sys
import re 
import random

TXT_DIR = "/root/txt"
SAVE_DIR = "/data2"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def get_txt_content():
    files_info = [] 
    index = 1 
    faield_count = 0 
    for x in os.listdir(TXT_DIR):
        __txt_file = os.path.join(TXT_DIR, x)
        matched = re.match("(.*?)\.txt", x, re.IGNORECASE)
        if not matched:
            print(__txt_file)
        else:
            # print(matched.group(1))
            try:
              with open(__txt_file, "rb") as f:
                  txt_content = f.read().decode("utf-8")
                  f.close() 
            except:
                # print(__txt_file)
                faield_count += 1 
                continue
            tmp_data = dict(
                index=index, 
                filepath=__txt_file, 
                filename=x, 
                content=txt_content
            )
            files_info.append(tmp_data)
    print(faield_count)
    return files_info
        

def push_csv():
    file_infos = get_txt_content() 

    # file_infos = [random.random() for x in range(2000)]
    file_infos_len = len(file_infos)
    import pandas as pd
    # pd.DataFrame()
    
    cur_index = 0 
    offset_index = 0 
    index = 1
    while offset_index < file_infos_len:
      random_len = random.randint(20, 100)
      offset_index = random_len + cur_index
      cur_list = file_infos[cur_index: offset_index]
      cur_index = offset_index
      print(len(cur_list))
      tmp_lists = [{"content":f"这个小说的名字是{x['filename']}, 内容如下：{x['content']}"} for x in cur_list]
      pd.DataFrame(tmp_lists).to_csv(os.path.join(SAVE_DIR, f"{index}.csv"), escapechar="\\")
      index += 1 
      print(f"-======= {index}")


if __name__ == "__main__":
    push_csv() 

    
