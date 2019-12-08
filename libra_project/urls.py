"""libra_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import libra_project.urls
from libra import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path("Book", views.books_list ),
    path("custs", views.studant_list ),
    path("Borrow", views.Borrows_list,name='Borrows_list' ),
    path("addbook", views.addbook ,name='addbook'),
    path("addstudant", views.addstudant,name='addstudant' ),
    path("makeborrow", views.makeborrow,name='makeborrow' ),
    path("Borrow_details/<int:id>", views.Borrow_details, name='Borrow_details' ),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
