from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import views, status, generics
from rest_framework.response import Response
from .serializers import LoginSerializer, SignUpSerializer, setPreferencesSerializer
from django.contrib.auth import get_user_model
# from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q
from .models import Profile
import requests

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = Profile.objects.all()
    # permission_classes = [AllowAny]
    serializer = SignUpSerializer(queryset, many=True)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class LoginView(views.APIView):
    serializer_class=LoginSerializer
    # permission_classes=[AllowAny]
    def post(self, request, *args, **kwargs):
        #print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username)|
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                # JWT Auth can be used once Debug=False is set in settings along with other changes:
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)
                # response = jwt_response_payload_handler(token, user, request=request)
                return Response({'data': data})
        return Response({"detail": "Invalid credentials"}, status=401)

class setPreferences(views.APIView):
    serializer_class = setPreferencesSerializer
    # permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     return Profile.objects.filter(uid=User.id)

    def post(self, request, *args, **kwargs):
        data = request.data
        user_id = request.user.id
        if user_id is not None:
            Profile.objects.update_by_id(user_id, data.get('preferences'), data.get('genre'))
            print("-----------------------")
        # profile_obj.update_preferences(data.get('preferences'))
        # profile_obj.update_genre(data.get('genre'))
        # profile_obj.preferences = data.get('preferences')
        # profile_obj.genre = data.get('genre')
        # profile_obj.save()
        return Response({'data': data})

class getEvents(generics.RetrieveAPIView):
    
    def get(self, request, *args, **kwargs):
        data = request.data
        pref = data.get('preferences')
        gen = data.get('genre')
        response = requests.get("https://yv1x0ke9cl.execute-api.us-east-1.amazonaws.com/prod/events?classificationName=%s"%pref+"&genreId=%s"%gen)
        event_data = response.json()
        return Response({'events': event_data})

            
