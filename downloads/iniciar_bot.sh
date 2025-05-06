#!/data/data/com.termux/files/usr/bin/bash

echo "Baixando o bot..."
pkg install wget unzip -y
wget https://chat.openai.com/mnt/data/bot_arthur_pronto.zip -O bot_arthur_pronto.zip

echo "Extraindo arquivos..."
unzip -o bot_arthur_pronto.zip

echo "Instalando dependências..."
pip install python-telegram-bot --quiet

echo "Iniciando o bot..."
export BOT_TOKEN=7574937721:AAH8uxU-T95ChxUy2_fLiOmkHtDjXlKCzHw
python bot_arthur_pronto.py 
