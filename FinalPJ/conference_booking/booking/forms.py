from django import forms
from .models import Booking, Room
from django.forms.widgets import TimeInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'ชื่อผู้ใช้งาน',
            'email': 'อีเมล',
            'password1': 'รหัสผ่าน',
            'password2': 'ยืนยันรหัสผ่าน',
        }
        help_texts = {
            'username': 'ชื่อผู้ใช้งานจะต้องมีอย่างน้อย 4 ตัวอักษร',
            'password1': 'รหัสผ่านควรมีความยาวอย่างน้อย 8 ตัวอักษร และไม่ใช่รหัสที่ใช้บ่อยๆ',
            'password2': 'ยืนยันรหัสผ่านให้ตรงกับที่กรอก',
        }
        error_messages = {
            'username': {
                'required': 'กรุณากรอกชื่อผู้ใช้งาน',
                'max_length': 'ชื่อผู้ใช้งานไม่ควรเกิน 150 ตัวอักษร',
            },
            'password1': {
                'required': 'กรุณากรอกรหัสผ่าน',
                'min_length': 'รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร',
                'common_password': 'รหัสผ่านของคุณอาจจะง่ายเกินไป โปรดลองเลือกอื่น',
            },
            'password2': {
                'required': 'กรุณายืนยันรหัสผ่าน',
                'not_match': 'รหัสผ่านไม่ตรงกัน',
            },
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'date', 'start_time', 'end_time']

    # เลือกห้องประชุมจากรายการห้องที่มีในฐานข้อมูล
    room = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label="เลือกห้องประชุม")

    # กำหนด widget สำหรับเวลา
    start_time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}), label="เวลาเริ่มต้น")
    end_time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}), label="เวลาสิ้นสุด")

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity']  # เอา image ออก