from django.contrib import admin

# Register your models here.
from .models import dashboard_live, stripeUser_live
class dashboardAdmin(admin.ModelAdmin):
	class Meta:
		model = dashboard_live
admin.site.register(dashboard_live,dashboardAdmin)

class stripeUserAdmin(admin.ModelAdmin):
	class Meta:
		model = stripeUser_live
 
admin.site.register(stripeUser_live,stripeUserAdmin)
