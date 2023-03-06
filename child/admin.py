from django.contrib import admin

from .models import childinfo,typecci,cci,lostchild

from .models import Post,Comment,Question,cases,parent,donor

from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Post)
admin.site.register(cases)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(childinfo)
admin.site.register(typecci)
admin.site.register(cci)
admin.site.register(lostchild)
admin.site.register(parent)
admin.site.register(donor)

admin.site.site_header = 'Child Care Admin'                    
admin.site.index_title = 'Admin Panel'           
admin.site.site_title = 'Child Care admin'