# -*- coding: utf-8 -*-

# Gerador de números de telefone aleatórios'''
# Autor: Elyakim Klettke Brito

class PhoneNumbers:

	def validate_prefix(self, num):
		if num < 10 or num > 99:
			return False
		
		return True

	# Gera todos os números de telefone possíveis a partir de um prefixo
	def generate_phone_numbers(self, prefixo):
		
		# Valida o prefixo
		if not self.validar_prefixo(prefixo):
			return False
		
		nove = 9

		for x in range(0, 10000000):
			print("%d%d%06d\n" % (nove,prefixo,x))

		return True



