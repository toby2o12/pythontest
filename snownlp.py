# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')

print(s.words)         # [u'这个', u'东西', u'真心',
                #  u'很', u'赞']

print(s.tags)          # [(u'这个', u'r'), (u'东西', u'n'),
                #  (u'真心', u'd'), (u'很', u'd'),
                #  (u'赞', u'Vg')]

print(s.sentiments)    # 0.9769663402895832 positive的概率

print(s.pinyin)        # [u'zhe', u'ge', u'dong', u'xi',
                #  u'zhen', u'xin', u'hen', u'zan']

s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

print(s.han)           # u'「繁体字」「繁体中文」的叫法
                # 在台湾亦很常见。'

text = u'''今年春节前，有朋友给我建议，可以在52nlp里提供一些相关领域的求职信息，既不影响52nlp的整体感觉，也可以获得一定的收益，平衡一下开支。虽然52nlp的域名和虚拟服务器的开支微乎其微，不过这个注意却让我有点心动；虽然52nlp从诞生之初就没本着赢利去，但是探索一下商业模式也无妨。不过比较纠结的是以何种方式展开？'''

s = SnowNLP(text)

print(s.keywords(3))	# [u'语言', u'自然', u'计算机']

print(s.summary(3))	# [u'因而它是计算机科学的一部分',
                #  u'自然语言处理是一门融语言学、计算机科学、
				#	 数学于一体的科学',
				#  u'自然语言处理是计算机科学领域与人工智能
				#	 领域中的一个重要方向']
#print(s.tags)
#print(s.sentences)
print(s.tf)
print(s.idf)



s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
print(s.tf)
print(s.idf)
print(s.sim([u'文章']))# [0.3756070762985226, 0, 0]