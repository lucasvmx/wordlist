# -*- coding: utf-8 -*-

# Script que contém definições de uso do programa

options_str = "-p: generate phone numbers\n"
options_str += "-m: generate mac address\n"
options_str += "-d <dd/mm/yyyy>: generate dates starting from the specified date\n\n"

def show_usage(nome_script):
	print( 'Usage: %s <options>' % nome_script)
	print( '\nPossible options:' )
	print(options_str)
	

