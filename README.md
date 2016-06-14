# HASC Corpusの中にあるダメファイル削除プログラム
badPersonList.txtに記述されているpersonデータをHASC Corpusから削除するプログラム

badPersonList.txtは以下のリポジトリのプログラムで作成
<https://github.com/icchiharu/FindBadFiles_for_HASC>

## 使い方
1. pythonファイルと同ディレクトリにbadPersonList.txtを用意.
2. pythonファイルと同ディレクトリにdataディレクトリを用意.
3. dataディレクトリにHASCコーパスのデータを入れる.
4. 以下のコマンドを実行
5. 結果がファイル出力される.

##### コマンド
```
python3 RemoveBadPersonFiles.py
```


### データのディレクトリ構成
```
.  
data  
├── 1_stay  
│  ├── person0001  
│  │   ├── HASCXXXXXX-acc.csv  
│  │   ├── HASCXXXXXX-gyro.csv  
│  │   ├── HASCXXXXXX-mag.csv  
│  │   └── ...  
│  ├── person0002  
│  └── ...  
├── 2_walk  
│　├── person0001  
│　│   ├── HASCXXXXXX-acc.csv  
│　│   ├── HASCXXXXXX-gyro.csv  
│　│   ├── HASCXXXXXX-mag.csv  
│　│   └── ...  
│　├── person0002  
│　└── ...  
└── ...
```

### badPersonList.txtの中身
```
person02056
person02057
person02058
person02059
person02061
person02063
person02064
person02065
person03048
person03049
person03050
person03051
person03052
person03072
person03077
person03079
person04009
person04029
person04031
person04035
person06023
```



### 　
Developed by icchi  
2016/06/14
