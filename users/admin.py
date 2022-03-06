from django.contrib import admin
from .models import NewsLetterRecipients, Profile


# Register your models here.
admin.site.register(NewsLetterRecipients)
admin.site.register(Profile)