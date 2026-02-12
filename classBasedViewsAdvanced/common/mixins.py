from django.db.models.fields import return_None
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from travelers.models import Traveler


class RecentObjectsMixin:
    recent_results_limit = 3

    @property
    def object_list(self):
        return self.__object_list

    @object_list.setter
    def object_list(self, value):
        self.__object_list = value[:self.recent_results_limit]

class AgeRestrictionMixin:

    def dispatch(self, request, *args, **kwargs):
        traveler_id = kwargs.get('pk') or request.GET.get('user_id')
        if traveler_id:
            try:
                traveler = Traveler.objects.get(pk=traveler_id)
            except Traveler.DoesNotExist:
                return HttpResponseRedirect(reverse('common:home-teen'))

            if traveler.age < 21:
                return HttpResponseRedirect(reverse('common:home-teen'))

        return super().dispatch(request, *args, **kwargs)
