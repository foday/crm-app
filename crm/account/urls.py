from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home), 
    #path('products/', views.products),
    #path('customer/', views.customer)

]