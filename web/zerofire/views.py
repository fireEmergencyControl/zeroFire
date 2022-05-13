from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from zerofire.models import *

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

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return redirect('/')

    @request_mapping("/tables", method="get")
    def tables(self, request):
        return render(request, 'tables.html')

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        name = request.POST["name"]
        id = request.POST["id"]
        mail = request.POST["mail"]
        workarea = request.POST["workarea"]
        zfClass = request.POST["class"]
        zfPass = request.POST["pass"]
        zfPassChk = request.POST["passCheck"]


        try:
            Manager.objects.get(id = id)
            return render(request, 'registerfail.html')
        except:
            if zfPass == zfPassChk:
                mgrclass = Rankdata.objects.get(rno = zfClass)
                Manager(name=name, id=id, email=mail, workarea=workarea, rno=mgrclass, pass_field=zfPass).save();
                request.session['sessionid'] = id;
                return redirect('/')
            else:
                return render(request, 'registerfail.html')

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST["inpitName"]
        zfPass = request.POST["inputPass"]

        try:
            mgr = Manager.objects.get(id=id)
            if mgr.pass_field == zfPass:
                request.session["sessionid"] = id
                return redirect('/')
            else:
                pass
        except:
            return render(request, 'loginfail.html')

    @request_mapping("/info", method="get")
    def info(self, request):
        try:
            obj = Manager.objects.get(id = request.session["sessionid"])
            context = {'obj':obj};
            return render(request, 'info.html',context)
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/change", method="get")
    def change(self, request):
        try:
            obj = Manager.objects.get(id=request.session["sessionid"])
            context = {'obj':obj}
            return render(request, 'change.html', context)
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/changeimpl", method="post")
    def changeimpl(self, request):
        name = request.POST["name"]
        id = request.POST["id"]
        mail = request.POST["mail"]
        workarea = request.POST["workarea"]
        zfClass = request.POST["class"]
        zfPass = request.POST["pass"]
        zfPassChk = request.POST["passCheck"]

        try:
            Manager.objects.get(id=request.session["sessionid"])
            if zfPass == zfPassChk:
                Manager(id=id, name=name, email=mail,workarea=workarea, rno=zfClass, pass_field=zfPass).save()
                return redirect('/')
            else:
                return render(request, 'registerfail.html')
        except:
            return render(request, 'accessfail.html')