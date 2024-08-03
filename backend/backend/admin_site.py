"""Admin-site of the project."""
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    """My custom admin site."""

    site_header = "Администрирование ресторана"
    site_title = "Админ портал"
    index_title = "Добро пожаловать"

    def get_app_list(self, request):
        """Get app list."""
        app_dict = self._build_app_dict(request)
        models = []
        for app_name, app in app_dict.items():
            models.extend(app['models'])

        restaurant_models = []
        other_models = []

        for model in models:
            m_n = model['object_name']
            if m_n in ['Category', 'Dish', 'Order',]:
                restaurant_models.append(model)
            else:
                other_models.append(model)

        sections = []
        if restaurant_models:
            sections.append({'name': 'Ресторан', 'models': restaurant_models})
        if other_models:
            sections.append({'name': 'Служебная информация',
                             'models': other_models})
        return sections


my_admin_site = MyAdminSite(name='admin')
