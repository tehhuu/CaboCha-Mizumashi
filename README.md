# CaboCha-Mizumashi
CaboChaを利用し学習データを水増しする

## Description

CaboChaを利用し、文節を文の前方より順次分離することで学習データを水増しします。

具体的な手順は以下の通りです。

1. CaboChaを利用し、文を文節に分割する。
1. 文頭の文節が非自立語を含まない場合、その文節を消去する。
1. 残された文の長さが指定字数以上であれば，それを新たな文として追加し、2に戻る。
1. 残された文の長さが指定字数以下になったら終了する。

Ex)

![mizumashi](https://user-images.githubusercontent.com/48121881/78457267-eaf80d00-76e3-11ea-970c-3d954f3f8406.png)


## Requirement

・ MeCab

・ CaboCha

## Run

1. git clone https://github.com/tehhuu/CaboCha-Mizumashi を実行
1. コード中の min_len (文の最低字数） を適宜変更
1. 入力ファイル(input.txt）を準備 (1行ずつ処理されることに注意)
1. コードを実行すると、出力ファイル output.txt が得られます。
