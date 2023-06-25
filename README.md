# かな付き住所データAPI

[Geolonia 住所データ](https://github.com/geolonia/japanese-addresses/)のデータを読み込んでな付きAPIを提供します。

## Requirements

Python3を使っています。
以下のライブラリが必要です。

- numpy (1.24.2)
- pandas (1.5.3)

## API

pman0214住所データが提供しているAPIに「かな」を付けたデータを提供しています。
元のデータでかなが欠損している場合には、かなは空となっています。

#### 都道府県 - 市町村エンドポイント

このエンドポイントでは、かなは提供していません。

```
https://pman0214.github.io/japanese-addresses-kana/api/ja.json
```

例: [https://pman0214.github.io/japanese-addresses-kana/api/ja.json](https://pman0214.github.io/japanese-addresses-kana/api/ja.json)

```
{
  "北海道": [
    "札幌市中央区",
    "札幌市北区",
    "札幌市東区",
    ...
  ],
  "青森県": [
    "青森市",
    "弘前市",
    "八戸市",
    ...
  ],
  "岩手県": [
    "盛岡市",
    "宮古市",
    "大船渡市",
    ...
  ],
```

#### 町丁目エンドポイント

```
https://pman0214.github.io/japanese-addresses-kana/api/ja/<都道府県名>/<市区町村名>.json
```

※ 都道府県名及び市区町村名は URL エンコードを行ってください。

例: [https://pman0214.github.io/japanese-addresses-kana/api/ja/%E5%8C%97%E6%B5%B7%E9%81%93/%E5%87%BD%E9%A4%A8%E5%B8%82.json](https://pman0214.github.io/japanese-addresses-kana/api/ja/%E5%8C%97%E6%B5%B7%E9%81%93/%E5%87%BD%E9%A4%A8%E5%B8%82.json)

```
[
  ...
  {
    "town": "篠ノ井塩崎",
    "koaza": "四之宮",
    "lat": 36.555444,
    "lng": 138.10524
  },
  {
    "town": "篠ノ井塩崎",
    "koaza": "越",
    "lat": 36.544766,
    "lng": 138.104657
  },
  {
    "town": "篠ノ井塩崎",
    "koaza": "長谷",
    "lat": 36.548163,
    "lng": 138.101997
  },
  {
    "town": "篠ノ井塩崎",
    "koaza": "明戸",
    "lat": 36.549686,
    "lng": 138.106612
  },
  ...
```

## License

APIとして提供しているデータは[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)で提供されています。

APIデータ生成用のスクリプトはMITライセンスで提供されています。
`LICENSE.txt` を参照してください。

* Copyright (c) 2023, Shigemi ISHIDA
