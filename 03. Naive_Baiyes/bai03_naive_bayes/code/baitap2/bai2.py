# -*- coding: utf-8 -*-
"""Bài tập 2 (bài 3): Từ nào tố cáo tin rác mạnh nhất."""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("data/tin_nhan.csv")
vec = CountVectorizer(token_pattern=r"(?u)\S+")
X = vec.fit_transform(df["noi_dung"])
y = df["la_rac"]

mo_hinh = MultinomialNB(alpha=1.0).fit(X, y)

# feature_log_prob_ có hai dòng: dòng 0 là lớp thường, dòng 1 là lớp rác
chenh = mo_hinh.feature_log_prob_[1] - mo_hinh.feature_log_prob_[0]
bang = pd.Series(chenh, index=vec.get_feature_names_out()).sort_values()

print("5 tu to cao tin RAC manh nhat (log P(tu|rac) - log P(tu|thuong) lon)")
print(bang.iloc[::-1].head(5).round(3).to_string())
print()
print("5 tu cho thay tin THUONG manh nhat (hieu am, nho nhat)")
print(bang.head(5).round(3).to_string())
