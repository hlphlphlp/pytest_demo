#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Huang Liping
# @Email : liping.a.huang@ericsson.com
# @File : test_random.py
# @Date : 2020/1/14 
# @Desc :

import random

def test_random_number():
    assert 3 == random.randint(0, 3)

def test_number_always_pass():
    assert 3 > 2