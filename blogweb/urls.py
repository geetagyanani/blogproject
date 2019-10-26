#blog web url file
from django.urls import path
from .views import *
from adminpanel.views import *
urlpatterns = [
        path('contact/submit',contact_submit, name="contact_submit"),

        path('dj-admin/services/add-new',add_service),
        path('dj-admin/services/edit/<id>',edit_service,name="edit_service"),
         path('dj-admin/services',services_list),
         path('dj-admin/services/delete/<id>',delete_service,name="delete_service"),
         path('dj-admin/services/submit',submit_service,name='submit_service'),
         path('dj-admin/services/update',update_service,name='update_service'),

        path('dj-admin/partners/add-new',add_partner),
        path('dj-admin/partners/edit/<id>',edit_partner,name="edit_partner"),
         path('dj-admin/partners',partners_list),
         path('dj-admin/partners/delete/<id>',delete_partner,name="delete_partner"),
         path('dj-admin/partners/submit',submit_partner,name='submit_partner'),
         path('dj-admin/partners/update',update_partner,name='update_partner'),

         path('dj-admin/products/add-new',add_product),
        path('dj-admin/products/edit/<id>',edit_product,name="edit_product"),
         path('dj-admin/products',products_list),
         path('dj-admin/products/delete/<id>',delete_product,name="delete_product"),
         path('dj-admin/products/submit',submit_product,name='submit_product'),
         path('dj-admin/products/update',update_product,name='update_product'),

        path('dj-admin/sliders/add-new',add_slider),
        path('dj-admin/sliders/edit/<id>',edit_slider,name="edit_slider"),
         path('dj-admin/sliders',sliders_list),
         path('dj-admin/sliders/delete/<id>',delete_slider,name="delete_slider"),
         path('dj-admin/sliders/submit',submit_slider,name='submit_slider'),
         path('dj-admin/sliders/update',update_slider,name='update_slider'),

         path('dj-admin/homeservices/add-new',add_homeservice),
        path('dj-admin/homeservices/edit/<id>',edit_homeservice,name="edit_homeservice"),
         path('dj-admin/homeservices',homeservices_list),
         path('dj-admin/homeservices/delete/<id>',delete_homeservice,name="delete_homeservice"),
         path('dj-admin/homeservices/submit',submit_homeservice,name='submit_homeservice'),
         path('dj-admin/homeservices/update',update_homeservice,name='update_homeservice'),

        path('',adminpanel_home , name='homeurl'),
        path(r'<slug>', adminpanel_page),
        

        





        
]
