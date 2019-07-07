# -*- coding: utf-8 -*-

# Script que contém definições de uso do programa

options = [ "-p", "-m", "-d" ]

options_str = "%s <prefix>: generate phone numbers\n" % options[0]
options_str += "%s: generate mac address\n" % options[1]
options_str += "%s <dd/mm/yyyy>: generate dates starting from the specified date\n\n" % options[2]

def show_usage(nome_script):
	print( 'Usage: %s <options>' % nome_script)
	print( '\nPossible options:' )
	print(options_str)
	

