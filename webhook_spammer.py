import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("Mister-Three")
print(banner)
msg = input("Input the webhook message: ")
webhook = input("Input the webhook url: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
Easy= 1
while Easy == 1:
    spam(msg, webhook)
