# -*- coding: utf-8 -*-

# Script para lidar com datas
# Autor: Lucas V. de Jesus

import datetime
import os
from mensagens import log_info, log_error

# Verifica se o ano é bissexto
def ano_bissexo(ano):
	return(ano % 4 == 0)

# Valida a data fornecida
def validar_data(dia, mes, ano):
	meses_30_dias = [4,6,9,11]
	meses_31_dias = [1,3,5,7,9,12]

	valido = True

	if dia < 1 or mes < 1 or ano < 1 or mes > 12 or dia > 31:
		return False

	for m in meses_31_dias:
		if mes == m:
			if dia > 31:
				valido = False
	
	if mes == 2:
		if ano_bissexo(ano):
			valido = dia < 30 and dia > 0
		else:
			valido = dia < 29 and dia > 0

	for m in meses_30_dias:
		if mes == m:
			if dia > 30:
				valido = False

	return valido

# Gera uma wordlist com o formato de data
def gerar_datas(start_day, start_month, start_year, file_datas):
	log_info( 'Gerando datas ...' )

	try:
		file = open(file_datas, 'w' )
	except Exception:
		log_error( 'Falha ao abrir o arquivo %s no modo escrita' % file_datas)
		quit(1)
	
	current_year = datetime.datetime.now().year 

	for y in range(start_year, current_year + 1):
		for m in range(start_month, 13):
			for d in range(start_day, 32):
				file.write( '%02d%02d%04d\n' % (d, m ,y))

	file.close()