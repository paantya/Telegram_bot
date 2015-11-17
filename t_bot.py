#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
from time import sleep

import token_lib
bool_disable_web_page_preview = 1

def send_Message(text_message, bool_disable_web_page_preview):
	bot.sendMessage(chat_id=token_lib.chat__id,text=text_message , disable_web_page_preview = bool_disable_web_page_preview)
	sleep(1)

if __name__ == '__main__':
	bot = telegram.Bot(token_lib.telegram_token)
	bot.sendPhoto(chat_id=token_lib.chat__id,,caption = 'П')
	#while (True):
		try:
			print ('Функция началась')
			sleep(5)
		except:
			print('Произошла какая-то ошибка!')
		else:
			print('Всё хорошо.')
		finally:
			print ('Цикл завершён.')