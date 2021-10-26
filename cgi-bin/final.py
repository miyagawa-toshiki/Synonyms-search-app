#!/Users/miyagawatoshiki/miniconda3/bin/python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>キーワード抽出</title>
</head>
<body>
<h1>キーワードを入力してください</h1>
<form action="final.py" method="post">
  <input type="text" name="keyword" />
  <input type="submit" />
</form>
<p>%s</p>
<p>%s</p>
<p>%s</p>
</body>
</html>
'''

import cgi
import os, sys
import numpy as np
import pandas as pd
import glob
import re
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from janome.tokenizer import Tokenizer
from synonyms import search_synonyms

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

# metadata.csvの置き場所を指定
dir='./cgi-bin/metadata.csv'

def is_str(v):
    return type(v) is str

f = cgi.FieldStorage()
keywords = f.getfirst('keyword', '')

# ここから処理の内容を書く。
# if is_str(keywords):
#   keyws=read_wakachi.parsewithelimination(keywords)
#   keys=np.array(keyws.split())

# else:
#   keys='キーワードを入力してください'
if is_str(keywords):
  result_list = []
  #result2 = ""
  for i in range(0,10):
    result = ""
    t = Tokenizer()
    # 形態素ごとに分割して順番に処理する
    for token in t.tokenize(keywords):
      # 名詞、形容詞の場合
      if token.part_of_speech.split(',')[0] in ['名詞','形容詞', '副詞']:
        #意味の近いワードに置換
        result = result + search_synonyms(token.surface)[0]
        #result1 = result + search_synonyms(token.surface)[0]
        

      else:
        result = result + token.surface
    result_list.append(result)
else:
  print('キーワードを入力してください')

df = pd.DataFrame(result_list, columns = ['synonyms_text'])
df.to_csv('synonyms.csv')
table = df.to_html()
#t = search_synonyms('犬')


print(html % (result, result_list, table))