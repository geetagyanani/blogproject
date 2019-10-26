from .autoload import *
def add_homeservice(request):
	return render(request,'adminpanel/add-homeservice.html',{})
def edit_homeservice(request,id):
	data=Homeservices.objects.filter(id=id).first()
	data ={'id':data.id,'title':data.title,'page_banner':data.image,'status':data.status,'description':data.description,'readmore_link':data.readmore_link}
	return render(request,'adminpanel/edit-homeservice.html',{'data':data})
def homeservices_list(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect("/")	
	per_page = configuration('admin_record_per_page_pages')
	if per_page is None:
		per_page = configuration('admin_record_per_page')
	defaultsort='-id'
	pageslist = Homeservices.objects.order_by(defaultsort).all()
	paginator = Paginator(pageslist, per_page)
	page = 1
	if request.GET.get("page") is not None:
		page = request.GET.get("page")
	pageslist = paginator.get_page(page)
	return render(request,'adminpanel/homeservices.html',{'datalist':pageslist})
def delete_homeservice(request,id):
	data=Homeservices.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect('/dj-admin/homeservices')
def submit_homeservice(request):
	data = request.POST
	Homeservices.objects.create(title=data.get('title'),image=data.get('page_banner'),status=data.get('status'),description=data.get("description"),readmore_link=data.get("readmore_link"))
	return HttpResponseRedirect("/dj-admin/homeservices")
def update_homeservice(request):
	data = request.POST
	obj = Homeservices.objects.get(id=data.get('id'))
	obj.title = data.get('title')
	obj.status = data.get('status')
	obj.image = data.get('page_banner')
	obj.description = data.get('description')
	obj.readmore_link = data.get('readmore_link') 
	obj.save()
	return HttpResponseRedirect('/dj-admin/homeservices')