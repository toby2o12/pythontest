# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tnpy.tnpy import RegexCore
core = RegexCore('rules/learn')
matchs=core.Match('领导你好！老婆你好');
for m in matchs:
    print('match',m.mstr, 'pos:',m.pos)
print(core.Rewrite('领导你好！老婆您好'));