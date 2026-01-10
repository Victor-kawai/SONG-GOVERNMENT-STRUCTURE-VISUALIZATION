import pandas as pd 
import json
import datetime

"""
- 确定展示时间
- 通过 始置时间-罢置时间的公元纪年对 快速筛选对应时间的条目
- 根据类别分别形成机构和官职条目并插入条目字典汇总
- 生成官制树
- TODO: 若插入数据库时按始置时间序进行排序，则可以根据始置时间提前剪枝
"""

# 控制截止时间
time = 1130

def institution_insert(entities, row):
    entities[row["条目名"]] = {
        "name": row["条目名"],
        "type": row["类别"],
        "office": row["衙署"] if row["衙署"]==row["衙署"] else "",
        "function": row["职掌"] if row["职掌"]==row["职掌"] else "",
        "establishment": row["编制"] if row["编制"]==row["编制"] else "",
        "other_names": row["简称与别名"] if row["简称与别名"]==row["简称与别名"] else "",
        "ref_pdf_page": row["参考文档页数"] if row["参考文档页数"]==row["参考文档页数"] else "",
        "trace": "",
        "ref_book": row["出处"] if row["出处"]==row["出处"] else "",
        "children_list": [],
        "children": [],
        "parents": row["上级机构"].split('，') if row["上级机构"]==row["上级机构"] else "",
        "start_time_old": row["始置时间"],
        "end_time_old": row["罢置时间"] if row["罢置时间"]==row["罢置时间"] else "",
        "start_time_new": row["始置时间-公元纪年"],
        "end_time_new": row["罢置时间-公元纪年"] if row["罢置时间-公元纪年"]==row["罢置时间-公元纪年"] else ""
    }

def official_insert(entities, row):
    entities[row["条目名"]] = {
        "name": row["条目名"],
        "type": row["类别"],
        "rank_text": row["官品文本"] if row["官品文本"]==row["官品文本"] else "",
        "rank": row["官品"] if row["官品"]==row["官品"] else "",
        "establishment": row["编制"] if row["编制"]==row["编制"] else "",
        "junior_officials": row["下级官员"] if row["下级官员"]==row["下级官员"] else "",
        "peer_officials": row["平级官员"] if row["平级官员"]==row["平级官员"] else "",
        "function": row["职掌"] if row["职掌"]==row["职掌"] else "",
        "other_names": row["简称与别名"] if row["简称与别名"]==row["简称与别名"] else "",
        "ref_pdf_page": row["参考文档页数"] if row["参考文档页数"]==row["参考文档页数"] else "",
        "trace": "",
        "ref_book": row["出处"] if row["出处"]==row["出处"] else "",
        "parents": row["隶属机构"].split('，') if row["隶属机构"]==row["隶属机构"] else "",
        "start_time_old": row["始置时间"],
        "end_time_old": row["罢置时间"] if row["罢置时间"]==row["罢置时间"] else "",
        "start_time_new": row["始置时间-公元纪年"],
        "end_time_new": row["罢置时间-公元纪年"] if row["罢置时间-公元纪年"]==row["罢置时间-公元纪年"] else ""
    }

def build_entity_dict(entities, file_name):
    src = pd.read_csv(file_name)
    for index, row in src.iterrows():
        if row["始置时间-公元纪年"] > time:
            break
        elif row["罢置时间-公元纪年"] <= time:
            continue
        else:
            if row["类别"] == "机构":
                institution_insert(entities, row)
            else:
                official_insert(entities, row)

# 生成机构树
def build_json(ins_table):
    # 节点的子节点应该由其他节点的父节点决定
    for name, ins_info in ins_table.items():
        if ins_info["parents"] != []:
            for parent in ins_info["parents"]:
                # print(parent, name, institution_tag[name]) # 检查表格用
                ins_table[parent]["children_list"].append(name)
    root_name = "皇帝"
    def build_tree(node_name):
        node_info = ins_table[node_name]
        print(node_info)
        if node_info["type"] == "机构":
            children_names = node_info["children_list"]
            if len(children_names) > 0:
                node_info["children"] = [build_tree(name) for name in children_names]
        return node_info
    nested_tree = build_tree(root_name)
    return nested_tree

if __name__ == "__main__":
    # 根据机构变更表生成 机构路径链 和 机构对象
    entities = {} # 条目对象
    file_name = "尚书省官制.csv"
    build_entity_dict(entities, file_name)
    nested_tree_json = build_json(entities)
    json.dump(nested_tree_json, open(str(time)+".json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)