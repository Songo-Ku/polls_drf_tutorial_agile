from django.urls import path, include
from .views import polls_list, polls_detail, ListUsers
from .apiviews import ChoiceList, CreateVote, UserCreate, LoginView, CustomAuthToken
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path("api/users/", ListUsers.as_view(), name="users-list"),
    path("api/token/auth", CustomAuthToken.as_view()),  # to jest customowy auth ktory daje wiecej pol

    path('auth/', include('rest_framework.urls'), name='rest_framework'),

    path("login/", views.obtain_auth_token, name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login-password/", LoginView.as_view(), name="login-password"),

    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),


    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls