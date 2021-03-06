from django.contrib import admin
from django.urls import path
from currency.views import historical_currency, latest_currency, index, history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='lastest'),
    path('history', history, name='history'),
    path('latest', latest_currency),
    path('historical', historical_currency),
]
