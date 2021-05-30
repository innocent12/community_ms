"""community_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLConf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app_cms import views
from django.urls import path
from django.urls import re_path
from app_cms.admin import views as admin_view
from app_cms.user.views import MigrantView as MigrantView
from app_cms.user.views import ResidentView as ResidentView
from app_cms.face_authencation import views as face_view
from app_cms.check_log import views as check_view

urlpatterns = [
    re_path(r'^$', views.index),
    path('logout/', views.logout),
    path('valid_account/', admin_view.valid_account),
    path('manage/', views.manage),
    path('blackboard/', views.blackboard),
    path('cms_admin/', admin_view.admin),
    path('cms_admin/list', admin_view.admin_list),
    path('cms_admin/cmsAdmin_add', admin_view.admin_add),
    path('cms_admin/save', admin_view.admin_save),
    path('cms_admin/delete', admin_view.admin_delete),
    path('cms_admin/update', admin_view.admin_update),
    re_path(r'^cms_admin/cmsAdmin_edit/[0-9]*$', admin_view.admin_edit),
    path('cms_statistic/', admin_view.statistic),
    path('cms_admin/statistic_api', admin_view.statistic_api),

    path('cms_resident/', ResidentView.resident),
    path('cms_resident/list', ResidentView.list),
    path('cms_resident/add', ResidentView.add),
    path('cms_resident/save', ResidentView.save),
    path('cms_resident/delete', ResidentView.delete),
    path('cms_resident/update', ResidentView.update),
    re_path(r'^cms_resident/edit/[0-9]*$', ResidentView.edit),

    path('cms_migrant/', MigrantView.migrant),
    path('cms_migrant/list', MigrantView.list),
    path('cms_migrant/add', MigrantView.add),
    path('cms_migrant/save', MigrantView.save),
    path('cms_migrant/delete', MigrantView.delete),
    path('cms_migrant/update', MigrantView.update),
    re_path(r'^cms_migrant/edit/[0-9]*$', MigrantView.edit),

    path('cms_check/', check_view.check),
    path('cms_check/list', check_view.list),
    path('cms_check/add', check_view.add),
    path('cms_check/add_with_img', check_view.add_with_img),
    path('cms_check/save', check_view.save),
    path('cms_check/delete', check_view.delete),
    path('cms_check/update', check_view.update),
    re_path(r'^cms_check/edit/[0-9]*$', check_view.edit),

    path('cms_face/video_cap', face_view.face_reconginze),
    path('cms_face/video', face_view.face_video),
    path('cms_face/validate_face', face_view.solve_face),


]
