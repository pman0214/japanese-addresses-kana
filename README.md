# かな付き住所データAPI

[Geolonia 住所データ](https://github.com/geolonia/japanese-addresses/)のデータを読み込んで、かな付きAPIを提供します。

## Requirements

Python3を使っています。
以下のライブラリが必要です。

- numpy (1.24.2)
- pandas (1.5.3)

## API

Geolonia住所データが提供しているAPIに「かな」を付けたデータを提供しています。
元のデータでかなが欠損している場合には、かなは空文字列となっています。

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

例: [https://pman0214.github.io/japanese-addresses-kana/api/ja/%E9%95%B7%E9%87%8E%E7%9C%8C/%E9%95%B7%E9%87%8E%E5%B8%82.json](https://pman0214.github.io/japanese-addresses-kana/api/ja/%E9%95%B7%E9%87%8E%E7%9C%8C/%E9%95%B7%E9%87%8E%E5%B8%82.json)

```
[
  ...
  {
    "town":"篠ノ井塩崎",
    "town_kana":"シノノイシオザキ",
    "koaza":"四之宮",
    "lat":36.555444,
    "lng":138.10524
  },
  {
    "town":"篠ノ井塩崎",
    "town_kana":"シノノイシオザキ",
    "koaza":"山崎",
    "lat":36.557487,
    "lng":138.118548
  },
  {
    "town":"篠ノ井塩崎",
    "town_kana":"シノノイシオザキ",
    "koaza":"平久保",
    "lat":36.560294,
    "lng":138.12407
  },
  ...
```

## Deployment

APIのJSONファイルはGitHub ActionsでGitHub Pagesにデプロイしています。
GitHub Pagesのトップには`public/index.html`を配置しています。

月1回の実行、または`master`ブランチへのpushでデプロイが実行されます。

詳細は`.github/workflows/static.yml`を参照してください。

## Contribute

バグに関するPull Requestはwelcomeです。
なお、オリジナルデータのバグに関しては修正しません。
[Geolonia 住所データ](https://github.com/geolonia/japanese-addresses/)でバグ報告してください。

## License

APIとして提供しているデータは[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)で提供されています。

APIデータ生成用のスクリプトはMITライセンスで提供されています。
`LICENSE.txt` を参照してください。

* Copyright (c) 2023, Shigemi ISHIDA
