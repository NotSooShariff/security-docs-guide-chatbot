import requests

# Replace this URL with the actual URL where your Flask app is running
url = 'http://127.0.0.1:5000/response'

# User input (replace this with the actual question)
user_question = "Give me a complete list of documents"

# Create JSON payload
payload = {'user_input': user_question}

# Make a POST request to the Flask app
try:
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print("Server Response:", data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Error: {e}")
