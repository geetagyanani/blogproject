from .autoload import *
def homepage(request):
	data = Pages.objects.filter(page_slug='home-page').first()
	if data is None:
		return render(request,'blogweb/404.html',{})
	temp_path = "blogweb/"+data.page_slug+".html"
	status=template_exist(temp_path)
	if status==False:
		temp_path="blogweb/home.html"
	return render(request,temp_path,{'data':data})
def template_exist( templatepath ):
	try:
		template.loader.get_template(templatepath)
		return True
	except:
		return False