
from django.contrib import admin
from django.urls import path
from app.views import hello_view, roll_die_view, random_between_view, add_view, hey_view, age_in_view, order_total_view

# Request (client/browser/app/...) == work (server) ==> response 
# Web_app (HttpRequest) --> HttpResponse
# /hello -> hello_view(request) => response
# /login -> login_view(...) 
# /view-notifcations -> 
# - HTTP (Hyper Text Transfer Protocol)


urlpatterns = [
    path("Hello/<name>/", hello_view),
    path("roll-die/<int:sides>/", roll_die_view),
    path("random-between/<int:lo>/<int:hi>/", random_between_view),
    path("add/<int:num1>/<int:num2>/", add_view),
    path("hey/<str:name>", hey_view),
    path("age-in/<int:Year>/<int:BirthYear>", age_in_view),
    path("order-total/<int:burg>/<int:fry>/<int:drinks>", order_total_view),
    path("admin/", admin.site.urls)
]
