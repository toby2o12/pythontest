# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import jieba

seg_list = jieba.cut("姓    名：	陶源	性    别：	男", cut_all=True)
print("Full Mode:", "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("姓    名：	陶源	性    别：	男", cut_all=False)
print("Default Mode:", "/ ".join(seg_list))  # 精确模式
seg_list = jieba.cut("姓    名：	陶源	性    别：	男")  # 默认是精确模式
print(", ".join(seg_list))
seg_list = jieba.cut_for_search("姓    名：	陶源	性    别：	男")  # 搜索引擎模式
print(", ".join(seg_list))