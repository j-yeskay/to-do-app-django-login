from django.urls import path
from . views import HomeView , CreateToDoView , DeleteToDoView , IndexView , EditToDoView , CompleteToDoView

urlpatterns = [
        path('', IndexView, name = "index"),
        path('home/', HomeView.as_view(), name = "home"),
        path('addtodo/', CreateToDoView.as_view() , name = "add-todo"),
        path('deletetodo/<int:pk>/' ,DeleteToDoView, name = "delete-todo"),
        path('edittodo/<int:pk>/' , EditToDoView.as_view() , name = "edit-todo"),
        path('completetodo/<int:pk>/', CompleteToDoView , name = "complete-todo")
]
