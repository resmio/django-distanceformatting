from django import template
from math import modf

register = template.Library()

@register.filter
def distanceformat(distance):
	"""
	Formats the variable of distance 
	"""
	if distance < 100:
		return '%.0f m' % distance
	elif distance < 1000:
		return '%.0f m' % round(distance, -1)
	else:
		m, k = modf(distance / 1000.0)
		if m < 0.1:
			return '%.0f km' % k
		else:
			return '%.1f km' % k + round(m, 1)
