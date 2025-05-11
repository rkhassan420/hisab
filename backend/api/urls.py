from django.urls import path
from loan import views

urlpatterns = [    

    path('home-content/', views.home_content),
    path('add-qist/', views.add_qist),
    path('get-all-qist/', views.get_all_qist),

]