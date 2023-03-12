from django.urls import path
from .views import ContactListView, ContactView, APIRouter, SpamView, SpamMarkView, SearchView, home

urlpatterns = [
    # path('', home, name='root'),
    path('', APIRouter.as_view(), name='root'),
    path('spam/', SpamView.as_view(), name='spam'),
    path('spam/<int:contact_number>/', SpamMarkView.as_view(), name='mark-spam'),
    path('search/', SearchView.as_view(), name='search'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('contacts/<pk>/', ContactView.as_view(), name='single-contact'),
]
