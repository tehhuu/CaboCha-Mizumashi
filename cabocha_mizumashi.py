# -*- coding: utf-8 -*-

import CaboCha
c = CaboCha.Parser('-f1')

with open('input.txt') as data:
    line_list = data.readlines()

    with open('output.txt','w') as new:
        for line in line_list:
            sentence = line.strip().replace(' ','')
            tree =  c.parse(sentence)
            length = len(sentence) #元の文の長さ
            pos = 0 #文中における位置
            min_len = 20 #最低文字数

            for i in range(tree.chunk_size()):
                flag = False
                chunk = tree.chunk(i)
                for j in range(chunk.feature_list_size):
                    if '非自立' in str(chunk.feature_list(j)): #消去する文節が非自立語を含むか確認
                        flag = True
                        break
                for i in range(chunk.token_size): #消去したあとの文の長さを求める
                    length -= len(tree.token(pos + i).surface)
                if flag and length >= min_len: #消去する文節が自立、かつ残りの文の長さが十分の場合に書き込み
                    for i in range(pos, tree.token_size()):
                        new.write(tree.token(i).surface)
                        #new.write(' ')
                    new.write('\n')
                pos += chunk.token_size

