from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import json
import requests
from kafka_producer import send_kafka_message


app = QApplication([])
url = "http://127.0.0.1:8000/send-location"


class UserWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("location_sender.ui", self)
        self.sendButton.clicked.connect(self.button_clicked)
        self.show()


    def button_clicked(self):
        location = self.locText.text()
        name = self.nameText.text()
        print(f"Button Clicked by {name} and {location}")
        self.locText.clear()
        self.nameText.clear()

        # send Post Request
        payload = {
            "name": str(name),
            "location": str(location)
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Request Successful")
            data = response.json()
            message = json.dumps(data).encode('utf-8')
            send_kafka_message(message)
            print(data)
            print(message)
            
        else:
            print("POST request failed with status code:", response.status_code)

window = UserWindow()
app.exec_()

