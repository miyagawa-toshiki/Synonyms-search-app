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
<form action="a.py" method="post">
  <input type="text" name="txt" />
  <input type="submit" />
</form>
<p>%s</p>
<p>%s</p>
</body>
</html>
'''

import cgi
import pandas as pd
from janome.tokenizer import Tokenizer
from synonyms import search_synonyms

def is_str(v):
    return type(v) is str

f = cgi.FieldStorage()
txt = f.getfirst('txt', '')

# ここから処理の内容を書く。
if is_str(txt):
  result_list = []
  for i in range(0,20):
    result = ""
    t = Tokenizer()
    # 形態素ごとに分割して順番に処理する
    for token in t.tokenize(txt):
      # 名詞、形容詞の場合
      try:
        if token.part_of_speech.split(',')[0] in ['名詞','形容詞', '副詞']:
          #意味の近いワードに置換
          result = result + search_synonyms(token.surface)[0]
          #result1 = result + search_synonyms(token.surface)[0]
        else:
          result = result + token.surface
      except ValueError:
        txt = 'その文章は対応していません'
    result_list.append(result)
else:
  txt='文章を入力してください'



df = pd.DataFrame(result_list, columns = ['synonyms_text'])
df.to_csv('synonyms.csv')
table = df.to_html()
#t = search_synonyms('犬')
#print(html % df)
print(html % (txt, table))
