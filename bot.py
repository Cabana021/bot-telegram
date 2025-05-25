import os
import telebot
import random
import threading
import schedule
import time
from dotenv import load_dotenv
from fotos import photos
from audios import songs
from utils import salvar_chat, carregar_chats

# Carrega variáveis do arquivo .env
load_dotenv()  

# Carrega o token do bot
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Introdução /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    salvar_chat(message.chat.id)
    bot.reply_to(message, "Oi, amor!! ebaaa 😄")

# Envia uma música /song
@bot.message_handler(commands=['song'])
def send_song(message):
    musica = random.choice(list(songs.values()))
    resposta = (
        f"Uma música que lembra o meu amor para o meu amor.. <3\n\n"
        f"🎶 *{musica['title']}*\n"
        f"{musica['link']}"
    )
    bot.send_message(message.chat.id, resposta, parse_mode='Markdown')

# Foto de gatinho /gato
@bot.message_handler(commands=['gato'])
def send_random_cat_photo(message):
    # Acessando as URLs das fotos de gatos
    cat_photos = photos['gatos']

    # Escolhendo uma foto aleatoriamente
    import random
    photo_key = random.choice(list(cat_photos.keys()))
    photo_url = cat_photos[photo_key]

    bot.send_photo(message.chat.id, photo_url, caption="Aqui está um gatinho!")

# Foto de doguinho /dog
@bot.message_handler(commands=['dog'])
def send_random_dog_photo(message):
    # Acessando as URLs das fotos de cachorro
    dog_photos = photos['caes']

    # Escolhendo uma foto aleatoriamente
    import random
    photo_key = random.choice(list(dog_photos.keys()))
    photo_url = dog_photos[photo_key]

    bot.send_photo(message.chat.id, photo_url, caption=f"Aqui está um doguinho!")

# Mensagem de bom dia
def bom_dia():
    mensagem = "Bom dia, meu amor!! ☀️💖"
    for chat_id in carregar_chats():
        bot.send_message(chat_id, mensagem)

# Lista com mensagens que serão enviadas de forma aleatória durante o dia
mensagem = [
    'Eii, te amo, meu amor! Beijoss',
    'Tanta saudades do meu amorzinho...',
    'E aí, puta, achou que seria algo fofo?',
    'Te amoooooo',
    'Me responde no tiktok, cachorra',
    'Amo muito você!',
    'Mostra os peitos? Te amo tanto..',
    'Estou sofrendo de tanta saudade.. me mande mensagem agora',
    'Ebaaaaa',
    'Saudades da minha mulher..',
    'Gostosa',
]

# Mensagem aleatória
def mensagem_aleatoria():
    for chat_id in carregar_chats():
        bot.send_message(chat_id, random.choice(mensagem))

# Agendando mensagens
def agendar_mensagens():
    schedule.every().day.at("06:00").do(bom_dia) # Envia uma mensagem de bom dia às 6h
    schedule.every(24).hours.do(mensagem_aleatoria)  # Envia uma mensagem aleatória a cada 24h

    while True:
        schedule.run_pending()
        time.sleep(60)

# Rodando em thread paralela
threading.Thread(target=agendar_mensagens, daemon=True).start()
# Mantém o bot ligado infinitamente
bot.infinity_polling()
