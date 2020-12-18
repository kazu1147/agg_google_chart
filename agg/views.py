import json

from django.db import models
from django.db.models import Func, DateField, Value, CharField
from django.db.models.functions import TruncSecond
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from agg.models import Product_Log


def show_chart(request):
    if request.method == "GET":
        return render(request, "agg/chart.html")


def chart_get_api(request):
    # 総販売個数の日付別集計
    agg_data = list(Product_Log.objects.all()
                    .annotate(**set_date_annotate("date"))
                    .values("date_str")
                    .annotate(models.Sum("amount")))
    print(f"集約: \n {agg_data} \n")
    agg_data = list(map(transform_format, agg_data))
    print(f"グーグルチャートに合わせたフォーマッティング1: \n {agg_data} \n")
    agg_format_data = dict(cols=[{"label": "日付", "type": "string"}, {"label": "販売個数", "type": "number"}],
                           rows=agg_data)
    agg_format_data = json.dumps(agg_format_data, indent=2, ensure_ascii=False)  # 日本語に対応するため、ensure_ascii=Falseを設定
    print(f"グーグルチャートに合わせたフォーマッティング2: \n {agg_format_data} \n")
    return HttpResponse(agg_format_data)


def transform_format(elem):
    obj = {'c': [{"v": x} for x in elem.values()]}
    return obj



# 日付用のannotateをセットする関数(2010-10-10 15:00(UTC)なら->'2010-10-11')
def set_date_annotate(column: str) -> dict:
    return {
        column + "_str":
            Func(
                column,
                Value('yyyy-mm-dd'),
                function='to_char',
                output_field=CharField()
            )
    }