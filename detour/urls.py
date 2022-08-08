"""detour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from detourapi.data.data_collection import YELPView
from detourapi.views.auth import register_user, login_user
from rest_framework import routers
from detourapi.views.doc import DocView
from detourapi.views.docassign import DocAssignView
from detourapi.views.greenroom_request import GreenRoomRequestView
from detourapi.views.guest_request import GuestRequestView
from detourapi.views.schedule_item import ScheduleItemView
from detourapi.views.show_date import ShowDateView
from detourapi.views.user import UserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'showDates', ShowDateView, 'showdate')
router.register(r'docs', DocView, 'doc')
router.register(r'assignDocToShow', DocAssignView, 'docassign')
router.register(r'greenRoomRequests', GreenRoomRequestView, 'greenroomrequest')
router.register(r'guestRequests', GuestRequestView, 'guestrequest')
router.register(r'scheduleItems', ScheduleItemView, 'scheduleitem')
router.register(r'users', UserView, 'user')
router.register(r'datacollection', YELPView, 'data')

urlpatterns = [
# Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
# Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
