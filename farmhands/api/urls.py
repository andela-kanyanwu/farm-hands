"""
URL patterns for farmhands API
"""

from django.conf.urls import url
from api.views import PlanView, PlanDetailView, UserPlanView,\
    UserPlanDetailView, LoginView, RegisterView, LogoutView

urlpatterns = [
    url(r'^plans$', PlanView.as_view(), name='plans'),
    url(r'^plans/(?P<planid>[0-9]+)$', PlanDetailView.as_view(), name='plan'),
    url(r'^users/(?P<userid>[0-9]+)/plans$',
        UserPlanView.as_view(), name='userplans'),
    url(r'^users/(?P<userid>[0-9]+)/plans/(?P<planid>[0-9]+)$',
        UserPlanDetailView.as_view(), name='userplan'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^register$', RegisterView.as_view(), name='register')
]
