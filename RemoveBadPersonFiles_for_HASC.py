#!/usr/bin/env python
# coding: utf-8

"""
__doc__
問題のあるファイル削除プログラム for HASC
badPerson.txtに記述されているpersonデータをHASC Corpusから削除するプログラム
"""
import os
import shutil

print(__doc__)
__author__ = "Haruyuki Ichino"
__version__ = "0.1"
__date__ = "2016/06/13"

# データ格納ディレクトリ
HASCCorpus = './data/'
# 削除するpersonリスト
badPersonListFile = './badPersonList.txt'


# ==========================================================
# ファイルの読み込み & リストに挿入
# ==========================================================

# ファイルから読み込み
f = open(badPersonListFile)
data = f.read()
f.close()

badPersonList = []

# 改行で分割してリストに挿入
lines = data.split('\n')
for line in lines:
    badPersonList.append(line)

print("badPersonList:")
print(badPersonList)
print()


# ==========================================================
# 探索 & 削除
# ==========================================================

actions = os.listdir(HASCCorpus)
# 行動ディレクトリでの処理
for action in actions:
    # .DS_Storeのチェック
    if action == ".DS_Store":
        continue

    input_action_dir = HASCCorpus + action + '/'

    # ディレクトリじゃない場合はスキップ
    if not os.path.isdir(input_action_dir):
        continue

    print("=================================================")
    print(input_action_dir)
    print("=================================================")

    # 被験者別の処理
    persons = os.listdir(input_action_dir)

    # listのpersonが行動ディレクトリ内にあるかチェック
    matchedList = list(set(persons) & set(badPersonList))
    if len(matchedList) == 0:
        print("この行動ディレクトリに該当するbadPersonなし")
        print()
        continue

    for person in persons:
        # .DS_Storeのチェック
        if person == ".DS_Store":
            continue

        input_person_dir = input_action_dir + person + '/'

        # badPersonListとのマッチング
        if person in badPersonList:
            # リストに含まれるなら削除
            try:
                shutil.rmtree(input_person_dir)
                print("%s: 削除" % input_person_dir)
            except:
                print("%s: 削除に失敗" % input_person_dir)

        # 各person処理の終了

    print()
    # 各行動への処理の終了

