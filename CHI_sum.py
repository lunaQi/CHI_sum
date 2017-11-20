# !/usr/bin/python
# -*-coding: utf-8 -*-

import pandas as pd

kinds = ['car', 'gat', 'house', 'it', 'jinrong', 'jk', 'mil', 'ny', 'ty', 'yl']
for kind in kinds:
    df = pd.read_csv("/Users/luna/nudoc/" + kind + "/" + kind + "_sum.csv")
    df_new = df.sum()
    df_new.to_csv("/Users/luna/nudoc/" + kind + "/" + kind + "_all.csv")

