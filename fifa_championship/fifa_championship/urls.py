from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.championship.api import ChampionshipViewSet

router = SimpleRouter()

router.register(r"championships", ChampionshipViewSet, base_name="championship")

urlpatterns = [path("admin/", admin.site.urls)]

urlpatterns += router.urls
