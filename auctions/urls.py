from django.urls import path

from . import views
app_name = 'auctions'

urlpatterns = [
    path('create/', views.create, name='create'),
    # path('myauctions/', views.my_auctions, name='my_auctions'),
    # Example: /auctions/
    path('', views.auctions, name='auctions'),
    # Example: /auctions/5/
    path('<int:auction_id>/', views.detail, name='detail'),
    # Example: /auctions/5/results/
    # path('<int:auction_id>/results/', views.results, name='results'),
    # Example: /auctions/5/bid/
    path('<int:auction_id>/bid/', views.bid, name='bid'),
]
