from .autoload import *
def contact_submit(request):
	data = request.POST
	message = render_to_string('blogweb/email.html',{'name':data.get("home"),'email':data.get("email"),"phone":data.get("phone"),"message":data.get("message")})
	subject = "Inquiry from Body Care"
	mail = EmailMessage(subject,message,to=['geetagyanani123@gmail.com'])
	mail.send()
	reply_message = render_to_string("blogweb/reply.html",{})
	subject ="Thank you for enquiry with us"
	mail = EmailMessage(subject,reply_message,to =[data.get("email")])
	status ={"status":"success"}
	return HttpResponse(json.dumps(status))