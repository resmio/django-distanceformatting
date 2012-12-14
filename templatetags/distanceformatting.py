from django import template
from math import modf

register = template.Library()

@register.filter
def distanceformat(distance):
	"""
	Formats the variable of distance 
	"""
	if distance < 100:
		return '%.0f m (%d)' % (distance, distance)
	elif distance < 1000:
		return '%.0f m (%d)' % (round(distance, -1), distance)
	else:
		m, k = modf(distance / 1000.0)
		if m < 0.1:
			return '%.0f km (%d)' % (k, distance)
		else:
			return '%.1f km (%d)' % (k + round(m, 1), distance)