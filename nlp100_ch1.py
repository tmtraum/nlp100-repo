# 00.文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
str00 = "stressed"
print(str00[::-1])
# desserts


# 01. 「パタトクカシーー」
#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
str01 = "パタトクカシー"
ans = str01[::2]
print(ans)
# パトカー


# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
str02_a = "パトカー"
str02_b = "タクシー"

ans = ''.join([i + j for i, j in zip(str02_a, str02_b)])
print(ans)
# パタトクカシーー


# 03.円周率
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
raw_text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = raw_text.replace('.', '').replace(',','')

ans = [len(w) for w in text.split()]

print(ans)
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


# 04. 元素記号
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
#  という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
#   それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
#   連想配列（辞書型もしくはマップ型）を作成せよ．"""

# 未処理のテキストを入力
raw_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# ピリオドを処理する
text = raw_text.replace('.', '')
#print(text)

# 空の辞書を作成
ans_dic= {}

for idx, w in enumerate(text.split(),1):
    if idx in (1,5,6,7,8,9,15,16,19):
        val = w[0]
    else:
        val = w[:2]
    ans_dic[idx] = val

print(ans_dic)
# {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}


# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
def n_gram(target, n):
    return[target[idx:idx+n] for idx in range(len(target) - n + 1)]

target = 'I am NLPer'
print(n_gram(target,2))

words = target.split()
print(n_gram(words,2))
# ['I ', ' a', 'am', 'm ', ' N', 'NL', 'LP', 'Pe', 'er']
# [['I', 'am'], ['am', 'NLPer']]


# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, 
# XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

# def n_gramをそのまま流用。
# setで集合を求める問題。
def n_gram(target,n):
    return[target[idx:idx + n] for idx in range(len(target) - n + 1)]

text_x = 'paraparaparadise'
text_y = 'paragraph'

X = set(n_gram(text_x,2))
Y = set(n_gram(text_y,2))

print(X | Y) 
print(X & Y)
print(X - Y)
print('se' in (X & Y))
# {'ap', 'di', 'ad', 'ag', 'ph', 'is', 'se', 'pa', 'gr', 'ra', 'ar'}
# {'ra', 'ap', 'ar', 'pa'}
# {'se', 'di', 'ad', 'is'}
# False


# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def create_sentence(x,y,z):
    return "{}時の{}は{}".format(x,y,z) 

create_sentence(12,"気温",22.4)
# '12時の気温は22.4'


# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# - 英小文字ならば(219 - 文字コード)の文字に置換
#- その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence): 
    result = ''
    for c in sentence:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

sentence = 'The quick brown Fox jumps over the lazy Dog.'
print('原文: ',sentence)

enigma = cipher(sentence)
print('暗号化:', enigma)

de_enigma = cipher(enigma)
print('復号化:', de_enigma)
# 原文:  The quick brown Fox jumps over the lazy Dog.
# 暗号化: Tsv jfrxp yildm Flc qfnkh levi gsv ozab Dlt.
# 復号化: The quick brown Fox jumps over the lazy Dog.


# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文を与え，その実行結果を確認せよ．

import random

def words_shuffle(word):
    # 単語が４文字以内であればそのまま
    if len(word) <= 4:
        return word
    else:
        # 始めと最後は並び替えなし、真ん中のみランダムシャッフルする
        start = word[0]
        end = word[-1]
        others = random.sample(list(word[1:-1]), len(word[1:-1]))
        return ''.join([start] + others + [end])
    
text = 'Sing a song of sixpence, a pocket full of rye. Four and twenty blackbirds, baked in a pie.'

ans = [words_shuffle(w) for w in text.split()]
print(''.join(ans))
# Singasongofsenixcpe,apecoktfullofrye.Fourandtwetnybalbkdscir,bkeadinapie.







