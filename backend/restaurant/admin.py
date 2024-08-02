"""Admin-zone of the restaurant app."""
from backend.admin_site import my_admin_site

from .models import CompanyInfo

my_admin_site.register(CompanyInfo)
