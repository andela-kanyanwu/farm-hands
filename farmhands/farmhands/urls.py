from django.conf.urls import include, url
from django.contrib import admin
import api.urls

urlpatterns = [
    url(r'^api/v1/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls'))
]
