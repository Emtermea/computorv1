# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solve.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emtermea <emtermea@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/08/19 17:38:17 by emtermea          #+#    #+#              #
#    Updated: 2015/08/19 17:38:21 by emtermea         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-

import time
from functionCalcul import *

def solve_one(prout):
	print "La solution reelle est :"
	if len(prout) == 2:
		print -prout[0]/prout[1]
	else:
		print "0"

def solve_zero(prout):
	if prout[0] == 0:
		print "Tous les nombres reels sont solution"
	else:
		#rouge
		print "\033[31mImpossible\033[0m"

def solve_two(prout):
	a = prout[2]
	try:
		b = prout[1]
	except:
		b = 0
	try:
		c = prout[0]
	except:
		c = 0
	delta = b**2 - 4*a*c
	if delta == 0:
		x = -b/(2*a)
		print "Le discriminant est nul "
		print "La solution reelle est :"
		print x
	elif delta > 0:
		#vert
		print "Le discriminant est \033[32mpositif\033[0m :", delta
		print "Les solutions \033[32mreelles\033[0m sont :"
		x1 = (-b + racine(delta))/(2*a)
		x2 = (-b - racine(delta))/(2*a)
		print x1
		print x2
	elif delta < 0:
		#cyan
		print "Le discriminant est \033[36mnegatif\033[0m :", delta
		print "Les solutions \033[36mcomplexes\033[0m sont :"
		print "(", -b, "- i *", racine(absolut(delta)), ") /", 2*a
		print "(", -b, "+ i *", racine(absolut(delta)), ") /", 2*a

#print en rose 

def solve(degre_max, prout):
	if degre_max > 2:
		#rose
		print "\033[35mResolution en cours\033[0m"
		time.sleep(4)
		print "\n\033[35mOh le polynome est superieur a deux... C'est plus complique\033[0m"
		time.sleep(3)
		print "\n\033[35mAh je ne sais pas le faire, desole\033[0m"
	elif degre_max == 2:
		solve_two(prout)
	elif degre_max == 1:
		solve_one(prout)
	elif degre_max == 0:
		solve_zero(prout)

