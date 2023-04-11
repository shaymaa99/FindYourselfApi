from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Category',views.CategoryViewSet,basename='Category')
router.register('Activities',views.ActivitiesViewSet,basename='Activities')
router.register('Activities_pk<int:id>',views.ActivitiesViewSet_pk,basename='Activities_pk')
router.register('Book',views.BookViewSet,basename='Book')
router.register('Book_pk<int:id>',views.BookViewSet_pk,basename='Book_pk')
router.register('Video',views.VideoViewSet,basename='Video')
router.register('Video_pk<int:id>',views.VideoViewSet_pk,basename='Video_pk')
router.register('app_Question',views.app_questionViewSet,basename='app_Question')
router.register('app_Question_pk<int:id>',views.app_QuestionViewSet_pk,basename='app_Question_pk')
router.register('Data_of_Category',views.data_of_CategoryViewSet,basename='Data_of_Category')
router.register('Data_of_Category_pk<int:id>',views.data_of_CategoryViewSet_pk,basename='Data_of_Category_pk')
urlpatterns=[
    #path('HoppiesGenerics',views.HoppiesGenerics.as_view(),name='HoppiesGenerics'),
    #path('HoppiesGenerics_pk<int:id>/',views.HoppiesGenerics_pk.as_view(),name='HoppiesGenerics_pk')
]
urlpatterns+=router.urls