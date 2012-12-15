from django import template
from math import modf

register = template.Library()

@register.filter
def distanceformat(distance):
	"""
	Formats the variable of distance 
	"""
	rounded = float('%.2g' % distance)
	m, k = modf(rounded / 1000.0)
	if k:
		return '%g km' % k + m
	else:
		return '%g m' % rounded
