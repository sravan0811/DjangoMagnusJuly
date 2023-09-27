from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars',views.CarViewSet)

urlpatterns = [
    path('home/',views.home,name='home'),
    path('help/',views.help,name='help'),
    path('contact/',views.contact,name='contact'),
    path('emp/',views.emp,name="emp"),
    path('user/',views.form_page,name='userform'),
    path('empform/',views.emp_formpage,name="empform"),
    path('',include(router.urls)),
    path('app-auth/',include('rest_framework.urls',namespace='rest_framework')),

]