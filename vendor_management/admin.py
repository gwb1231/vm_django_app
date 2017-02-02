from django.contrib import admin
from .models import Vendor, Contract, Service, User, Department, Project, Task
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Contract)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Task)