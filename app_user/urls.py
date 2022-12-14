from django.urls import path, include

import app_user.views as resource
from app_user.exceptions import handler404

# handler404=handler404

urlpatterns = [
    path("new/", resource.NewUserView.as_view(), name="new user"),
    path("login/", resource.LoginUserView.as_view(), name="login user"),
    path("logout/", resource.LogoutUserView.as_view(), name="logout user"),
    path("<int:pk>/", include([
        path("info/", resource.ProfileUserView.as_view(), name="profile user"),
        path("edit/", resource.edit_user_view, name="edit user"),
        path("delete/", resource.DeleteUserView.as_view(), name="delete user"),
        ])
    )
]



