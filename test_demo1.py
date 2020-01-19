#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Huang Liping
# @Email : liping.a.huang@ericsson.com
# @File : test_demo1.py
# @Date : 2019/12/9 
# @Desc :

import pytest

def add(a, b):
    return a + b

class TestDemo:

    def test_fun(self):
        assert add(1, 1) == 2
        assert add(1, 2) == 4

    def test_int(self):
        assert 2 == 2

    @pytest.mark.tmo
    def test_string(self):
        assert 'hello, py3test ?' == 'hello world, pytest !'

    def test_set(self):
        assert {3, 4, 1, 2} == {1, 2, 4}

    @pytest.mark.abc
    @pytest.mark.tmo
    def test_lst(self):
        assert ["hello", 1, 3, "aaa"] == ["hello1", 2, 3, "bbb"]


    @pytest.mark.apple
    def test_dic(self):
        print("hahahah")
        assert {"a": 1} == {"a": 1}, "The result of dictionary compare passed"
        assert {"a": 1, "b": 2} == {"b": 2, "a": 3}, "The result of dictionary compare failed"

if __name__ == '__main__':
    pytest.main(["test_demo1.py::TestDemo::test_lst"])
