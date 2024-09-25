from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus_list, name='bus_list'),
    path('book/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('filtered_bookings/', views.filtered_bookings, name='filtered_bookings'),
    path('receipt/<int:booking_id>/', views.download_receipt, name='download_receipt'),
    path('success/<int:booking_id>/', views.transaction_success, name='transaction_success'),
    # path('', RedirectView.as_view(url='/accounts/home/', permanent=False)),
]
