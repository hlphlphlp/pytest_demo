#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Huang Liping
# @Email : liping.a.huang@ericsson.com
# @File : test_demo2.py
# @Date : 2019/12/9 
# @Desc :

import pytest

tag = 'YIDONG'

def data_driven(**data):
    if tag == 'TMO':
        return data['TMO']
    elif tag == 'YIDONG':
        return data['YIDONG']
    elif tag == 'LIANTONG':
        return data['LIANTONG']

d1 = [1,2,3]
d2 = [4,5]


@pytest.mark.parametrize("number", data_driven(TMO=d1, YIDONG=d2))
def test_one(number):
    assert number < 2

if __name__ == '__main__':
    pytest.main()
