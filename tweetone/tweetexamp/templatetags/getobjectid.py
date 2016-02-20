from django import template

register = template.Library()
# since _id is not to be used in the Django framework html pages, create a filter to get the value
@register.filter("mongo_id")
def mongo_id(value):
	return str(value['_id'])
	
