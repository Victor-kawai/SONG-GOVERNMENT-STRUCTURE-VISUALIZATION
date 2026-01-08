'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2025-04-05 19:01:10
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-04-05 19:02:14
FilePath: \毕设\code\extract_table.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd 
# 读取csv文件并按表格形式输出
df = pd.read_csv('test.csv', encoding='utf-8')
print(df)
with open("test.txt", "w", encoding="utf-8") as f:
    f.write(df.to_string(index=False))