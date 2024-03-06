from django.urls import include, path
# import routers
from rest_framework import routers


# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register('Employee', EmployeeSet)


# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),
	# path('api-auth/', include('rest_framework.urls')),
	#path('student-auth/',include('rest_framework.urls')),
    path('employee-auth/',include('rest_framework.urls'))
    ,

]
