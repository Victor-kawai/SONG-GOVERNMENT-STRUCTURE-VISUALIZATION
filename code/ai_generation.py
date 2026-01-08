'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2025-04-25 16:29:04
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-05-13 17:39:39
FilePath: \毕设\code\ai_generation.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import json
import re
import pandas as pd

'''
 * 程序主要功能是将json文件和文本文件按条目拆分，再逐条喂给大模型进行处理。
 * 处理完成后将结果保存到一个新的json文件中。
 * 汇总后再统一输出成表格。
'''

# 读取预处理过的表格文件
def read_json_file(entry_name: str)-> list:
    json_file_path = '元丰新制/表格转换完成/'+entry_name+'/'+entry_name+'表格.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    print("读取json文件完成")
    return json_data

# 读取文本文件
def read_text_file(entry_name: str)-> dict:
    text_file_path = '元丰新制/表格转换完成/'+entry_name+'/'+entry_name+'文本转换后处理后.md'
    with open(text_file_path, 'r', encoding='utf-8') as f:
        text = f.readlines()
    # 删掉前两行页数信息和门类信息后的文本内容
    txt = ""
    for i in text[2:]:
        txt += i
    # 将文本中的## /page{\d+[LR]}行删掉
    txt_without_page = re.sub(r'## /page\{\d+[LR]}\n', '', txt)
    # 生成一个列表，列表中的每个元素是一个条目
    i = -1
    txt_list = {}
    entry = ''
    txt_entries_list = []
    for line in txt_without_page.split('\n'):
        if line.startswith('### '):
            entry = line[4:].replace(' ', '') # 规范化条目名格式，去掉可能的空格
            txt_entries_list.append(entry)
            txt_list[entry] = line+'\n'
            i += 1
        elif line.startswith('#### '):
            txt_list[entry] += '\n'+line+'\n'
        else:
            txt_list[entry] += line
    print("读取文本文件完成")
    return txt_list

# 生成prompt
def prompt_generation(json_data, text_data, prompt)-> str:
    prompt = prompt.replace("{input_table}", json_data)
    prompt = prompt.replace("{input_text}", text_data)
    print("生成prompt完成")
    return prompt


if __name__ == '__main__':
    entry_name = "司农寺门"
    json_list = read_json_file(entry_name)
    txt_dict = read_text_file(entry_name)
    # 生成读取prompt文件
    with open('prompt1.0_follow.txt', 'r', encoding='utf-8') as f:
        prompt = f.read()
    # json条目名有多余空格，需要去掉（已经可以匹配所有条目）
    # 文本信息的顺序和json文件的顺序可能不一致，按照json的顺序来获得文本信息
    entry_jsons = []
    for item in json_list:
        item["条目名"] = item["条目名"].replace(' ', '')
        if item["条目名"] in txt_dict.keys():
            # json内容只提取一部分，另外做一个结构存储。
            prompt_attr_list = ["类别", "条目名", "衙署", "上级机构", "下级机构", "隶属机构", "官品文本", "官品", "品级", "编制文本", "编制", "官额", "吏额", "职掌文本", "职掌", "出处", "始置时间", "罢置时间", "前身"]
            # tmp提取prompt_attr_list中的属性
            tmp = {key : item[key] for key in prompt_attr_list if key in item}
            # 将json数据转换为字符串格式
            input_table = json.dumps(tmp, ensure_ascii=False, indent=4) # indent=4会保留json的缩进
            message = prompt_generation(input_table, txt_dict[item["条目名"]], prompt)
            print(message)
            # TODO: 这里需要调用大模型进行处理，返回结果
            response = ""
            # TODO: 若是json数组，需要循环拿
            # 将返回结果转换为json格式
            entry_json = json.loads(response)
            # 这里需要将新的处理结果重新存回去原始json再转换成表格
            attr_list = ["类别", "衙署", "上级机构", "下级机构", "隶属机构", "官品", "品级", "编制", "官额", "吏额", "职掌", "始置时间", "罢置时间", "前身"]
            for entry in attr_list:
                item[entry] = entry_json[entry]
            entry_jsons.append(item)
    # 将处理后的结果保存到一个新的json文件中
    with open('元丰新制/表格转换完成/'+entry_name+'/'+entry_name+'ai后.json', 'w', encoding='utf-8') as f:
        json.dump(entry_jsons, f, ensure_ascii=False, indent=4)
    print("处理完成，结果已保存到新的json文件中。")
    # 汇总后再统一输出成表格
    df = pd.DataFrame(entry_jsons)
    df.to_csv('元丰新制/表格转换完成/'+entry_name+'/'+entry_name+'ai后.csv', index=False, encoding='utf-8-sig')
    print("汇总完成，结果已保存到新的csv文件中。")


# TODO：prompt效果不够好，还要调，主要是官额吏额的部分。——目前调好了，还有个分期的问题未处理。
    # TODO：检查prompt是否能输出json列表
    # TODO：设计循环读取
# TODO: 调用大模型的code补全。
# TODO：慢慢做表格吧sigh