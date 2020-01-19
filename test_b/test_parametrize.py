#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Huang Liping
# @Email : liping.a.huang@ericsson.com
# @File : test_parametrize.py
# @Date : 2019/12/15 
# @Desc :

import pytest

@pytest.mark.parametrize('a, b',
                         [
                             (1, 2),
                             (2, 2),
                             (3, 3)
                         ])
def test_equal(a, b):
    assert a == b