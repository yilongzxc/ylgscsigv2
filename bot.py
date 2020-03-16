import time
import telebot
import articles
import base
import jama

bot_token = "938245208:AAFLUILk5hlKH74eKLfG6uHW7zQ72flUkaI"
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Welcome to the GS CSIG bot! Enter /help to get started!')

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, '''Click or type out the commands to get the latest journal updates! Access the articles for free via the NUS Libraries Proxy Bookmarklet.

General Surgical Journals:
/jama_surgery

Specialised Surgical Journals:

CTVS
/journal_of_vascular_surgery

Neurosurgery
/jnnp
/world_neurosurgery

Hepato-Pancreato-Biliary
/hepato_pancreato_biliary

Orthopedics
/clinical_orthopedics_trauma
''')

@bot.message_handler(commands=['jama_surgery'])
def send_JAMA_Surgery(message):
	JAMA_Surgery = jama.section()
	def JAMA_Surgery_string(JAMA_Surgery):
	    JAMA_Surgery_str = ""
	    return JAMA_Surgery_str.join(JAMA_Surgery)
	bot.reply_to(message, "Here are the latest articles from JAMA Surgery:" + """

""" + JAMA_Surgery_string(JAMA_Surgery))

@bot.message_handler(commands=['journal_of_vascular_surgery'])
def send_Journal_of_Vascular_Surgery(message):
	Journal_of_Vascular_Surgery = articles.Sci.site(articles.Journal_of_Vascular_Surgery)
	def Journal_of_Vascular_Surgery_string(Journal_of_Vascular_Surgery):
	    Journal_of_Vascular_Surgery_str = ""
	    return Journal_of_Vascular_Surgery_str.join(Journal_of_Vascular_Surgery)
	bot.reply_to(message, "Here are the latest articles from Journal of Vascular Surgery:" + """

""" + Journal_of_Vascular_Surgery_string(Journal_of_Vascular_Surgery))

@bot.message_handler(commands=['jnnp'])
def send_Journal_of_Neurology_Neurosurgery_and_Psychiatry(message):
	Journal_of_Neurology_Neurosurgery_and_Psychiatry = base.Sci.site(base.Journal_of_Neurology_Neurosurgery_and_Psychiatry)
	def Journal_of_Neurology_Neurosurgery_and_Psychiatry_string(Journal_of_Neurology_Neurosurgery_and_Psychiatry):
	    Journal_of_Neurology_Neurosurgery_and_Psychiatry_str = ""
	    return Journal_of_Neurology_Neurosurgery_and_Psychiatry_str.join(Journal_of_Neurology_Neurosurgery_and_Psychiatry)
	bot.reply_to(message, "Here are the latest articles from Journal of Neurology Neurosurgery and Psychiatry:" + """

""" + Journal_of_Neurology_Neurosurgery_and_Psychiatry_string(Journal_of_Neurology_Neurosurgery_and_Psychiatry))

@bot.message_handler(commands=['world_neurosurgery'])
def send_World_Neurosurgery(message):
	World_Neurosurgery = articles.Sci.site(articles.World_Neurosurgery)
	def World_Neurosurgery_string(World_Neurosurgery):
	    World_Neurosurgery_str = ""
	    return World_Neurosurgery_str.join(World_Neurosurgery)
	bot.reply_to(message, "Here are the latest articles from World_Neurosurgery:" + """

""" + World_Neurosurgery_string(World_Neurosurgery))

@bot.message_handler(commands=['hepato_pancreato_biliary'])
def send_Annals_of_Hepato_Pancreato_Biliary_Surgery(message):
	Annals_of_Hepato_Pancreato_Biliary_Surgery = base.Sci.site(base.Annals_of_Hepato_Pancreato_Biliary_Surgery)
	def Annals_of_Hepato_Pancreato_Biliary_Surgery_string(Annals_of_Hepato_Pancreato_Biliary_Surgery):
	    Annals_of_Hepato_Pancreato_Biliary_Surgery_str = ""
	    return Annals_of_Hepato_Pancreato_Biliary_Surgery_str.join(Annals_of_Hepato_Pancreato_Biliary_Surgery)
	bot.reply_to(message, "Here are the latest articles from Annals_of_Hepato_Pancreato_Biliary_Surgery:" + """

""" + Annals_of_Hepato_Pancreato_Biliary_Surgery_string(Annals_of_Hepato_Pancreato_Biliary_Surgery))

@bot.message_handler(commands=['clinical_orthopedics_trauma'])
def send_Clinical_Orthopedics_and_Trauma(message):
	Clinical_Orthopedics_and_Trauma = articles.Sci.site(articles.Clinical_Orthopedics_and_Trauma)
	def Clinical_Orthopedics_and_Trauma_string(Clinical_Orthopedics_and_Trauma):
	    Clinical_Orthopedics_and_Trauma_str = ""
	    return Clinical_Orthopedics_and_Trauma_str.join(Clinical_Orthopedics_and_Trauma)
	bot.reply_to(message, "Here are the latest articles from World_Neurosurgery:" + """

""" + Clinical_Orthopedics_and_Trauma_string(Clinical_Orthopedics_and_Trauma))

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
