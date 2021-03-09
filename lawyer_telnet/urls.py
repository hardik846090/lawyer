from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('practice', views.practice, name="practice"),
    path('practice2', views.practice2, name="practice2"),
    path('practicedetails', views.practicedetails, name="practicedetails"),
    path('cases', views.cases, name="cases"),
    path('blog', views.blog, name="blog"),
    path('blogleft', views.blogleft, name="blogleft"),
    path('blogdetails', views.blogdetails, name="blogdetails"),
    path('team', views.team, name="team"),
    path('teamdetails', views.teamdetails, name="teamdetails"),
    path('faq', views.faq, name="faq"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('contact', views.contact, name="contact"),
    path('consultation', views.consultation, name="consultation"),

    #  *****  admin  *****

    path('admin/dashboard', views.dashboard, name="dashboard"),
    path('admin/dashboard?username=hardik&password=1234', views.adminlogin, name="adminlogin"),
    path('admin/contact', views.admincontact, name="admincontact"),

    path("changeStatus/<str:foo>", views.changeStatus, name="changeStatus"),

    #  *****  Services  *****

    path('admin/services', views.adminLoadService, name="adminLoadService"),
    path('admin/insertservice', views.adminInsertService, name="adminInsertService"),
    path('admin/viewservice', views.adminViewService, name="adminViewService"),
    path('admin/deleteservice', views.adminDeleteService, name="adminDeleteService"),
    path('admin/editservice', views.adminEditService, name="adminEditService"),
    path('admin/updateserivce', views.adminUpdateService, name="adminUpdateService"),

    #  *****  Practice  *****

    path('admin/practices', views.adminLoadPractice, name="adminLoadPractice"),
    path('admin/insertpractice', views.adminInsertPractice, name="adminInsertPractice"),
    path('admin/viewpractice', views.adminViewPractice, name="adminViewPractice"),
    path('admin/deletepractice', views.adminDeletePractice, name="adminDeletePractice"),
    path('admin/editpractice', views.adminEditPractice, name="adminEditPractice"),
    path('admin/updatepractice', views.adminUpdatePractice, name="adminUpdatePractice"),
    path('user/filterpractice/<str:practice>', views.filterpractice, name="filterpractice"),

    #  *****  Law  *****

    path('admin/law', views.adminLoadLaw, name="adminLoadLaw"),
    path('admin/insertlaw', views.adminInsertLaw, name="adminInsertLaw"),
    path('admin/viewlaw', views.adminViewLaw, name="adminViewLaw"),
    path('admin/deletelaw', views.adminDeleteLaw, name="adminDeleteLaw"),
    path('admin/editlaw', views.adminEditLaw, name="adminEditLaw"),
    path('admin/updatelaw', views.adminUpdateLaw, name="adminUpdateLaw"),

    #  *****  Media  *****

    path('admin/media', views.adminLoadMedia, name="adminLoadMedia"),
    path('admin/insertmedia', views.adminInsertMedia, name="adminInsertMedia"),
    path('admin/viewmedia', views.adminViewMedia, name="adminViewMedia"),
    path('admin/deletemedia', views.adminDeleteMedia, name="adminDeleteMedia"),
    path('admin/editmedia', views.adminEditMedia, name="adminEditMedia"),
    path('admin/updatemedia', views.adminUpdateMedia, name="adminUpdateMedia"),
    path('user/filtermedia/<str:media>', views.filtermedia, name="filtermedia"),

    #  *****  Media Comment  ****

    path('user/addcomment', views.addcomment, name="addcomment"),
    path('admin/comment', views.adminLoadComment, name="adminLoadComment"),
    path('user/insertcomment', views.insertComment, name="insertComment"),
    path('admin/addreply', views.adminReplyComment, name="adminReplyComment"),
    path('admin/insertReply', views.adminInsertReply, name="adminInsertReply"),
    path('admin/deletereply', views.adminDeleteReply, name="adminDeleteReply"),
    path('admin/editreply', views.adminEditReply, name="adminEditReply"),
    path('admin/updatereply', views.adminUpdateReply, name="adminUpdateReply"),

    #  *****  Consulation  *****

    path('admin/consultation', views.adminConsulation, name="consulation"),

]
