from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from .utils import generate_data_set
from .views import SchemeList, CreateSchema, EditSchema, SchemeDelete, SchemeDetail

urlpatterns = [
    path('', login_required(SchemeList.as_view())),
    path('generate_data/<int:id>/', login_required(generate_data_set), name='generate-data'),
    path('schemas/<int:pk>/', login_required(SchemeDetail.as_view()), name='schema-detail'),
    path('data_sets/<int:pk>/', login_required(SchemeDetail.as_view()), name='data-sets'),
    path('create/', login_required(CreateSchema.as_view()), name='create'),
    path('list/', login_required(SchemeList.as_view()), name='list'),
    path('edit/<int:id>/', login_required(EditSchema.as_view()), name='edit'),
    path('delete/<int:id>/', login_required(SchemeDelete.as_view()), name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', RedirectView.as_view(url='/./list/', permanent=False)),
]
