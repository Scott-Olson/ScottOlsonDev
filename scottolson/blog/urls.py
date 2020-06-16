from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.landing, name='landing'),
	path('<slug:slug>/', views.get_blog_by_slug, name="detail")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)