# استخدام صورة Python
FROM python:3.11-slim

# تعيين العمل إلى مجلد التطبيق
WORKDIR /app

# نسخ متطلبات البوت إلى داخل المجلد
COPY requirements.txt .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي الملفات
COPY . .

# تشغيل البوت
CMD ["python", "app.py"]
