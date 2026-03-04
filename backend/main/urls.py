from django.urls import include, path
from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'resumes', views.ResumeViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'previous-jobs', views.PreviousJobViewSet)
router.register(r'ratings', views.RatingViewSet)


urlpatterns = [
    # path('', views.landing_page, name='landing_page'),
    path('', include(router.urls)),
    path('login/', views.resume_login, name='resume_login'),
    # path('resumes/', views.resume_list, name='resume_list'),
    # path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
    # path('resume/edit/', views.edit_resume, name='edit_resume'),
    # path('resume/<int:pk>/rate/', views.rate_resume, name='rate_resume'),
    # path('resume/edit/add-skill/', views.add_skill, name='add_skill'),
    # path('resume/edit/add-education/', views.add_education, name='add_education'),
    # path('resume/edit/add-job/', views.add_job, name='add_job'),
]