from .autoload import *
def add_service(request):
	return render(request,'adminpanel/add-service.html',{})
def edit_service(request,id):
	data=Services.objects.filter(id=id).first()
	data ={'id':data.id,'title':data.title,'image':data.image,'status':data.status}
	return render(request,'adminpanel/edit-service.html',{'data':data})
def services_list(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect("/")	
	per_page = configuration('admin_record_per_page_pages')
	if per_page is None:
		per_page = configuration('admin_record_per_page')
	defaultsort='-id'
	pageslist = Services.objects.order_by(defaultsort).all()
	paginator = Paginator(pageslist, per_page)
	page = 1
	if request.GET.get("page") is not None:
		page = request.GET.get("page")
	pageslist = paginator.get_page(page)
	return render(request,'adminpanel/services.html',{'datalist':pageslist})
def delete_service(request,id):
	data=Services.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect('/dj-admin/services')
def submit_service(request):
	data = request.POST
	Services.objects.create(title=data.get('title'),image=data.get('page_banner'),status=data.get('status'))
	return HttpResponseRedirect("/dj-admin/services")
def update_service(request):
	data = request.POST
	obj = Services.objects.get(id=data.get('id'))
	obj.title = data.get('title')
	obj.status = data.get('status')
	obj.image = data.get('page_banner')
	
	obj.save()
	return HttpResponseRedirect('/dj-admin/services')