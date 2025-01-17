from django.contrib import admin
from .models import contact, Notification, FAQ


# admin.site.register(contact)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["message", "date"]


class contactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "date"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "comments",
                    "date",
                ),
            },
        ),
    )
    list_per_page = 10


class FAQADMIN(admin.ModelAdmin):
    list_display = ["question", "date"]


admin.site.register(FAQ, FAQADMIN)


admin.site.register(contact, contactAdmin)
admin.site.register(Notification, NotificationAdmin)
# Register your models here.
