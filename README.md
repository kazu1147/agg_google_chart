# agg_google_chart
djangoによる集計作業とGoogle chartによる可視化(非同期処理)

| ID  | 商品名  |
| ---- | ---- |
|  1  |  ぶどう  |
|  2  |  りんご  |
|  3  |  みかん  |

| ID  | 日付  | 商品ID  | 販売個数 |
|---- | ---- | ---- | ---- |
| 1 |  2020/12/1  |  1 | 200 |
| 2 |  2020/12/1  |  2 | 160 |
| 3 |  2020/12/1  |  3 | 110 |
| 4 |  2020/12/2  |  1 | 300 |
| 5 |  2020/12/2  |  3 | 470 |
| 6 |  2020/12/2  |  2 | 110 |
| 7 |  2020/12/3  |  3 | 215 |
| 8 |  2020/12/3  |  2 | 100 |
| 9 |  2020/12/3  |  1 | 550 |

上記のレコードに対して、日付別に集計を行う(総販売個数)