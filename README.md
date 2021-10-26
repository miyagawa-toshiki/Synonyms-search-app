# Synonyms-search-app
pythonで作ったwebアプリケーション。cgiでブラウザに表示される。文字を入力すれば、類義語のような文章がたくさん出力される

使ったデータベースは日本語wordnet</br>
http://compling.hss.ntu.edu.sg/wnja/
<!--<h1>cgiとは</h1>-->

編集権限をchmod 755　によって変更した上で処理を行う

（cgiserver.pyがある場所で）</br>
python -m http.server --cgi 8888</br>
を実行する
###Serving HTTP on :: port 8888 (http://[::]:8888/)###

これが出てきたらブラウザで
http://localhost:8888/cgi-bin/index.pyと検索

pythonは自分の環境に合わせる。一行目を自分用に変える






