from django.urls import path
from .views.UserApi import LoginUser,RegisterUser
from .views.RoleApi import CreateRole
from .views.CountryApi import CreateCountry
from .views.RoomApi import RoomHandling,CreateRoom
from .views.PackApi import CreatePack,pack
# from .views.ForumApi import CreateForum
# from .views.CommentApi import CreateComment
# from .views.QuestionApi import get_question_detail,CreateQuestion,UpdateQuestion,DeleteQuestion
from .views.UserApi import login_user
from .views.UserApi import register_user
from .views.Render import index_page

urlpatterns = [
    path('login', login_user),

    path('register', register_user),

    path('index', index_page),

    path('login-user',LoginUser.as_view()),

    path('register-user',RegisterUser.as_view()),
    # ROLE
    path('create-role', CreateRole.as_view()),  # Gọi hàm create
    # COUNTRY
    path('create-country', CreateCountry.as_view()),  # Gọi hàm create

    #  # QUESTION
    # path('question/<int:question_id>',get_question_detail, name='get_question_detail'),
    # path('question/create/', CreateQuestion.as_view()),  # Gọi hàm create
    # path('question/update/<int:pk>', UpdateQuestion.as_view()),  # Gọi hàm update
    # path('question/delete/<int:pk>', DeleteQuestion.as_view()),  # Gọi hàm delete

    # ROOM
    path('join-room', RoomHandling.join_room, name='join_room'),

    path('left-room', RoomHandling.left_room, name='left_room'),


    #PACK
    path('create-pack', CreatePack.as_view()),
 
    path('choose-pack', pack.choosePack, name='choosePack'),
    path('create-room', CreateRoom.as_view()),

    
    # path('create-forum',CreateForum.as_view()),
    
    # path('create-comment',CreateComment.as_view()),
]
