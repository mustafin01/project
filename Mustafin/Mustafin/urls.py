from django.contrib import admin
from django.urls import path, re_path
from mustafin_app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('full_name/', views.full_name, kwargs={'name': 'mustafin', 'age': 17, 'interests': 'изучение python'}),
    path('full_about/', views.full_about, kwargs={'city': 'Набережные Челны', 'perfomance': 'Нармальное', 'study_preference': 'Люблю учиться'}),
    path('full_contacts/', views.full_contracts, kwargs={'github': 'https://github.com/mustafin01', 'tg': '@WHOMUSTAFA', 'number_phone': 79968458036})
]

