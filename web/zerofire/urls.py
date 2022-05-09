from django_request_mapping import UrlPattern

from zerofire.views import MyView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)
