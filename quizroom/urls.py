from django.urls import include, path

from .views import quizroom, students, clubs

urlpatterns = [
    path('', quizroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('clubs/', include(([
        path('', clubs.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', clubs.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', clubs.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', clubs.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', clubs.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', clubs.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', clubs.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', clubs.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='clubs')),
]
