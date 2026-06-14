import os
from flask import Flask, request
import telebot

from bot.bot_instance import bot
from bot.handlers import start, actions

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "Bot online", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("utf-8")

    update = telebot.types.Update.de_json(json_str)

    bot.process_new_updates([update])

    return "", 200