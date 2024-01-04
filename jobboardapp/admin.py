from django.contrib import admin
from .models import JobListing

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location')
    search_fields = ('title', 'company')