from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('adoptar/',views.adoptar,name='adoptar'),
    path('registro/',views.registro,name='registro'),
    path('sesion/',views.sesion,name='sesion'),
    path('pitbulls/',views.mascotas_pitbull,name='pitbulls'),
    path('pastores/',views.mascotas_pastores,name='pastores'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
