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
/surgery
/american_journal_of_surgery
/journal_of_surgical_research
/journal_of_pediatric_surgery

Sub-specialty Surgical Journals:

CTVS
/journal_of_vascular_surgery

Neurosurgery
/jnnp
/world_neurosurgery
/interdisciplinary_neurosurgery
/clinical_neurology_and_neurosurgery

Hepato-Pancreato-Biliary
/annals_of_hepato_pancreato_biliary

Orthopedics
/clinical_orthopedics_trauma

Transplant 
/transplantation_reviews
/transplantation_reports
/transplant_immunology

''')

@bot.message_handler(commands=['jama_surgery'])
def send_JAMA_Surgery(message):
	JAMA_Surgery = jama.section()
	def JAMA_Surgery_string(JAMA_Surgery):
	    JAMA_Surgery_str = ""
	    return JAMA_Surgery_str.join(JAMA_Surgery)
	bot.reply_to(message, "Here are the latest articles from JAMA Surgery:" + """

""" + JAMA_Surgery_string(JAMA_Surgery))
	
@bot.message_handler(commands=['surgery'])
def send_Surgery(message):
	Surgery = articles.Sci.site(articles.Surgery)
	def Surgery_string(Surgery):
	    Surgery_str = ""
	    return Surgery_str.join(Surgery)
	bot.reply_to(message, "Here are the latest articles from Surgery:" + """

""" + Surgery_string(Surgery))

@bot.message_handler(commands=['american_journal_of_surgery'])
def send_American_Journal_of_Surgery(message):
	American_Journal_of_Surgery = articles.Sci.site(articles.American_Journal_of_Surgery)
	def American_Journal_of_Surgery_string(American_Journal_of_Surgery):
	    American_Journal_of_Surgery_str = ""
	    return American_Journal_of_Surgery_str.join(American_Journal_of_Surgery)
	bot.reply_to(message, "Here are the latest articles from the American Journal of Surgery:" + """

""" + American_Journal_of_Surgery_string(American_Journal_of_Surgery))
	
@bot.message_handler(commands=['journal_of_surgical_research'])
def send_Journal_of_Surgical_Research(message):
	Journal_of_Surgical_Research = articles.Sci.site(articles.Journal_of_Surgical_Research)
	def Journal_of_Surgical_Research_string(Journal_of_Surgical_Research):
	    Journal_of_Surgical_Research_str = ""
	    return Journal_of_Surgical_Research_str.join(Journal_of_Surgical_Research)
	bot.reply_to(message, "Here are the latest articles from the Journal of Surgical Research:" + """

""" + Journal_of_Surgical_Research_string(Journal_of_Surgical_Research))

@bot.message_handler(commands=['journal_of_pediatric_surgery'])
def send_Journal_of_Pediatric_Surgery(message):
	Journal_of_Pediatric_Surgery = articles.Sci.site(articles.Journal_of_Pediatric_Surgery)
	def Journal_of_Pediatric_Surgery_string(Journal_of_Pediatric_Surgery):
	    Journal_of_Pediatric_Surgery_str = ""
	    return Journal_of_Pediatric_Surgery_str.join(Journal_of_Pediatric_Surgery)
	bot.reply_to(message, "Here are the latest articles from the Journal of Pediatric Surgery:" + """

""" + Journal_of_Pediatric_Surgery_string(Journal_of_Pediatric_Surgery))
	
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

@bot.message_handler(commands=['interdisciplinary_neurosurgery'])
def send_Interdisciplinary_Neurosurgery(message):
	Interdisciplinary_Neurosurgery = articles.Sci.site(articles.Interdisciplinary_Neurosurgery)
	def Interdisciplinary_Neurosurgery_string(Interdisciplinary_Neurosurgery):
	    Interdisciplinary_Neurosurgery_str = ""
	    return Interdisciplinary_Neurosurgery_str.join(Interdisciplinary_Neurosurgery)
	bot.reply_to(message, "Here are the latest articles from Interdisciplinary Neurosurgery:" + """

""" + Interdisciplinary_Neurosurgery_string(Interdisciplinary_Neurosurgery))	
	
@bot.message_handler(commands=['annals_of_hepato_pancreato_biliary'])
def send_Annals_of_Hepato_Pancreato_Biliary_Surgery(message):
	Annals_of_Hepato_Pancreato_Biliary_Surgery = base.Sci.site(base.Annals_of_Hepato_Pancreato_Biliary_Surgery)
	def Annals_of_Hepato_Pancreato_Biliary_Surgery_string(Annals_of_Hepato_Pancreato_Biliary_Surgery):
	    Annals_of_Hepato_Pancreato_Biliary_Surgery_str = ""
	    return Annals_of_Hepato_Pancreato_Biliary_Surgery_str.join(Annals_of_Hepato_Pancreato_Biliary_Surgery)
	bot.reply_to(message, "Here are the latest articles from Annals of Hepato-Pancreato-Biliary Surgery:" + """

""" + Annals_of_Hepato_Pancreato_Biliary_Surgery_string(Annals_of_Hepato_Pancreato_Biliary_Surgery))

@bot.message_handler(commands=['clinical_neurology_and_neurosurgery'])
def send_Clinical_Neurology_and_Neurosurgery(message):
	Clinical_Neurology_and_Neurosurgery = articles.Sci.site(articles.Clinical_Neurology_and_Neurosurgery)
	def Clinical_Neurology_and_Neurosurgery_string(Clinical_Neurology_and_Neurosurgery):
	    Clinical_Neurology_and_Neurosurgery_str = ""
	    return Clinical_Neurology_and_Neurosurgery_str.join(Clinical_Neurology_and_Neurosurgery)
	bot.reply_to(message, "Here are the latest articles from the Journal of Clinical Neurology and Neurosurgery:" + """

""" + Clinical_Neurology_and_Neurosurgery_string(Clinical_Neurology_and_Neurosurgery))
	
@bot.message_handler(commands=['clinical_orthopedics_trauma'])
def send_Clinical_Orthopedics_and_Trauma(message):
	Clinical_Orthopedics_and_Trauma = articles.Sci.site(articles.Clinical_Orthopedics_and_Trauma)
	def Clinical_Orthopedics_and_Trauma_string(Clinical_Orthopedics_and_Trauma):
	    Clinical_Orthopedics_and_Trauma_str = ""
	    return Clinical_Orthopedics_and_Trauma_str.join(Clinical_Orthopedics_and_Trauma)
	bot.reply_to(message, "Here are the latest articles from World_Neurosurgery:" + """

""" + Clinical_Orthopedics_and_Trauma_string(Clinical_Orthopedics_and_Trauma))

@bot.message_handler(commands=['transplantation_reviews'])
def send_Transplantation_Reviews(message):
	Transplantation_Reviews = articles.Sci.site(articles.Transplantation_Reviews)
	def Transplantation_Reviews_string(Transplantation_Reviews):
	    Transplantation_Reviews_str = ""
	    return Transplantation_Reviews_str.join(Transplantation_Reviews)
	bot.reply_to(message, "Here are the latest articles from Transplantation Reviews:" + """

""" + Transplantation_Reviews_string(Transplantation_Reviews))

@bot.message_handler(commands=['transplantation_reports'])
def send_Transplantation_Reports(message):
	Transplantation_Reports = articles.Sci.site(articles.Transplantation_Reports)
	def Transplantation_Reports_string(Transplantation_Reports):
	    Transplantation_Reports_str = ""
	    return Transplantation_Reports_str.join(Transplantation_Reports)
	bot.reply_to(message, "Here are the latest articles from Transplantation Reports:" + """

""" + Transplantation_Reports_string(Transplantation_Reports))

@bot.message_handler(commands=['transplant_immunology'])
def send_Transplant_Immunology(message):
	Transplant_Immunology = articles.Sci.site(articles.Transplant_Immunology)
	def Transplant_Immunology_string(Transplant_Immunology):
	    Transplant_Immunology_str = ""
	    return Transplant_Immunology_str.join(Transplant_Immunology)
	bot.reply_to(message, "Here are the latest articles from Transplant Immunology:" + """

""" + Transplant_Immunology_string(Transplant_Immunology))

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
