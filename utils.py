# utils.py
import json
import os

CHAT_FILE = 'chats.json'

def carregar_chats():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, 'r') as f:
        return json.load(f)

def salvar_chat(chat_id):
    chats = carregar_chats()
    if chat_id not in chats:
        chats.append(chat_id)
        with open(CHAT_FILE, 'w') as f:
            json.dump(chats, f)
