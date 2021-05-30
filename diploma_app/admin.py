from django.contrib import admin
from .models import reg_user, points, professions, worker, pupil, diplomas

admin.site.register(reg_user)
admin.site.register(points)
admin.site.register(professions)
admin.site.register(worker)
admin.site.register(pupil)
admin.site.register(diplomas)
