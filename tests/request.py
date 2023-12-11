#######################################################
# A simple test script to check if the server is live #
#######################################################


import requests

# Replace this URL with the actual URL where your Flask app is running
url = 'http://127.0.0.1:5000/response'

# User input (replace this with a test question)
user_question = "Hey GPT! Say 'potato' if you can read me :)"

payload = {'user_input': user_question}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Server Response:", data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Error: {e}")
