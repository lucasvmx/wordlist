# -*- coding: utf-8 -*-

# Script para gerar wordlists
# Autor: Lucas Vieira
# Testado no python 3.7.1 64-bit

import sys
import datetime
import os

# Telefones móveis: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=330
# Telefones Fixos: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=331

if sys.version_info < (3,0):
	print( 'Este script requer o python 3.x ')
	quit(1)
	
current_year = datetime.datetime.now().year

argumento_datas = '--datas'
argumento_fixo = '--fixo'
argumento_celular = '--celular'

file_telefone_fixo = 'telefone-fixo.dat'
file_celular = 'telefone-movel.dat'
file_datas = 'datas.dat'

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

def ano_bissexo(ano):
	return(ano % 4 == 0)

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

# Gera uma wordlist para telefones fixos do DF
def generate_fixed_phone_wordlist():
	print( 'Gerando wordlist com telefones fixos ...')

	try:
		file = open( file_telefone_fixo, 'w' )
	except Exception:
		log_error( 'Falha ao abrir o arquivo %s no modo escrita' % file_telefone_fixo)
		quit(1)

	p1 = 2000
	p2 = 3000
	p3 = 4000
	p4 = 5000

	# Numeros no formato 2XXX-XXXX
	log_info( 'Gerando numeros no formato: 2XXX-XXXX ...' )

	for n1 in range(p1,3000):
		for n2 in range(0,10000):
			file.write( '%04d%04d\n' % (n1, n2))

	# Numeros no formato 3XXX-XXXX
	log_info( 'Gerando numeros no formato: 3XXX-XXXX ...' )
	for n1 in range(p2,4000):
		for n2 in range(0,10000):
			file.write( '%04d%04d\n' % (n1, n2))

	# Numeros no formato 4XXX-XXXX
	log_info( 'Gerando numeros no formato: 4XXX-XXXX ...' )
	for n1 in range(p3,5000):
		for n2 in range(0,10000):
			file.write( '%04d%04d\n' % (n1, n2))

	# Numeros no formato 5XXX-XXXX
	log_info( 'Gerando numeros no formato: 5XXX-XXXX ...' )
	for n1 in range(p4,6000):
		for n2 in range(0,10000):
			file.write( '%04d%04d\n' % (n1, n2))

	file.close()

# Gera uma wordlist para telefones móveis
def generate_mobile_phone_wordlist():
	log_info( 'Gerando numeros de celular ...')

	try:
		file = open( file_celular, 'w')
	except Exception:
		log_error( 'Falha ao abrir o arquivo %s no modo escrita' % file_telefone_fixo)
		quit(1)

	p1 = 8000
	p2 = 0

	log_info( 'Gerando numeros no formato: 98XXX-XXXX ...')
	# Números no formato 98XXX-XXXX
	for n1 in range(p1,9000):
		for n2 in range(p2, 10000):
			file.write( '9%04d%04d\n' % (n1, n2))

	p1 = 9000

	log_info( 'Gerando numeros no formato: 99XXX-XXXX ...')

	# Números no formato 99XXX-XXXX
	for n1 in range(p1,10000):
		for n2 in range(p2, 10000):
			file.write( '9%04d%04d\n' % (n1,n2))

	p1 = 7000

	log_info( 'Gerando numeros no formato: 97XXX-XXXX ...')
	# Números no formato 97XXX-XXXX
	for n1 in range(p1,8000):
		for n2 in range(p2, 10000):
			file.write( '9%04d%04d\n' % (n1,n2))

	file.close()

# Gera uma wordlist com o formato de data
def generate_dates(start_day, start_month, start_year):
	log_info( 'Gerando datas ...' )

	try:
		file = open( file_datas, 'w' )
	except Exception:
		log_error( 'Falha ao abrir o arquivo %s no modo escrita' % file_telefone_fixo)
		quit(1)

	for y in range(start_year, current_year + 1):
		for m in range(start_month, 13):
			for d in range(start_day, 32):
				file.write( '%02d%02d%04d\n' % (d, m ,y))

	file.close()

def uso(nome_script):
	print( 'Uso: %s <opcao>\n' % nome_script)
	print( 'Possíveis valores para o parâmetro opcao:')
	print( '\t%s\tGera uma wordlist contendo numeros de celular do Brasil' % argumento_celular)
	print( '\t%s\tGera uma wordlist contendo numeros de telefone fixo do Brasil' % argumento_fixo)
	print( '\t%s\tGera uma wordlist contendo datas no format dd:mm:yy\n' % argumento_datas)
	print( 'Exemplo: %s --celular --fixo\n' % nome_script)

# Processando os argumentos da linha de comando ...

datas = False
celular = False
fixo = False

qtd_argumentos = len(sys.argv)
sistema_operacional = os.name

if qtd_argumentos != 2 and qtd_argumentos != 3 and qtd_argumentos != 4:
	uso(sys.argv[0])
	quit(1)

for j in range(1,qtd_argumentos):
	if sys.argv[j] == argumento_celular:
		celular = True
		continue
	elif sys.argv[j] == argumento_datas:
		datas = True
		continue
	elif sys.argv[j] == argumento_fixo:
		fixo = True
		continue
	else:
		continue

if datas:
	try:
		print( 'Digite a data de inicio no formato dd/mm/yy: ')
		data_inicio = str(sys.stdin.readline())
		data = data_inicio.split('/')

		dia_inicio = int(data[0])
		mes_inicio = int(data[1])
		ano_inicio = int(data[2])

		if not(validar_data(dia_inicio,mes_inicio,ano_inicio)):
			log_error( 'Data invalida' )
			quit(1)
		else:
			log_info( 'Gerando datas a partir de %02d/%02d/%02d ...' % (dia_inicio, mes_inicio, ano_inicio))
			generate_dates(dia_inicio, mes_inicio, ano_inicio)
	except KeyboardInterrupt:
		log_alert( '\nScript interrompido' )
		os.remove(file_datas)
	
if celular:
	try:
		generate_mobile_phone_wordlist()
	except KeyboardInterrupt:
		log_alert( '\nScript interrompido ')
		os.remove(file_celular)

if fixo:
	try:
		generate_fixed_phone_wordlist()
	except KeyboardInterrupt:
		log_alert( '\nScript interrompido' )
		os.remove(file_telefone_fixo)

log_ok('Programa finalizado')