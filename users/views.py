from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from users.serializers import UserSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer
from votes.models import Vote


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def newsletters(self, request, pk=None):
        user = self.get_object()
    # 6. Como usuario quiero iniciar sesión para poder ver los boletines a los que estoy suscrito.
        if request.method== 'GET':
            id = Newsletter.objects.filter(users=int(user.id))
            serialized = NewsletterSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
    # 7. Como usuario quiero poder darme de baja de los boletines para dejar de recibir noticias.
        if request.method=='DELETE':
            id_user = user.id 
            newsletters = Newsletter.objects.all()
            for newsletter in newsletters:
                newsletter.users.remove(id_user)
            return Response(status = status.HTTP_204_NO_CONTENT)


class Login(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('users: UserViewset')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login.self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        user = authenticate(username= form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login.self).form_valid(form)

