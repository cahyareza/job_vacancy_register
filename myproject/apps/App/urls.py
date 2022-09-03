from django.urls import path
from .views import home, register, backend, candidate

urlpatterns = [
    # Frontend
    path('', home, name="home"),
    path('register', register, name='register'),
    # Backend
    path('backend/', backend, name='backend'),
    path('<int:id>/', candidate, name='candidate'),
]