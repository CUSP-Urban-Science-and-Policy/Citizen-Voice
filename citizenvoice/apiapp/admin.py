from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth

from .models import ( Answer, Question, Survey, Response, PointFeature, 
                     PolygonFeature, LineFeature, MapView,
                     LocationCollection, DashboardTopic)

# Register the models in the admin site in order to view, create and edit them from the admin page
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Response)
admin.site.register(PointFeature)
admin.site.register(LineFeature)
admin.site.register(PolygonFeature)
admin.site.register(MapView)
admin.site.register(LocationCollection)
admin.site.register(DashboardTopic)


# Unregister User and Group fields
# admin.site.unregister(auth.models.User)
# admin.site.unregister(auth.models.Group)

