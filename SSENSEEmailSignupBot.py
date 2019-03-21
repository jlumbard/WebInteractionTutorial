import requests
sesh = requests.session()

url = "https://www.ssense.com/en-ca/newsletters/subscribers"

email = input("Whats your email: ")

gender = input("What is your clothing gender? men/women: ")

payload = {"email": email, "gender": "women", "source": "SSENSE_EN_FOOTER"}

headers = {}

x= sesh.post(url, payload, headers)

print(x.status_code)
