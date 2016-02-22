from django.conf.urls import include, url
from django.contrib import admin
import api.urls
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/v1/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api-login/', views.obtain_auth_token)

]
