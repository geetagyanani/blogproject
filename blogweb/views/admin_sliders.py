from .autoload import *
def add_slider(request):
	return render(request,'adminpanel/add-slider.html',{})
def edit_slider(request,id):
	data=Sliders.objects.filter(id=id).first()
	data ={'id':data.id,'title':data.title,'image':data.image,'status':data.status,'description':data.description}
	return render(request,'adminpanel/edit-slider.html',{'data':data})
def sliders_list(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect("/")	
	per_page = configuration('admin_record_per_page_pages')
	if per_page is None:
		per_page = configuration('admin_record_per_page')
	defaultsort='-id'
	pageslist = Sliders.objects.order_by(defaultsort).all()
	paginator = Paginator(pageslist, per_page)
	page = 1
	if request.GET.get("page") is not None:
		page = request.GET.get("page")
	pageslist = paginator.get_page(page)
	return render(request,'adminpanel/sliders.html',{'datalist':pageslist})
def delete_slider(request,id):
	data=Sliders.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect('/dj-admin/sliders')
def submit_slider(request):
	data = request.POST
	Sliders.objects.create(title=data.get('title'),image=data.get('page_banner'),status=data.get('status'),description=data.get('description'))
	return HttpResponseRedirect("/dj-admin/sliders")
def update_slider(request):
	data = request.POST
	obj = Sliders.objects.get(id=data.get('id'))
	obj.title = data.get('title')
	obj.status = data.get('status')
	obj.image = data.get('page_banner')
	obj.description = data.get('description')
	obj.save()
	return HttpResponseRedirect('/dj-admin/sliders')