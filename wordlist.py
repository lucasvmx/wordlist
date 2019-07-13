# -*- coding: utf-8 -*-

# Script para gerar wordlists
# Autor: Lucas Vieira, Elyakim Klettke Brito
# Testado no python 3.7.1 64-bit
# Este é o arquivo principal

# Telefones móveis: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=330
# Telefones Fixos: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=331 

import sys
import datetime
import os
from phones import *
from messages import *
from dates import *
from usage import *
from mac import *

# Função principal do programa
def main():
	if sys.version_info < (3,0):
		print_red( 'This script requires python 3')
		quit(1)

	arg_count = len(sys.argv)
	
	if arg_count < 2:
		show_usage(sys.argv[0])

	# Analisa os argumentos da linha de comando
	i = 0
	
	# Flags
	generate_phones = False
	generate_mac = False
	generate_date = False


	start_date = "" # Data de início
	phone_prefix = 62 # Prefixo do número de telefone (Padrão é 61)

	for arg in sys.argv:
		if arg == options[0]:
			# Gerar numero de telefone
			generate_phones = True
			phone_prefix = int(sys.argv[i + 1])
		elif arg == options[1]:
			# Gerar endereços MAC
			generate_mac = True
		elif arg == options[2]:
			# Gerar datas e o próximo argumento é a data
			generate_date = True
			start_date = str(sys.argv[i + 1]).split("/")

		i = i + 1
			
	# Fazer as operações
	try:
		if generate_phones:
			phones = PhoneNumbers()
			phones.generate_phone_numbers(phone_prefix)

		if generate_date:
			day = int(start_date[0])
			month = int(start_date[1])
			year = int(start_date[2])

			generate_dates(day, month, year)

		if generate_mac:
			mac = MacAddress()
			mac.generate_mac(0, 281474976710655)
	except KeyboardInterrupt:
		print( 'Stopping ...')

if __name__ == "__main__":
	main()

