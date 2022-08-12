from django.contrib import admin
from .models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task
        fields = '__all__'


admin.site.register(Task, TaskAdmin)
