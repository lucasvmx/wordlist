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
from phones import PhoneNumbers
from messages import log_error
from dates import validar_data, gerar_datas
from usage import *
from getopt import getopt
from mac import MacAddress

QUANTIDADE_MAX_ARGUMENTOS = 10
QUANTIDADE_MIN_ARGUMENTOS = 2

# Função principal do programa
def main():
	if sys.version_info < (3,0):
		log_error( 'Este script requer o python 3.x ')
		quit(1)

	MacAddress.number_to_mac_address(2, 848481292822)

	qtd_argumentos = len(sys.argv)

	if qtd_argumentos > QUANTIDADE_MAX_ARGUMENTOS or qtd_argumentos < QUANTIDADE_MIN_ARGUMENTOS:
		show_usage(sys.argv[0])
		exit(1)

if __name__ == "__main__":
	main()

