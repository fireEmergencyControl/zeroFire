from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'index.html')

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping("/login", method="get")
    def login(self, request):
        return render(request, 'login.html')

    @request_mapping("/tables", method="get")
    def tables(self, request):
        return render(request, 'tables.html')

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        return render(request, 'index.html')