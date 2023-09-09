from django.urls import path
from .views import taskAll, taskDetail, taskpost, taskpatch, taskput, taskdelete

urlpatterns=[
    path('taskall/', taskAll.as_view()),
    path('taskdetail/<int:forid>', taskDetail.as_view()),
    path('taskpost/', taskpost.as_view()),
    path('taskpatch/<int:forid>', taskpatch.as_view()),
    path('taskput/<int:forid>', taskput.as_view()),
    path('taskdelete/<int:forid>', taskdelete.as_view())
]