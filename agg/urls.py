from django.urls import path

from agg.views import show_chart, chart_get_api

app_name = "agg"

urlpatterns = [
    path("api/get/", chart_get_api, name="chart_get_api"),
    path("", show_chart, name="show_chart")
]