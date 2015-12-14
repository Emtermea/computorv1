# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    moreFunctions.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emtermea <emtermea@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/19 01:49:40 by emtermea          #+#    #+#              #
#    Updated: 2015/08/19 01:49:42 by emtermea         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
# -*- coding: utf-8 -*-

import sys
import re

def check_degre_max(A):
	degre_max = 0
	i = 0
	while i < len(A):
		if int(re.search("[0-9]+$", A[i]).group(0)) > degre_max:
			degre_max = int(re.search("[0-9]+$", A[i]).group(0))
		i += 1
	return degre_max

#checker gestion d'erreur --> lettres
def check_letter_in_tab(tab):
	taille = len(tab)
	while taille:
		if re.search("[^\+\=\-\*\.\^Xx0-9]", tab):
			#jaune
			print "\033[33mFormat invalide\033[0m : caractere(s) non valide(s)"
			sys.exit(2)
		taille -= 1

def check_right_format_between_operator(tab):
	tmp = re.split('[\-\+]', tab)
	tmp.pop(0)
	i = 0
	while i < len(tmp):
		if (not (re.search("^([0-9]+\.[0-9]+|[0-9]+)(\*)?[xX]\^[0-9]+$", tmp[i]))) and (not (tmp[i] == '0')):
			#jaune
			print "\033[33mFormat invalide\033[0m"
			sys.exit(4)
		i += 1

def gestion_erreur(tab):
	check_letter_in_tab(tab[0])
	check_letter_in_tab(tab[1])
	check_right_format_between_operator(tab[0])
	check_right_format_between_operator(tab[1])

