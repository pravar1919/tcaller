from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Contact
from .serializers import ContactSerializers, SpamSerializers, ContactSearchSerializers
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


def home(request):
    return render(request, 'index.html')


class ContactListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)


class SpamView(generics.ListAPIView):
    queryset = Contact.objects.filter(spam=True)
    serializer_class = SpamSerializers
    permission_classes = (permissions.AllowAny,)


class SpamMarkView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = SpamSerializers
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'contact_number'


class SearchView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSearchSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'contact_number']
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class APIRouter(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'contacts': reverse('contacts', request=request, format=format),
            'spam': reverse('spam', request=request, format=format),
            'search': reverse('search', request=request, format=format),
        })
