# **🚀 ระบบจองห้องประชุมออนไลน์** 🏢💻  โปรเจควิชา ICT 12367

 ![image](https://github.com/user-attachments/assets/049a2e72-cd7a-4d10-918e-4d293504ac54)

ระบบจองห้องประชุมออนไลน์ที่สามารถรองรับการจองห้องประชุมภายในองค์กร โดยระบบจะช่วยให้ผู้ใช้งานสามารถเลือกห้องประชุมในวันและเวลาที่ต้องการได้อย่างสะดวกและรวดเร็ว อีกทั้งยังสามารถดูสถานะของห้องประชุมในแต่ละวันได้จากปฏิทินที่แสดงผลในระบบ

## 🧠 **Stack ที่ใช้**
- 💻 **Django** (Back-end)
- 🎨 **Bootstrap 5** (Front-end)
- 🗄 **SQLite** (Database dev mode)

## **ฟีเจอร์หลักของระบบ**
- **การสมัครสมาชิก** และ **การเข้าสู่ระบบ** 🔑
- **การเลือกห้องประชุม** และการ **แสดงผลปฏิทิน** 📅
- **การจองห้องประชุม** และการ **ยืนยันการจอง** ✔️
- **ระบบล็อกเอาต์** เพื่อป้องกันการเข้าถึงข้อมูลจากผู้ที่ไม่ได้รับอนุญาต 🔓
 # **ตัวอย่างหน้าจอระบบ**
## **หน้าแรก (Home Page) 🏠**
![image](https://github.com/user-attachments/assets/1ec8bf50-855b-4830-b309-599716737b07)

---
## **หน้าเข้าสู่ระบบ (Login Page) 🔑**
![image](https://github.com/user-attachments/assets/fd069f8d-4c1b-4bc3-b251-e3c35a328f01)

---
## **หน้าสมัครสมาชิก (Sign Up Page) 📝**
![image](https://github.com/user-attachments/assets/3cfe5849-0008-4934-b6be-a9736d2a029b)

---
## **หน้าแสดงปฏิทิน (Calendar Page) 📅**
![image](https://github.com/user-attachments/assets/f3f4d2ea-2cc4-4c11-8801-a4805e69e837)

---
## **หน้าจองห้องประชุม (Booking Page) 🏢**
![image](https://github.com/user-attachments/assets/a5b7ac70-46cf-4c01-956f-b3369a711370)

---
## **หน้ายืนยันการจอง (Booking Confirmation Page) ✔️**
![image](https://github.com/user-attachments/assets/a703fba9-4878-4b8d-bde5-a8aa5112ad90)

---
## **หน้าการจองของฉัน **
พอกด ยกเลิก ข้อมูลจะถูกลบออกไป
![image](https://github.com/user-attachments/assets/50a67197-7de0-49f8-9557-ec59dfd2dfce)

---
## **หน้าข้อมูลห้องประชุม (Room Information Page) 🛋️**
![image](https://github.com/user-attachments/assets/e3d63979-3029-4468-87e7-753f464142bb)

---

## **วิธีการรันโปรเจค** 💻

1. **ติดตั้ง Python และ Django**:
   - ตรวจสอบว่า Python ถูกติดตั้งในระบบแล้ว:
     ```bash
     python --version
     ```
   - หากยังไม่ได้ติดตั้ง Django ให้ติดตั้งโดยใช้คำสั่ง:
     ```bash
     pip install django
     ```
 2. **ติดตั้ง Dependencies**:
   - ไปที่โฟลเดอร์โปรเจคและติดตั้ง dependencies ที่จำเป็น:
     ```bash
     cd conference_booking
     pip install -r (name).txt
     ```

3. **ตั้งค่าฐานข้อมูล SQLite**:
   - Django ใช้ **SQLite** เป็นฐานข้อมูลเริ่มต้นในโหมดพัฒนา ซึ่งสามารถเริ่มใช้งานได้ทันที โดยไม่ต้องตั้งค่าอะไรเพิ่มเติม

4. **การ Migrate ฐานข้อมูล**:
   - ทำการ migrate ฐานข้อมูลเพื่อสร้างตารางใน SQLite:
     ```bash
     python manage.py migrate
     ```

5. **รันเซิร์ฟเวอร์**:
   - ใช้คำสั่งนี้เพื่อรันเซิร์ฟเวอร์ Django:
     ```bash
     python manage.py runserver
     ```

6. **เข้าถึงแอปพลิเคชัน**:
   - เมื่อรันเซิร์ฟเวอร์เสร็จแล้ว, เปิดเบราว์เซอร์และเข้าไปที่:
     ```
     http://127.0.0.1:8000/
     ```

  












