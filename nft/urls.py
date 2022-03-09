from django.urls import path
from . import views


urlpatterns = [
    path("fileupload", views.NFTViewSet.as_view()),
    path("multifileupload", views.MultiNFTViewSet.as_view()),
    path("addCollection", views.CollectionViewSet.as_view()),
    path("getCollection", views.get_collection_data),
    path("updateCollection", views.update_collection_contract),
    path("createNFT", views.CreateNFTViewSet.as_view()),
    path("getNFT", views.get_nft_data),
    path("updateNFT", views.NFTUpdateViewSet.as_view()),
]
