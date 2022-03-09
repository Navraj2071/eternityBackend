from django.urls import path
from . import views


urlpatterns = [
    path("addprofile", views.ProfileViewSet.as_view()),
    path("addcontracts", views.ContractsViewSet.as_view()),
    path("checkcontractexistance", views.check_contract_existance),
    path("scannedBlocks", views.ScannedBlocksViewSet.as_view()),
]
