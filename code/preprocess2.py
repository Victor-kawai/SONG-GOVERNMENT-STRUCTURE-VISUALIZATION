'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2024-05-22 11:40:23
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-04-25 16:35:44
FilePath: \毕设\code\preprocess2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2024-05-22 11:40:23
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-02-15 00:08:15
FilePath: \毕设\code\preprocess2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from ocr_api import *
from trans_format import *

# 字段：官品 编制 简称 职源 职掌
replace_dict = test_dict
if __name__ == "__main__":
    organization = "司农寺"
    text_file_path = ocr_request(organization)
    print(replace_dict)
    md_format_change2(text_file_path, replace_dict)
    print("\n 处理结束，请人工检查文本内容！")