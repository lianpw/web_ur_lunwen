"""
@Filename:  cores/case
@Author:   lianpengwei
@Time:    2022/9/19 18:17
@Describe:  动态生成测试用例
"""
from pprint import pprint

import pytest

from cores.kdt import KeyWord


def create_case(case_data: dict):
    for suit_name, case_dict in case_data.items():
        class Test:
            # 把pytest夹具保存到测试类当中
            @pytest.fixture(autouse=True)
            def init_fixture(self, request):
                self.request = request

            @pytest.mark.parametrize('case', case_dict.items())
            def test_(self, case):
                name = case[0]
                step_list = case[1]

                kw = KeyWord(request=self.request)  # 不传递driver, 传递pytest
                for step in step_list:
                    key = step[2]
                    args = step[3:]
                    print(f'{key=}')
                    print(f'{args=}')
                    f = kw.get_kw_method(key)
                    f(*args)
        yield Test