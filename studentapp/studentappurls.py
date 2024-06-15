from django.urls import path
from . import views

urlpatterns=[
    path('studenthome/',views.studenthome,name='studenthome'),
    path('logout/',views.logout,name='logout'),
    path('response/',views.response,name='response'),
    path('postquestion/',views.postquestion,name='postquestion'),
    path('postanswer/<qid>',views.postanswer,name='postanswer'),
    path('postans/',views.postans,name='postans'),
    path('viewanswer/<qid>',views.viewanswer,name='viewanswer'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('profilemanagement/',views.profilemanagement,name='profilemanagement'),
    path('viewmat/',views.viewmat,name='viewmat'),
]