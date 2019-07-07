# -*- coding: utf-8 -*-

# Script para lidar com datas
# Autor: Lucas V. de Jesus

import datetime
import os
from messages import log_info, log_error

# Verifica se o ano é bissexto
def is_leap_year(ano):
	return(ano % 4 == 0)

# Valida a data fornecida. Retorna True se a data for válida
# Ou False se a data for inválida
def is_valid_date(dia, mes, ano):
	thirty_days_months = [4,6,9,11] # Lista de meses com 30 dias
	thirty_one_days_months = [1,3,5,7,9,12] # Lista de meses com 31 dias

	is_valid = True
	
	if dia < 1 or mes < 1 or ano < 1 or mes > 12 or dia > 31:
		return False

	for m in thirty_one_days_months:
		if mes == m:
			if dia > 31:
				is_valid = False
	
	if mes == 2:
		if is_leap_year(ano):
			is_valid = dia < 30 and dia > 0
		else:
			is_valid = dia < 29 and dia > 0

	for m in thirty_days_months:
		if mes == m:
			if dia > 30:
				is_valid = False

	return is_valid

# Gera uma wordlist com o formato de data
def generate_dates(start_day, start_month, start_year):
	current_year = datetime.datetime.now().year 

	for y in range(start_year, current_year + 1):
		for m in range(start_month, 13):
			for d in range(start_day, 32):
				print( '%02d%02d%04d\n' % (d, m ,y))