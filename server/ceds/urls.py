from django.urls import path
from server.ceds.views import ServicesMockListView

urlpatterns = [
    # http://localhost:8000/service/web/api/v1/services
    path(
        route="web/api/v1/services",
        view=ServicesMockListView.as_view(),
        name="services_mock"
    )
]
