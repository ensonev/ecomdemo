from rest_framework import serializers
from .models import Product, User
from django.contrib.auth.hashers import make_password

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email",
                  "username",
                  "first_name",
                  "last_name",
                  "is_staff",
                  "id",
                  ]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('username'))
        return super(CustomerSerializers, self).create(validated_data)
    
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =["name",
                 "description",
                 "price",
                 "stock",
                 "category",
                 "image",
                 "active",
                 "customer",
                 "id",
                  ]
        read_only_fields = ['customer', 'id']
    def create(self, validated_data):
        validated_data['active'] = True
        validated_data['customer'] = self.context.get('request').user
        return super(ProductSerializers, self).create(validated_data) 


