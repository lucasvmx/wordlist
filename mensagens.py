# -*- coding: utf-8 -*-

# Funções para imprimir mensagens organizadas na tela

import os

def log_error(text):
	if os.name != 'nt':
		fmt = '\x1b[1;31m[!]\x1b[0m '
		print(fmt + text)
	else:
		print(text)

def log_ok(text):
	if os.name != 'nt':
		fmt = '\x1b[1;32m[+]\x1b[0m '
		print(fmt + text)
	else:
		print(text)

def log_alert(text):
	if os.name != 'nt':
		fmt = '\x1b[1;33m[!]\x1b[0m '
		print(fmt + text)
	else:
		print(text)

def log_info(text):
	if os.name != 'nt':
		fmt = '\x1b[1;34m[*]\x1b[0m '
		print(fmt + text)
	else:
		print(text)