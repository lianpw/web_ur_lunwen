"""
@Filename:  cores/read_data
@Author:   lianpengwei
@Time:    2022/9/19 17:39
@Describe:  读取用例中的数据
"""
from pprint import pprint

import openpyxl


def filter_empty(old_l):
    """
    过滤序列中的空置
    :param old_l: 没过滤之前的数据
    :return: 返回过滤之后的数据
    """
    new_l = []
    for i in old_l:
        if i:
            new_l.append(i)
    return new_l


def read_excel(path):
    """
    读取excel文件数据
    :param path:
    :return:
    """
    wb = openpyxl.load_workbook(path)
    suit_dict = {}
    for ws in wb.worksheets:
        case_dict = {}
        case_name = ''
        for line in ws.iter_rows(values_only=True):
            line = filter_empty(line)
            _id = line[0]

            if isinstance(_id, int):
                if _id == -1:
                    case_name = line[3]
                    case_dict[case_name] = []
                elif _id > 0:
                    case_dict[case_name].append(line)
        suit_dict[ws.title] = case_dict
    return suit_dict


if __name__ == '__main__':
    res = read_excel('../testcases/test_excel.xlsx')
    pprint(res)