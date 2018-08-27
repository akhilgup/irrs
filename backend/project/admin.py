from django.contrib import admin
from .models import Employee, Worker, User, Complains

# Register your models here.
admin.site.register(Employee)
admin.site.register(Worker)
admin.site.register(User)
admin.site.register(Complains)
