# -*- coding: utf-8 -*-

# Gerador de números de telefone aleatórios'''
# Autor: Elyakim Klettke Brito

class PhoneNumbers:

	def validate_prefix(self, num):
		if num < 10 or num > 99:
			return False
		
		return True

	# Gera todos os números de telefone possíveis a partir de um prefixo
	def generate_phone_numbers(self, prefix):
		
		# Valida o prefixo
		if not self.validate_prefix(prefix):
			return False
		
		nove = 9

		if prefix == 0:
			for x in range(70000000, 99999999):
				print("%08d\n" % x)
		else:
			for x in range(0, 10000000):
				print("%d%d%06d\n" % (nove,prefix,x))
		
		return True

if __name__ == "__main__":
	print( 'This script should not run directly')


