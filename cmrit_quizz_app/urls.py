from django.urls import include, path

from quizroom.views import quizroom, students, clubs

urlpatterns = [
    path('', include('quizroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', quizroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/club/', clubs.ClubSignUpView.as_view(), name='club_signup'),
]