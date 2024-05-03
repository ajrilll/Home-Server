import cv2
import websocket
from telebot import TeleBot
from PIL import Image
from io import BytesIO

bot_token = "BOT_HERE"
bot = TeleBot(bot_token)
def send_to_websocket(message):
    try:
        ws = websocket.create_connection("ws://YOUR_IP:PORT")
        ws.send(message)
        ws.close()
        print("Pesan berhasil dikirim ke websocket:", message)
    except Exception as e:
        print("Gagal mengirim pesan ke websocket:", e)

def capture_frame(rtsp_url, output_file):
    try:
        cap = cv2.VideoCapture(rtsp_url)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(output_file, frame)
            print("Capture berhasil disimpan sebagai", output_file)
            return True
        else:
            print("Gagal membaca frame dari aliran video RTSP")
            return False
        
        cap.release()
    except Exception as e:
        print("Error:", e)
        return False

def send_photo_to_telegram(chat_id, photo_file):
    try:
        with open(photo_file, 'rb') as photo:
            bot.send_photo(chat_id, photo)
        print("Foto berhasil dikirim ke Telegram")
    except Exception as e:
        print("Error mengirim foto ke Telegram:", e)

@bot.message_handler(commands=['capture'])
def capture_handler(message):
    if capture_frame(rtsp_url, output_file):
        send_photo_to_telegram(message.chat.id, output_file)
    else:
        bot.reply_to(message, "Capture foto gagal.")

@bot.message_handler(commands=['lamp1'])
def handle_lamp1(message):
    send_to_websocket("1")
    bot.reply_to(message, "OK")

@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Maaf, perintah tidak dikenali.")

rtsp_url = "rtsp://user:pass@yourip:port/"
output_file = "capture.jpg"

bot.polling()
