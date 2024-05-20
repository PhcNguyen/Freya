import requests
import time
from .urls import TELEBASE



class Telegram:
    def __init__(self, token):
        self.base = TELEBASE.format(token)
        self.handlers = []

    def sendMessage(self, chat_id, text):
        url = self.base + "sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
            return None
        return response.json()

    def getUpdates(self, offset=None):
        url = self.base + "getUpdates"
        payload = {
            'timeout': 100,
            'offset': offset
        }
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error getting updates: {e}")
            return None
        return response.json()

    def Updates(self, updates):
        for update in updates.get("result", []):
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                for handler in self.handlers:
                    response_text = handler(chat_id, text)
                    if response_text:
                        self.sendMessage(chat_id, response_text)

    def Poll(self):
        offset = None
        while True:
            updates = self.getUpdates(offset)
            if updates and updates.get("ok"):
                if updates["result"]:
                    self.Updates(updates)
                    offset = updates["result"][-1]["update_id"] + 1
            time.sleep(1)
