from django import template
from blogweb.models import * 
register = template.Library()
@register.inclusion_tag("blogweb/tags/service.html")

def tags_service():
	data=Services.objects.order_by("-id").all()
	return {'data':data}
@register.inclusion_tag("blogweb/tags/partner.html")
def tags_partner():
	data=Partners.objects.order_by("-id").all()
	return {'data':data}
@register.inclusion_tag("blogweb/tags/product.html")
def products_list():
	data=Products.objects.order_by("-id").all()
	return {'data':data}

@register.inclusion_tag("blogweb/tags/slider.html")
def sliders_list():
	data=Sliders.objects.order_by("-id").all()
	return {'data':data}
@register.inclusion_tag("blogweb/tags/homeservice.html")
def homeservices_list():
	data=Homeservices.objects.order_by("-id").all()
	return {'data':data}
