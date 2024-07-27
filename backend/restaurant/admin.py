"""Admin-zone of the restaurant app."""
from django.contrib import admin

from .models import CompanyInfo

admin.site.register(CompanyInfo)
