from django.shortcuts import render
from rest_framework import mixins

# Create your views here.
class UserAPI(GeneratorExit, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    