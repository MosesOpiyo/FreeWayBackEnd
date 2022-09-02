from rest_framework import serializers

from .models import Account,MyAccountManager

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','password','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        account = Account(email=self.validated_data['email'],username = self.validated_data['username'])
        account.set_password(self.validated_data['password'])
        print(f"New user,{account.username} has been created with email {account.email}")
        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','username','date_joined','last_login']