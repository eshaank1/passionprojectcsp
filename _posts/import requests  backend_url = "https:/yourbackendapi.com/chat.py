import requests

chat_messages = [...]  

backend_url = "https://chat.stu.nighthawkcodingsociety.com/receive_chat_data"
data_to_send = {
    "chat_data": chat_messages
}

try:
    response = requests.post(backend_url, json=data_to_send)

    if response.status_code == 200:
        print("Data sent successfully to the backend.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

