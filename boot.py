import requests

# ضع التوكن الخاص بالبوت هنا
BOT_TOKEN = "7859907084:AAFAC4jkjJ7GWI-9P4ttVH8C7dyq_bAAozI"


CHANNEL_ID = "-1002348202240"



message = "مرحبًا، هذه رسالة تجريبية من كود بايثون!"


url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# البيانات المرسلة
params = {
    "chat_id": CHANNEL_ID,
    "text": message,
    "parse_mode": "HTML"  # يمكن استخدام Markdown أو HTML
}

# إرسال الطلب
response = requests.post(url, params=params)

# طباعة النتيجة
if response.status_code == 200:
    print("✅ تم إرسال الرسالة بنجاح!")
else:
    print(f"❌ فشل في الإرسال! {response.text}")
