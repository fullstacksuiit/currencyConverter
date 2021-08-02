from django.shortcuts import render
from .services import latest_currency, historical_currency, calculate_currency
from .utils import CURRENCIES


def index(request):
    context = {
        "lhs": "USD",
        "lhs_value": "",
        "rhs": "INR",
        "rhs_value": "",
        "currencies": CURRENCIES,
    }
    if request.method == "POST":
        rhs = request.POST.get("rhs")
        lhs = request.POST.get("lhs")
        value = float(request.POST.get("lhs_value"))
        rates = latest_currency()
        currency = calculate_currency(rates, lhs, rhs)
        result = currency * value
        context["rhs_value"] = result
        context["lhs_value"] = value
        context["rhs"] = rhs
        context["lhs"] = lhs
    return render(request, "index.html", context)


def history(request):
    context = {
        "lhs": "USD",
        "lhs_value": "",
        "rhs": "INR",
        "rhs_value": "",
        "currencies": CURRENCIES,
    }
    if request.method == "POST":
        date = request.POST.get("date")
        rhs = request.POST.get("rhs")
        lhs = request.POST.get("lhs")
        value = float(request.POST.get("lhs_value"))
        rates = historical_currency(date)
        currency = calculate_currency(rates, lhs, rhs)
        result = currency * value
        context["rhs_value"] = result
        context["lhs_value"] = value
        context["rhs"] = rhs
        context["lhs"] = lhs
    return render(request, "history.html", context)
