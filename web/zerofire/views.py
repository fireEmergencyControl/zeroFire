from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from zerofire.models import *
from django.core.paginator import Paginator


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        try:
            if request.session['sessionid'] != None:
                return render(request, 'alreadylogin.html')
            else:
                pass
        except:
            return render(request, 'login.html')

    @request_mapping("/index", method="get")
    def index(self, request):
        try:
            mgr = Manager.objects.get(id=request.session["sessionid"])
            context = {'obj':mgr}
            return render(request, 'index.html', context)
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping("/login", method="get")
    def login(self, request):
        try:
            if request.session['sessionid'] != None:
                return render(request, 'alreadylogin.html')
            else:
                pass
        except:
            return render(request, 'login.html')

    @request_mapping("/logout", method="get")
    def logout(self, request):
        try:
            if request.session['sessionid'] != None:
                del request.session['sessionid']
                return redirect('/')
            else:
                pass
        except:
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
            Manager.objects.get(id=id)
            return render(request, 'registerfail.html')
        except:
            if zfPass == zfPassChk:
                mgrclass = Rankdata.objects.get(rno=zfClass)
                Manager(name=name, id=id, email=mail, workarea=workarea, rno=mgrclass, pass_field=zfPass).save();
                request.session['sessionid'] = id;
                return redirect('/')
            else:
                return render(request, 'registerfail.html')

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST["inputId"]
        zfPass = request.POST["inputPass"]

        try:
            mgr = Manager.objects.get(id=id)
            if mgr.pass_field == zfPass:
                request.session["sessionid"] = mgr.id
                # context = {'obj':mgr}
                return redirect("/index")
            else:
                return render(request, 'loginfail.html')
        except:
            return render(request, 'loginfail.html')

    @request_mapping("/info", method="get")
    def info(self, request):
        try:
            obj = Manager.objects.get(id=request.session["sessionid"])
            context = {'obj': obj};
            return render(request, 'info.html', context)
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/change", method="get")
    def change(self, request):
        try:
            obj = Manager.objects.get(id=request.session["sessionid"])
            context = {'obj': obj}
            return render(request, 'change.html', context)
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/changeimpl", method="post")
    def changeimpl(self, request):
        name = request.POST["name"]
        id = request.POST["id"]
        mail = request.POST["mail"]
        workarea = request.POST["workarea"]
        # zfClass = request.POST["class"]
        zfPass = request.POST["pass"]
        zfPassChk = request.POST["passCheck"]

        try:
            obj = Manager.objects.get(id=request.session["sessionid"])
            if zfPass == zfPassChk:
                # mgrClass = Rankdata.objects.get(rno=zfClass)
                obj.name = name
                obj.email = mail
                obj.workarea = workarea
                # obj.rno = mgrClass
                obj.pass_field = zfPass
                obj.save()
                return redirect('/')
            else:
                pass
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/delete", method="get")
    def delete(self, request):
        try:
            id2 = Manager.objects.get(id=request.session["sessionid"])
            if request.session["sessionid"] != None:
                del request.session["sessionid"]
            id2.delete()
            return render(request, 'delete.html')
        except:
            return render(request, 'accessfail.html')

    @request_mapping("/tables", method="get")
    def tables(self, request):
        try:
            Manager.objects.get(id=request.session["sessionid"])
            board = Board.objects.all()
            page = request.GET.get('page', '1')
            question_list = Board.objects.order_by('-bno')
            paginator = Paginator(question_list, 10)
            page_obj = paginator.get_page(page)
            context = {'boards': board,
                       'question_list': page_obj,
                       'page': page}

            return render(request, 'tables.html', context)
        except:
            return render(request, "accessfail.html")

    @request_mapping("/write", method="get")
    def write(self, request):
        try:
            Manager.objects.get(id=request.session["sessionid"])
            return render(request, 'write.html')
        except:
            return render(request, "accessfail.html")

    @request_mapping("/writeimpl", method="post")
    def writeimpl(self, request):
        # try:
            id = request.session["sessionid"]
            if id != None:
                info = Manager.objects.get(id=id)
                # fcount = request.POST["fcount"]
                pump = request.POST["pump"]
                content = request.POST["contents"]
                etc = request.POST["etc"]
                # rtime = request.POST["rtime"]
                Board(mno=info, pump=pump, content=content, etc=etc).save()
                return redirect('/tables')
            else:
                # pass
        # except:
                return render(request, 'accessfail.html')
        # return render(request, 'write.html')

    @request_mapping("/test", method="get")
    def test(self, request):
        return render(request, 'index2.html')