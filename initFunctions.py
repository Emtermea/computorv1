# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    initFunctions.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emtermea <emtermea@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/19 16:24:11 by emtermea          #+#    #+#              #
#    Updated: 2015/08/19 16:24:15 by emtermea         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def equ_init_split(equ_init):
	tab = equ_init.split('=')
	if len(tab) != 2:
		#jaune
		print "\033[33mFormat invalide\033[0m : probleme avec '=' dans la string"
		sys.exit(1)
	return tab

def change_signe_and_push(A, B):	
	i = 0
	while i < len(B):
		if B[i][0] == '-':
			B[i] = "+" + B[i][1:]
		elif B[i][0] == '+':
			B[i] = "-" + B[i][1:]
		A.append(B[i])
		i += 1
	return A

def add_sign(tab):
	if (tab[0][0] != '+' and tab[0][0] != '-'):
		tab[0] = "+" + tab[0]
	if (tab[1][0] != '+' and tab[1][0] != '-'):
		tab[1] = "+" + tab[1]