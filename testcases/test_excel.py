"""
@Filename:  testcases/test_excel
@Author:   lianpengwei
@Time:    2022/9/19 14:32
@Describe:  ...
"""
from pathlib import Path
from pprint import pprint

from cores.case import create_case
from cores.read_data import read_excel

test_dir = Path(__file__).parent
_case_count = 0
file_list = test_dir.glob('test_*.xlsx')
for file in file_list:
    data = read_excel(file)
    # pprint(data)
    for case in create_case(data):
        _case_count += 1
        globals()[f'Test_{_case_count}'] = case
