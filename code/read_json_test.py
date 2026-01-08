import json 
import pandas as pd

# 读取json文件
json_file_path = 'example.json'
with open(json_file_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)
df = pd.DataFrame(json_data)
df.to_csv('example.csv', index=False, encoding='utf-8-sig')