'''
Author: Victor-kawai 1900017878@pku.edu.cn
Date: 2025-04-15 14:21:28
LastEditors: Victor-kawai 1900017878@pku.edu.cn
LastEditTime: 2025-04-15 16:48:28
FilePath: \毕设\code\tmp.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
if __name__ == "__main__":
    lines = []
    with open("元丰新制/完成/尚书省/尚书省原文.md", "r", encoding="utf-8") as f:
        text = f.readlines()
        for line in text:
            if line != "\n":
                lines.append(line)
    print(lines)
    with open("元丰新制/完成/尚书省/尚书省原文2.md", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
