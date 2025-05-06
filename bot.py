from telegram.ext import Updater, CommandHandler

def start(update, context):
    mensagem = (
        "🚗 *Sejam bem-vindos à minha lojinha!* 🚗\n"
        "💥 Instagram: @arthur.vendas01\n\n"
        "Digite /produtos para ver a tabela de preços."
    )
    update.message.reply_text(mensagem, parse_mode='Markdown')

def produtos(update, context):
    tabela = """
🚗 *Sejam bem-vindos à minha lojinha!* 🚗  
💥 Instagram: @arthur.vendas01

*Golds com World Sale*  
10k: R$1,50  
20k: R$2,50  
30k: R$3,50  

*Golds sem World Sale*  
90k: R$3,65  
100k: R$4,00  
150k: R$4,25  
200k: R$4,50  
250k: R$4,75  
300k: R$5,00  
350k: R$5,25  
400k: R$5,50  
450k: R$5,75  
500k: R$6,00  

*Money*  
10M: R$1,00  
20M: R$2,00  
30M: R$3,00  
40M: R$4,00  
50M: R$5,00  

*Desbloqueios na Conta*  
W16: R$4,00  
Fumaça: R$3,50  
Todos os carros pagos: R$3,50  
Todos os carros de gold: R$2,00  
Desbloquear casa paga: R$4,00  
Buzinas pagas: R$5,00  
Sirene em todos os carros: R$4,00  
King: R$3,50  
Nome RGB: R$2,00  

📲 *Pagamento via Pix*  
Chave Pix: 79999598533
"""
    update.message.reply_text(tabela, parse_mode='Markdown')

# Substitua "7574937721:AAH8uxU-T95ChxUy2_fLiOmkHtDjXlKCzHw" pelo token do seu bot
updater = Updater("7574937721:AAH8uxU-T95ChxUy2_fLiOmkHtDjXlKCzHw", use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("produtos", produtos))

updater.start_polling()
updater.idle()
