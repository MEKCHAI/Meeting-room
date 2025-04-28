from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Room, Booking
from datetime import date
import calendar
from collections import defaultdict
from django.contrib import messages
from django.db.models import Q
from .forms import RoomForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm  # แทนที่ด้วยฟอร์มของคุณ
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.shortcuts import render, get_object_or_404
from .models import Room
from django.contrib.auth.models import User  # เพิ่มการ import User


# ฟังก์ชันแสดงรายการห้องประชุม
def room_list(request):
    rooms = Room.objects.all()[:3]  # เลือกห้องแค่ 3 ห้อง
    return render(request, 'booking/room_list.html', {'rooms': rooms})

# ฟังก์ชันแสดงรายละเอียดห้องประชุม
def room_detail(request, id):
    room = get_object_or_404(Room, id=id)  # ดึงห้องประชุมที่มี ID ตรง
    return render(request, 'booking/room_detail.html', {'room': room})
def room_list(request):
    rooms = MeetingRoom.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})



class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'signup.html'  # หรือชื่อไฟล์ HTML ที่ใช้
    success_url = reverse_lazy('login')  # เมื่อสมัครสำเร็จจะไปที่หน้า login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # หรือเส้นทางที่คุณต้องการ
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "✅ ยกเลิกการจองเรียบร้อยแล้ว")
        return redirect('my_bookings')
    return redirect('my_bookings')

@staff_member_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ เพิ่มห้องสำเร็จ')
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'booking/room_form.html', {'form': form, 'title': 'เพิ่มห้องประชุม'})

@login_required
def edit_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ แก้ไขห้องเรียบร้อยแล้ว")
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'booking/room_form.html', {'form': form, 'title': 'แก้ไขห้องประชุม'})

@login_required
def delete_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.delete()
    messages.success(request, "🗑️ ลบห้องเรียบร้อยแล้ว")
    return redirect('room_list')

def calendar_grid_view(request, year, month):
    year = int(year)
    month = int(month)
    today = date.today()
    cal = calendar.Calendar(firstweekday=6)  # เริ่มวันอาทิตย์
    month_days = cal.monthdatescalendar(year, month)

    # ✅ ดึงข้อมูลการจองเฉพาะเดือนนี้
    bookings = Booking.objects.filter(date__year=year, date__month=month)

    # ✅ จัดกลุ่มการจองตามวัน
    bookings_by_day = defaultdict(list)
    for booking in bookings:
        bookings_by_day[booking.date.strftime('%Y-%m-%d')].append(booking)

    # ✅ สร้างปฏิทินแบบตาราง
    matrix = []
    week = []
    for day in cal.itermonthdates(year, month):
        if len(week) == 7:
            matrix.append(week)
            week = []
        week.append(day if day.month == month else None)
    if week:
        matrix.append(week)

    # ✅ ส่งข้อมูลไปยังเทมเพลต
    return render(request, 'booking/calendar_grid.html', {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'calendar_matrix': matrix,
        'bookings_by_day': bookings_by_day,
        'prev_month': (month - 1) or 12,
        'prev_year': year - 1 if month == 1 else year,
        'next_month': (month % 12) + 1,
        'next_year': year + 1 if month == 12 else year,
        'today': today,
    })

def month_calendar(request, year, month):
    year = int(year)
    month = int(month)

    month_name = calendar.month_name[month]
    num_days = monthrange(year, month)[1]
    days = range(1, num_days + 1)

    bookings = Booking.objects.filter(date__year=year, date__month=month).select_related('room')
    
    bookings_by_day = defaultdict(list)
    for booking in bookings:
        bookings_by_day[booking.date.day].append(booking)

    return render(request, 'booking/month_calendar.html', {
        'year': year,
        'month': month,
        'month_name': month_name,
        'days': days,
        'bookings_by_day': dict(bookings_by_day),
    })

def room_list(request):
    # ดึงข้อมูลห้องทั้งหมดจากฐานข้อมูล
    rooms = Room.objects.all()

    # สมมุติว่าคุณต้องการแก้ไขชื่อห้องหรือสถานที่ในห้องประชุม
    room_to_update = Room.objects.get(id=1)  # ดึงห้องที่มี id = 1
    room_to_update.name = "ห้องประชุมชั้น 1"  # เปลี่ยนชื่อห้อง
    room_to_update.location = "ชั้น 1 อาคาร A"  # เปลี่ยนสถานที่
    room_to_update.save()  # บันทึกการเปลี่ยนแปลง

     # สมมุติว่าคุณต้องการแก้ไขชื่อห้องหรือสถานที่ในห้องประชุม
    room_to_update = Room.objects.get(id=2)  # ดึงห้องที่มี id = 1
    room_to_update.name = "ห้องประชุมชั้น 2"  # เปลี่ยนชื่อห้อง
    room_to_update.location = "ชั้น 2 อาคาร A"  # เปลี่ยนสถานที่
    room_to_update.save()  # บันทึกการเปลี่ยนแปลง

     # สมมุติว่าคุณต้องการแก้ไขชื่อห้องหรือสถานที่ในห้องประชุม
    room_to_update = Room.objects.get(id=3)  # ดึงห้องที่มี id = 1
    room_to_update.name = "ห้องประชุมชั้น 3"  # เปลี่ยนชื่อห้อง
    room_to_update.location = "ชั้น 3 อาคาร A"  # เปลี่ยนสถานที่
    room_to_update.save()  # บันทึกการเปลี่ยนแปลง





    return render(request, 'booking/room_list.html', {'rooms': rooms})

def calendar_view(request):
    today = date.today()
    year = today.year
    months = [(i, calendar.month_name[i]) for i in range(1, 13)]
    return render(request, 'booking/calendar.html', {'months': months, 'year': year})

@login_required
def book_room(request):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # ถ้าผู้ใช้กดยืนยัน → สร้างการจอง
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)

                # ตรวจสอบการจองซ้ำ
                conflict = Booking.objects.filter(
                    room=booking.room,
                    date=booking.date,
                    start_time__lt=booking.end_time,
                    end_time__gt=booking.start_time
                ).exists()

                if conflict:
                    messages.error(request, "❌ เวลานี้ถูกจองแล้ว กรุณาเลือกเวลาอื่น")
                    return redirect('book_room')  # หรือจะ redirect กลับ form ก็ได้

                booking.user = request.user
                booking.save()
                messages.success(request, "✅ จองสำเร็จ!")
                return redirect('calendar')
        else:
            # ถ้ายังไม่ได้กดยืนยัน → ไปหน้าแสดงข้อมูลเพื่อยืนยัน
            form = BookingForm(request.POST)
            if form.is_valid():
                booking_preview = form.save(commit=False)
                return render(request, 'booking/booking_confirm.html', {
                    'booking': booking_preview,
                    'form_data': request.POST  # ส่งกลับไปให้ hidden field
                })
    else:
        selected_date = request.GET.get('date')
        form = BookingForm(initial={'date': selected_date} if selected_date else None)

    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', 'start_time')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calendar')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def room_detail(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'booking/room_detail.html', {'room': room})

