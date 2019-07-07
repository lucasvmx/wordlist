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
	
	qtd_argumentos = len(sys.argv)	
	show_usage(sys.argv[0])

if __name__ == "__main__":
	main()

