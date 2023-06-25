# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Shigemi ISHIDA
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np
import pandas as pd
import os
import json

# ======================================================================
#ORIG_DATA_PATH = 'https://github.com/geolonia/japanese-addresses/raw/develop/data/latest.csv'
### for debug
ORIG_DATA_PATH = 'latest.csv'

OUTDIR = 'public/api/ja/'
CITIES_PATH = 'ja.json'

# ======================================================================
# 出力先の作成
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)

# データ読み込み
df = pd.read_csv(
    ORIG_DATA_PATH,
    encoding='utf-8',
)

df_pref = df[[
    '都道府県コード',
    '都道府県名',
]].drop_duplicates().set_index('都道府県コード')

# 都道府県 - 市町村エンドポイント
cities = df.groupby('都道府県コード').apply(lambda x:
    x.sort_values('市区町村コード')['市区町村名'].unique().tolist())
cities = df_pref.join(pd.DataFrame(cities)).set_index('都道府県名')
cities = pd.Series(cities[0])
with open(OUTDIR + CITIES_PATH, 'w', encoding='utf-8') as f:
    json.dump(
        cities.to_dict(),
        f,
        ensure_ascii=False,
    )

# # 町丁目エンドポイント
# for pref in cities.keys():
#     for city in cities[pref]:
#         pass
