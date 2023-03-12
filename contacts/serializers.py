from rest_framework import serializers
from .models import Contact


class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'name', 'contact_number', 'email']


class SpamSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['contact_number', 'spam']
        lookup_fields = 'contact_number'


class ContactSearchSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'name', 'contact_number', 'email', 'spam']
