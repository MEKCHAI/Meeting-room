from django.conf import settings  # เพิ่มบรรทัดนี้
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('book/', views.book_room, name='book_room'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('calendar/<int:year>/<int:month>/', views.month_calendar, name='month_calendar'),
    path('rooms/', views.room_list, name='room_list'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('calendar/<int:year>/<int:month>/grid/', views.calendar_grid_view, name='calendar_grid'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/edit/', views.edit_room, name='edit_room'),
    path('rooms/<int:room_id>/delete/', views.delete_room, name='delete_room'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('signup/', views.SignUpView.as_view(), name='signup'),  # ตั้ง URL สำหรับหน้าสมัครสมาชิก
    path('rooms/', views.room_list, name='room_list'),  # สำหรับแสดงรายการห้องประชุม
    path('room/<int:id>/', views.room_detail, name='room_detail'),  # สำหรับดูรายละเอียดห้อง
]
