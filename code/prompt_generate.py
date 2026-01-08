'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2025-04-15 14:25:52
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-04-15 16:49:08
FilePath: \毕设\code\prompt_generate.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
if __name__ == "__main__":
    # 读prompt
    with open("./prompt1.0.txt", "r", encoding="utf-8") as f:
        text = f.readlines()
        prompt = ""
        for line in text:
            prompt += line
    # 读示例文本
    with open("./元丰新制/完成/尚书省/尚书省原文2.md", "r", encoding="utf-8") as f:
        text = f.readlines()
        str = ""
        for line in text:
            str += line
        prompt = prompt.replace("example_text", str)
    # 读示例表格
    with open("./元丰新制/完成/尚书省/尚书省表格.md", "r", encoding="utf-8") as f:
        text = f.readlines()
        str = ""
        for line in text:
            str += line
        prompt = prompt.replace("{example_table}", str)
    
    # 读跟进prompt
    with open("./prompt1.0_follow.txt", "r", encoding="utf-8") as f:
        text = f.readlines()
        prompt_follow = ""
        for line in text:
            prompt_follow += line
    # 读目标文本
    with open("./元丰新制/表格转换完成/宰执官类/平章军国事门/平章军国事门文本转换后处理后.md", "r", encoding="utf-8") as f:
        text = f.readlines()
        str = ""
        for line in text:
            str += line
        prompt_follow = prompt_follow.replace("{content}", str)
    # 写出prompt
    with open("./prompt_generate.txt", "w", encoding="utf-8") as f:
        f.write(prompt)
    with open("./prompt_follow_generate.txt", "w", encoding="utf-8") as f:
        f.write(prompt_follow)


