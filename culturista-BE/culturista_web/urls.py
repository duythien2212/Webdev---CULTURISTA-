from django.urls import path
from .views.UserApi import LoginUser,RegisterUser
from .views.RoleApi import CreateRole
from .views.CountryApi import CreateCountry
from .views.RoomApi import RoomHandling,CreateRoom
from .views.PackApi import CreatePack,pack
from .views.ForumApi import CreateForum, searchForum
from .views.CommentApi import CreateComment
from .views.QuestionApi import get_question_detail,CreateQuestion,UpdateQuestion,DeleteQuestion
from .views.Render import *

urlpatterns = [
    # render path
    path('login', login_user, name="login"),

    path('register', register_user, name="register"),

    path('', index_page, name="index"),
    
    path('profile', profile, name="profile"),

    path('find-forum', find_forum, name="findForum"),

    path('chat', chat_page, name="chat"),

    path('find-room', find_room, name="findRoom"),

    path('play/roomID=<int:roomID>', play, name="play"),

    # AUTHENTICATION
    path('login-user',LoginUser.as_view()),

    path('register-user',RegisterUser.as_view()),
    # ROLE
    path('create-role', CreateRole.as_view()),  # Gọi hàm create
    # COUNTRY
    path('create-country', CreateCountry.as_view()),  # Gọi hàm create

     # QUESTION
    path('question/<int:question_id>',get_question_detail, name='get_question_detail'),
    path('question/create/', CreateQuestion.as_view()),  # Gọi hàm create
    path('question/update/<int:pk>', UpdateQuestion.as_view()),  # Gọi hàm update
    path('question/delete/<int:pk>', DeleteQuestion.as_view()),  # Gọi hàm delete

    # ROOM
    path('join-room', RoomHandling.join_room, name='join_room'),

    path('left-room', RoomHandling.left_room, name='left_room'),


    #PACK
    path('create-pack', CreatePack.as_view()),
 
    path('choose-pack', pack.choosePack, name='choosePack'),
    path('create-room', CreateRoom.as_view()),

    # Forum
    path('create-forum-form', create_forum, name='create_forum'),
    path('create-forum',CreateForum.as_view()),
    path('find-forum/title=<title>',searchForum),
    path('forum/<content_id>', forum),
    path('create-comment',CreateComment.as_view()),
]
