'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2024-05-06 17:06:53
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-02-21 22:37:37
FilePath: \毕设\code\text2table.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import re
from preprocess2 import replace_dict
from text2table_static import data_extract

if __name__ == "__main__":
    target = "中书门下附属机构门"
    text_file = "元丰新制/半完成/"+target+"/"+target+"文本转换后处理后.md"
    data_extract(replace_dict, text_file)
    # TODO:大模型行为测试
