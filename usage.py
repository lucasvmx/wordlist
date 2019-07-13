# -*- coding: utf-8 -*-

# Script que contém definições de uso do programa

from messages import *

options = [ "-p", "-m", "-d" ]

def show_usage(nome_script):

	options_str = '''\x1b[1;33m%s\x1b[0m <prefix>: generate phone numbers (0 to generate without prefix)
\x1b[1;33m%s\x1b[0m: generate mac address
\x1b[1;33m%s\x1b[0m <dd/mm/yyyy>: generate dates starting from the specified date\n 
Usage example: \x1b[35;1mpython3 %s -m\x1b[0m\n''' % (options[0], options[1], options[2], nome_script)

	print_green( 'Usage: %s <options>' % nome_script)
	print( '\nPossible options:' )
	print(options_str)
	
if __name__ == "__main__":
	print( 'This script should not run directly')
