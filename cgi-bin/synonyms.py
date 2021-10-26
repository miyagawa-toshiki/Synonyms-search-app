import random
from collections import namedtuple

import sqlite3
#conn = sqlite3.connect('/Users/miyagawatoshiki/wordresearch/wnjpn.db')
conn = sqlite3.connect('/Users/miyagawatoshiki/wordresearch/wnjpn.db')

Word = namedtuple('Word', 'wordid lang lemma pron pos')

def get_word(lemma):
    cur = conn.execute("select * from word where lemma=?", (lemma,))
    return [Word(*row) for row in cur]

Sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')

def get_senses(word, lang):
    cur = conn.execute("select * from sense where wordid=? and lang=?", (word.wordid, lang))
    return [Sense(*row) for row in cur]

def get_words_from_synset(synset, word, lang):
    cur = conn.execute("select * from word where wordid in (select wordid from sense where synset=? and lang=?) and wordid<>?;", (synset, lang, word.wordid))
    return [Word(*row) for row in cur]
# ランダムに類義語を取り出す関数
def search_synonyms(lemma, lang="jpn"):
    synonym_list = []
    # 1. 単語のwordidを取得する
    wobj = get_word(lemma)
    if wobj:
        word = wobj[0]
        # 2. そのwordidが属するsynsetのsenseを取得する
        senses = get_senses(word, lang)
        for s in senses:
            # 3. synsetに属する単語を類義語として取得する
            synonyms = get_words_from_synset(s.synset, word, lang)
            for syn in synonyms:
                if syn.lemma not in synonym_list:
                    synonym_list.append(syn.lemma)
    else:
        print(f"'{lemma}'の類義語は見つかりませんでした。")

    #return synonym_list
    return random.sample(synonym_list, 1)


#
print(search_synonyms('犬'))