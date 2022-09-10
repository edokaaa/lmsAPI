from django.urls import path, include
from rest_framework import routers
from lms import views

app_name = 'lms'


# API Home Routes

router = routers.DefaultRouter()
router.register(r'courses', views.CourseView, 'courses')
# router.register(r'materials', views.CourseMaterialView, 'materials')
router.register(r'tracks', views.TrackView, 'tracks')
# router.register(r'capstone-projects', views.CapstoneProjectView, 'capstone-projects')


urlpatterns = [
    # path('', include(router.urls)),
    path('courses/', views.CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),
    # path('courses/<slug:slug>/', views.CourseDetailAPIView.as_view(), name='course_detail'),
    # path('courses/', views.CourseView.as_view(), name='courses'),
    # path('tracks/', views.TrackView, name='tracks_list'),
    # path('tracks/', views.TrackView.as_view({'post':'create'}), name='tracks_create'),
    # path('tracks/<slug:slug>/', views.TrackDetailAPIView.as_view(), name='track_detail'),
    # path('courses/<int:pk>/', views.course_mod_view, name='course_modification'),

    # path('capstone-projects/', views.CapstoneProjectView.as_view(), name='capstone'),
    # path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail'),
    # path('capstone-projects/<int:pk>/', views.CapstoneDetailAPIView.as_view(), name='capstone_detail'),
    # path('student-vouchers/<int:pk>/', views.VoucherDetailAPIView.as_view(), name='voucher_detail'),
    # path('student-vouchers/', views.voucher_alt_view, name='voucher'),
    # path('api/accounts/', include('accounts.urls')),

]
