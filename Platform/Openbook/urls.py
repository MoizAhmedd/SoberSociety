from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('',views.HomePageView,name = 'index'),
        path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True),name = 'login'),
        path('signup/',views.signup,name = 'signup'),
        path('success/',views.SuccessView.as_view(),name = 'success'),
        path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
        path('redirect/',views.RedirectView.as_view(),name = 'redirect'),
        path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
        path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
        path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
        path('profile/<int:pk>',views.ProfileView.as_view(),name = 'profile'),
        path('challenges/',views.ChallengeView.as_view(),name = 'ChallengeView'),
        path('challenges/new/',views.NewChallengeView.as_view(),name = 'newchallenge'),
        path('challenges/detail/<int:pk>',views.ChallengeDetailView.as_view(),name = 'ChallengeDetail'),
        path('blog/',views.BlogView.as_view(),name = 'blog'),
        path('blog/<int:pk>',views.BlogTextView.as_view(),name = 'blogdetail'),
        path('blog/<int:pk>',views.CommentsView.as_view(),name = 'comments1'),
        path('blog/<int:pk>/comment',views.WriteCommentsView.as_view(),name = 'writecomment'),
        path('chat/',views.ChatView.as_view(),name = 'chat'),
        path('new',views.WriteBlogView.as_view(),name = 'newblog')



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
