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
		log_error( 'This script requires python 3.x ')
		quit(1)
	
	# arg_count = len(sys.argv)
	show_usage(sys.argv[0])

	# Analisa os argumentos da linha de comando
	i = 0

	# Flags
	generate_phones = False
	generate_mac = False
	generate_dates = False


	start_date = "" # Data de início
	phone_prefix = 62 # Prefixo do número de telefone (Padrão é 61)

	for arg in sys.argv:
		if arg == options[0]:
			# Gerar numero de telefone
			generate_phones = True

			# TODO: implementar a leitura do prefixo

		elif arg == options[1]:
			# Gerar endereços MAC
			generate_mac = True
		elif arg == options[2]:
			# Gerar datas e o próximo argumento é a data
			generate_dates = True
			start_date = sys.argv[i + 1]

		i = i + 1
			
	# Fazer as operações
	if generate_phones:
		phones = PhoneNumbers()
		phones.generate_phone_numbers(phone_prefix)

	if generate_dates:
		print("Date generation not implemented yet")
	
	if generate_mac:
		mac = MacAddress()
		mac.generate_mac(0, 281474976710655)

if __name__ == "__main__":
	main()

