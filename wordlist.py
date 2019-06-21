# -*- coding: utf-8 -*-

# Script para gerar wordlists
# Autor: Lucas Vieira, Elyakim Klettke Brito
# Testado no python 3.7.1 64-bit

import sys
import datetime
import os
from telefones import NumerosDeTelefone
from mensagens import log_error
from datas import validar_data, gerar_datas
from uso import uso

QUANTIDADE_MAX_ARGUMENTOS = 10
QUANTIDADE_MIN_ARGUMENTOS = 2

# Telefones móveis: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=330
# Telefones Fixos: http://www.anatel.gov.br/setorregulado/plano-de-numeracao-brasileiro?id=331 

qtd_argumentos = len(sys.argv)

if sys.version_info < (3,0):
	log_error( 'Este script requer o python 3.x ')
	quit(1)

if qtd_argumentos > QUANTIDADE_MAX_ARGUMENTOS or qtd_argumentos < QUANTIDADE_MIN_ARGUMENTOS:
	uso(sys.argv[0])
	exit(1)