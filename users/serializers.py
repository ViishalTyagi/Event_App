from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers, exceptions
from .models import Profile

User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True} }

class SignUpSerializer(serializers.ModelSerializer):
    PREFERENCES = (
        ('AT', 'Arts & Theatre'),
        ('F', 'Film'),
        ('M', 'Miscellaneous'),
        ('Music'),
        ('S', 'Sports'), 
        ('Undefined'), 
        ('D', 'Donation'), 
        ('ES', 'Event Style'), 
        ('G', 'Group'), 
        ('I', 'Individual'), 
        ('Merchandise'), 
        ('N' ,'Nonticket'), 
        ('P', 'Parking'), 
        ('T', 'Transportation'), 
        ('U', 'Upsell'), 
        ('V', 'Venue Based')
    )
    GENRE = (
        ('KnvZfZ7vAee','R&B'),
        ('KnvZfZ7vAv1', 'Hip-Hop/Rap'),
        ('KnvZfZ7vAe1', 'Comedy'),
        ('KnvZfZ7v7nJ', 'Classical'),
        ('KnvZfZ7vAvE', 'Jazz'),
        ('KnvZfZ7vAk1', 'Foreign'),
        ('KnvZfZ7vAvF', 'Dance/Electronic'),
        ('KnvZfZ7vAkA', 'Comedy'),
        ('KnvZfZ7vAkd', 'Animation'),
        ('KnvZfZ7vAkJ', 'Music'),
        ('KnvZfZ7vAka', 'Miscellaneous'),
        ('KnvZfZ7vAk', 'Family'),
        ('KnvZfZ7v7ld', 'Miscellaneous Theatre'),
        ('KnvZfZ7v7l1', 'Theatre')
    )

    email = serializers.EmailField(label='Email Address')
    password2 = serializers.CharField(write_only=True)
    preferences = serializers.ChoiceField(choices=PREFERENCES) 
    genre = serializers.ChoiceField(choices=GENRE)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'preferences',
            'genre',
        ]
        extra_kwargs = {"password": {"write_only": True} }

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exists")
        return value

    def validate(self, data):
        pw  = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def create(self, validated_data):      
        pref = validated_data.pop('preferences')
        gen = validated_data.pop('genre')

        user_obj = User(
            username=validated_data.get('username'), 
            email=validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
    
        Profile.objects.create(
            uid=user_obj.id,
            preferences=pref,
            genre=gen
        )
        # profile_obj.save()
       
        # print(profile_obj)
        return user_obj



class setPreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'preferences',
            'genre',
        ]
        
    


