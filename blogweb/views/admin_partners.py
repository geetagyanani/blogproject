from .autoload import *
def add_partner(request):
	return render(request,'adminpanel/add-partner.html',{})
def edit_partner(request,id):
	data=Partners.objects.filter(id=id).first()
	data ={'id':data.id,'title':data.title,'page_banner':data.image,'status':data.status}
	return render(request,'adminpanel/edit-partner.html',{'data':data})
def partners_list(request):
	if request.user.is_authenticated == False:
		return HttpResponseRedirect("/")	
	per_page = configuration('admin_record_per_page_pages')
	if per_page is None:
		per_page = configuration('admin_record_per_page')
	defaultsort='-id'
	pageslist = Partners.objects.order_by(defaultsort).all()
	paginator = Paginator(pageslist, per_page)
	page = 1
	if request.GET.get("page") is not None:
		page = request.GET.get("page")
	pageslist = paginator.get_page(page)
	return render(request,'adminpanel/partners.html',{'datalist':pageslist})
def delete_partner(request,id):
	data=Partners.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect('/dj-admin/partners')
def submit_partner(request):
	data = request.POST
	Partners.objects.create(title=data.get('title'),image=data.get('page_banner'),status=data.get('status'))
	return HttpResponseRedirect("/dj-admin/partners")
def update_partner(request):
	data = request.POST
	obj = Partners.objects.get(id=data.get('id'))
	obj.title = data.get('title')
	obj.status = data.get('status')
	obj.image = data.get('page_banner')
	obj.save()
	return HttpResponseRedirect('/dj-admin/partners')