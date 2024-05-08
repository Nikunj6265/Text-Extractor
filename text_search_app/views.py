# Import necessary modules
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from text_search_app.models import User, Paragraph, Word
from text_search_app.serializers import (
    UserSerializer,
    SearchSerializer,
    ParagraphSerializer,
    TextSerializer,
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Registration view
class RegistrationView(APIView):
    permission_classes = [AllowAny]

    # POST method for user registration
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            user.is_active = True
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view
class LoginView(APIView):
    permission_classes = [AllowAny]

    # POST method for user login
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'detail': 'Logged in successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Email or Password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

# Logout view
class LogoutView(APIView):
    
    # POST method for user logout
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logged out successfully.'}, status=status.HTTP_200_OK)

# User detail view
class UserDetailView(APIView):
    
    # GET method to get user details
    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data['is_staff'] = request.user.is_staff
        return Response(data)

    # PATCH method to update user details
    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Search paragraphs view
class SearchParagraphs(APIView):
    
    # POST method to search for paragraphs containing a word
    def post(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data['word'].lower()
            word_instances = Word.objects.filter(word=word)
            paragraph_ids = [word_instance.paragraph_id for word_instance in word_instances]
            paragraphs = Paragraph.objects.filter(id__in=paragraph_ids)[:10]
            serializer = ParagraphSerializer(paragraphs, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Insert paragraphs view
class InsertParagraphs(APIView):
    
    # POST method to insert paragraphs into the database
    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text'].lower()
            paragraphs = text.split('\n\n')
            for paragraph_text in paragraphs:
                paragraph = Paragraph.objects.create(text=paragraph_text.strip())
                paragraph.save()
                words = paragraph.text.split(' ')
                for word in words:
                    word_obj = Word.objects.create(word=word, paragraph=paragraph)
                    word_obj.save()
            return Response({'message': 'Paragraphs inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
