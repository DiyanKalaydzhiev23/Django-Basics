from datetime import time, datetime

from django.http import HttpResponseForbidden


class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
            field.widget.attrs["readonly"] = True


class TimeRestrictedMixin:
    access_time_start = time(9, 0)
    access_time_end = time(23, 0)

    def dispatch(self, request, *args, **kwargs):
        current_time = datetime.now().time()

        if not (self.access_time_start <= current_time <= self.access_time_end):
            return HttpResponseForbidden("Access is not allowed at this time")

        return super().dispatch(request, *args, **kwargs)
