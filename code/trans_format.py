'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2024-04-11 18:31:28
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-02-21 22:31:00
FilePath: \毕设\code\trans_format.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re

# 字段：官品 编制 简称 职源 职掌
# 来源: preprocess2.py
test_dict = {"简称与别名": ["简称"],
                "简称与别称": ["简称"],
                "职源、沿革、职掌、品位": ["职源", "职掌", "官品"],
                "职源与沿革、职掌、官品": ["职源", "职掌", "官品"], 
                "职源与沿革、职掌": ["职源", "职掌"],
                "官品、编制、简称与别名": ["官品", "编制", "简称"],
                "职源、沿革、编制": ["职源", "编制"],
                "职掌与沿革": ["职掌", "职源"],
                "职源、职掌、编制": ["职源", "职掌", "编制"], 
                "职掌、官品、编制": ["职掌", "官品", "编制"], 
                "职源、职掌": ["职源", "职掌"],
                "职掌、品位": ["职掌", "官品"], 
                "编制、职能":["职掌", "编制"],
                "编制与品位": ["编制", "官品"],
                "沿革与职掌": ["职源", "职掌"],
                "省称与别名": ["简称"],
                "简称与追改": ["简称"],
                "简称与旧称": ["简称"],
                "职源与沿革": ["职源"], 
                "职源与改革": ["职源"],
                "省称与别名": ["简称"],
                "追称": ["简称"],
                "职掌": ["职掌"],
                "职能": ["职掌"],
                "位遇": ["官品"],
                "序位": ["官品"], 
                "地位": ["官品"],
                "品秩": ["官品"],
                "编制": ["编制"],
                "职源": ["职源"], 
                "简称": ["简称"], 
                "通称": ["简称"], 
                "省称": ["简称"], 
                "别名": ["简称"], 
                "别称": ["简称"], 
                "合称": ["简称"],
                "品阶": ["官品"],
                "官品": ["官品"], 
                "品位": ["官品"],
                "班位": ["官品"],
                "沿革": ["职源"],
                "泛称": ["简称"]} 

def md_format_change2(file_name, replace_dict):
    print("==== markdown格式转换开始 ====")

    with open(file_name, "r", encoding="utf-8") as src:
        data = src.read()

    # Process replace_list items
    for key in replace_dict.keys():
        item = "\n"+key
        stripped_item = item.strip()  # Remove leading/trailing whitespace
        pattern = re.escape(item)
        replacement = f"\n#### {stripped_item}\n"
        data = re.sub(pattern, replacement, data)

    # Replace image file patterns (e.g., 123L.jpg) with Markdown format
    # image_pattern = r'([0-9]{2}[LR])\.jpg'  # Matches 3 digits followed by L or R and ending with .jpg
    # image_replacement = r'## /page{\1}'  # Replaces with /page{digitsLorR}
    # data = re.sub(image_pattern, image_replacement, data)

    # Write modified content to the output file
    with open(file_name[:file_name.rfind(".")]+"转换后.md", "w", encoding="utf-8") as dst:
        dst.write(data)

    print("==== markdown格式转换完成 ====")

if __name__ == "__main__":
    file_name = "元丰新制/表格转换完成/宰执官类/宰执官类文本.md"
    md_format_change2(file_name, test_dict)
