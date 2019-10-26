from .autoload import *
def add_product(request):
	return render(request,'adminpanel/add-product.html',{})
def edit_product(request,id):
	data=Products.objects.filter(id=id).first()
	data ={'id':data.id,'title':data.title,'page_banner':data.image,'status':data.status,'description':data.description}
	return render(request,'adminpanel/edit-product.html',{'data':data})
def products_list(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect("/")	
	per_page = configuration('admin_record_per_page_pages')
	if per_page is None:
		per_page = configuration('admin_record_per_page')
	defaultsort='-id'
	pageslist = Products.objects.order_by(defaultsort).all()
	paginator = Paginator(pageslist, per_page)
	page = 1
	if request.GET.get("page") is not None:
		page = request.GET.get("page")
	pageslist = paginator.get_page(page)
	return render(request,'adminpanel/products.html',{'datalist':pageslist})
def delete_product(request,id):
	data=Products.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect('/dj-admin/products')
def submit_product(request):
	data = request.POST
	Products.objects.create(title=data.get('title'),image=data.get('page_banner'),status=data.get('status'),description=data.get("description"))
	return HttpResponseRedirect("/dj-admin/products")
def update_product(request):
	data = request.POST
	obj = Products.objects.get(id=data.get('id'))
	obj.title = data.get('title')
	obj.status = data.get('status')
	obj.image = data.get('page_banner')
	obj.description = data.get('description')
	obj.save()
	return HttpResponseRedirect('/dj-admin/products')