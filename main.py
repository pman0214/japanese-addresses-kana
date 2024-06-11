# -*- coding: utf-8 -*-
#
# Copyright (c) 2023-2024, Shigemi ISHIDA
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
import shutil
import json

# ======================================================================
ORIG_DATA_PATH = 'https://github.com/geolonia/japanese-addresses/raw/develop/data/latest.csv'
OUTDIR = 'public/api/'
API_PATH = 'ja/'
CITIES_PATH = 'ja.json'
CITIES_OBJ_PATH = 'ja-obj.json'

# ======================================================================
# 出力先のクリア
if os.path.exists(OUTDIR):
    shutil.rmtree(OUTDIR)
os.makedirs(OUTDIR)

# データ読み込み
df = pd.read_csv(
    ORIG_DATA_PATH,
    encoding='utf-8',
)
# 大字、小字が空のときは空文字列にする
df.loc[pd.isna(df['大字町丁目名']), '大字町丁目名'] = ''
df.loc[pd.isna(df['大字町丁目名カナ']), '大字町丁目名カナ'] = ''
df.loc[pd.isna(df['小字・通称名']), '小字・通称名'] = ''

df_cities = df[[
    '都道府県コード',
    '都道府県名',
    '市区町村コード',
    '市区町村名',
    '市区町村名カナ',
]].drop_duplicates().set_index('市区町村コード')

df_pref = df_cities[[
    '都道府県コード',
    '都道府県名',
]].drop_duplicates().set_index('都道府県コード')

#--------------------------------------------------
# 都道府県 - 市町村エンドポイント

prefs = df_cities.groupby('都道府県コード').apply(
    lambda x: x['市区町村名'].tolist(),
    include_groups=False,
)
# 都道府県名を連結
prefs = df_pref.join(prefs.rename('cities')).set_index('都道府県名')

# 書き出し
with open(OUTDIR + CITIES_PATH, 'w', encoding='utf-8') as f:
    json.dump(
        pd.Series(prefs['cities']).to_dict(),
        f,
        ensure_ascii=False,
        separators=(',', ':'),
    )

#--------------------------------------------------
# 都道府県 - 市町村オブジェクトエンドポイント

prefs = df_cities.groupby('都道府県コード').apply(
    lambda x: x[['市区町村名', '市区町村名カナ']],
    include_groups=False,
).rename(columns={
    '市区町村名': 'city',
    '市区町村名カナ': 'city_kana',
})
prefs = prefs.groupby('都道府県コード').apply(lambda x: x.to_dict(orient='records'))
# 都道府県名を連結
prefs = df_pref.join(prefs.rename('cities')).set_index('都道府県名')

# 書き出し
with open(OUTDIR + CITIES_OBJ_PATH, 'w', encoding='utf-8') as f:
    json.dump(
        pd.Series(prefs['cities']).to_dict(),
        f,
        ensure_ascii=False,
        separators=(',', ':'),
    )

#--------------------------------------------------
# 町丁目エンドポイント

cols = {
    '大字町丁目名': 'town',
    '大字町丁目名カナ': 'town_kana',
    '小字・通称名': 'koaza',
    '緯度': 'lat',
    '経度': 'lng',
}
towns = df.rename(columns=cols).groupby(
    ['都道府県コード', '市区町村コード'],
    group_keys=True,
).apply(
    lambda x: x[list(cols.values())].to_dict('records'),
    include_groups=False,
)
# 都道府県名、市区町村名を連結
towns = df_cities.join(towns.rename('towns'))

# 書き出し
for k, v in towns.set_index(['都道府県名', '市区町村名'])['towns'].to_dict().items():
    outpath = OUTDIR + API_PATH + k[0]
    outfile = k[1] + '.json'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    with open(outpath + '/' + outfile, 'w') as f:
        json.dump(
            v,
            f,
            ensure_ascii=False,
            separators=(',', ':'),
        )
