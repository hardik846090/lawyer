from django.shortcuts import render, redirect, HttpResponse
from .models import Services, Practices, Contact, Law, Media, MediaComment, Consulation
from django.contrib import messages
import os
from django.db.models import Q
import json


# Create your views here.

# *****  admin *****

def dashboard(request):
    return render(request, 'admin/index.html')


def adminlogin(request):
    return render(request, 'admin/index.html')


def admincontact(request):
    contactList = Contact.objects.all()
    return render(request, 'admin/contact.html', {'contactList': contactList})


def adminConsulation(request):
    consulationList = Consulation.objects.all()
    return render(request, 'admin/consultation.html', {'consulationList': consulationList})


def changeStatus(request, foo):
    if foo == 'service':
        id = request.GET['id']
        status = request.GET['status']
        changeStatus = Services.objects.get(pk=id)
        if status == 'active':
            changeStatus.status = 'inactive'
        if status == 'inactive':
            changeStatus.status = 'active'
        changeStatus.save()
        return redirect('/admin/viewservice')

    if foo == 'practice':
        id = request.GET['id']
        status = request.GET['status']
        changeStatus = Practices.objects.get(pk=id)
        if status == 'active':
            changeStatus.status = 'inactive'
        if status == 'inactive':
            changeStatus.status = 'active'
        changeStatus.save()
        return redirect('/admin/viewpractice')

    if foo == 'law':
        id = request.GET['id']
        status = request.GET['status']
        changeStatus = Law.objects.get(pk=id)
        if status == 'active':
            changeStatus.status = 'inactive'
        if status == 'inactive':
            changeStatus.status = 'active'
        changeStatus.save()
        return redirect('/admin/viewlaw')

    if foo == 'media':
        id = request.GET['id']
        status = request.GET['status']
        changeStatus = Media.objects.get(pk=id)
        if status == 'active':
            changeStatus.status = 'inactive'
        if status == 'inactive':
            changeStatus.status = 'active'
        changeStatus.save()
        return redirect('/admin/viewmedia')


# *****  services  *****

def adminLoadService(request):
    return render(request, 'admin/services.html')


def adminInsertService(request):
    serviceName = request.POST['serviceName']
    serviceDesc = request.POST['serviceDesc']
    serviceImage = request.FILES.get('serviceImage')

    addService = Services(serviceName=serviceName, serviceDesc=serviceDesc, serviceImage=serviceImage, status="active")
    addService.save()
    messages.success(request, "Service successfully saved.")
    return redirect('/admin/viewservice')


def adminViewService(request):
    serviceList = Services.objects.all()
    return render(request, 'admin/viewServices.html', {'serviceList': serviceList})


def adminDeleteService(request):
    id = request.GET['id']
    deleteService = Services.objects.get(pk=id)
    os.remove('../lawyer/media/' + str(deleteService.serviceImage))
    deleteService.delete()
    messages.success(request, "Service successfully deleted.")
    return redirect('/admin/viewservice')


def adminEditService(request):
    id = request.GET['id']
    editService = Services.objects.get(pk=id)
    return render(request, 'admin/services.html', {'editService': editService})


def adminUpdateService(request):
    id = request.POST['id']
    serviceName = request.POST['serviceName']
    serviceDesc = request.POST['serviceDesc']
    serviceImage = request.FILES.get('serviceImage')

    updateService = Services.objects.get(pk=id)
    if serviceImage != None:
        os.remove('../lawyer/media/' + str(updateService.serviceImage))
        updateService.serviceImage = serviceImage
    updateService.serviceName = serviceName
    updateService.serviceDesc = serviceDesc
    updateService.save()
    messages.success(request, "Service successfully updated.")
    return redirect('/admin/viewservice')


    #  *****  practices  *****


def adminLoadPractice(request):
    return render(request, 'admin/practices.html')


def adminInsertPractice(request):
    practiceName = request.POST['practiceName']
    practiceDesc = request.POST['practiceDesc']
    practiceImage = request.FILES.get('practiceImage')

    addPractice = Practices(practiceName=practiceName, practiceDesc=practiceDesc, practiceImage=practiceImage,
                            status="active")
    addPractice.save()
    messages.success(request, "Practice successfully saved.")
    return redirect('/admin/viewpractice')


def adminViewPractice(request):
    practiceList = Practices.objects.all()
    return render(request, 'admin/viewPractices.html', {'practiceList': practiceList})


def adminDeletePractice(request):
    id = request.GET['id']
    deletePractice = Practices.objects.get(pk=id)
    os.remove('../lawyer/media/' + str(deletePractice.practiceImage))
    deletePractice.delete()
    messages.success(request, "Practice successfully deleted.")
    return redirect('/admin/viewpractice')


def adminEditPractice(request):
    id = request.GET['id']
    editPractice = Practices.objects.get(pk=id)
    return render(request, 'admin/practices.html', {'editPractice': editPractice})


def adminUpdatePractice(request):
    id = request.POST['id']
    practiceName = request.POST['practiceName']
    practiceDesc = request.POST['practiceDesc']
    practiceImage = request.FILES.get('practiceImage')

    updatePractice = Practices.objects.get(pk=id)

    if practiceImage != None:
        os.remove('../lawyer/media/' + str(updatePractice.practiceImage))
        updatePractice.practiceImage = practiceImage
    updatePractice.practiceName = practiceName
    updatePractice.practiceDesc = practiceDesc
    updatePractice.save()
    messages.success(request, 'Practice successfully updated.')
    return redirect('/admin/viewpractice')


def filterpractice(request, practice):
    practiceId = request.GET['practiceId']
    practiceList = Practices.objects.filter(practiceName=practice)

    return render(request, 'user/practice-details.html',
                  {'practiceList': practiceList, 'practice': practice, 'practiceId': practiceId})


#  *****  Law  *****

def adminLoadLaw(request):
    return render(request, 'admin/law.html')


def adminInsertLaw(request):
    lawName = request.POST['lawName']
    lawDesc = request.POST['lawDesc']
    lawImage = request.FILES.get('lawImage')

    addLaw = Law(lawName=lawName, lawDesc=lawDesc, lawImage=lawImage, status="active")
    addLaw.save()
    messages.success(request, "Law successfully saved.")
    return redirect('/admin/viewlaw')


def adminViewLaw(request):
    lawList = Law.objects.all()
    return render(request, 'admin/viewLaw.html', {'lawList': lawList})


def adminDeleteLaw(request):
    id = request.GET['id']
    deleteLaw = Law.objects.get(pk=id)
    os.remove('../lawyer/media/' + str(deleteLaw.lawImage))
    deleteLaw.delete()
    messages.success(request, "Law successfully deleted.")
    return redirect('/admin/viewlaw')


def adminEditLaw(request):
    id = request.GET['id']
    editLaw = Law.objects.get(pk=id)
    return render(request, 'admin/law.html', {'editLaw': editLaw})


def adminUpdateLaw(request):
    id = request.POST['id']
    lawName = request.POST['lawName']
    lawDesc = request.POST['lawDesc']
    lawImage = request.FILES.get('lawImage')

    updateLaw = Law.objects.get(pk=id)
    if lawImage != None:
        os.remove('../lawyer/media/' + str(updateLaw.lawImage))
        updateLaw.lawImage = lawImage
    updateLaw.lawName = lawName
    updateLaw.lawDesc = lawDesc
    updateLaw.save()
    messages.success(request, "Law successfully updated.")
    return redirect('/admin/viewlaw')


#  *****  Media  *****

def adminLoadMedia(request):
    return render(request, 'admin/media.html')


def adminInsertMedia(request):
    mediaTitle = request.POST['mediaTitle']
    mediaDesc = request.POST['mediaDesc']
    byName = request.POST['byName']
    mediaImage = request.FILES.get('mediaImage')
    related = request.POST['related']

    addMedia = Media(mediaTitle=mediaTitle, mediaDesc=mediaDesc, byName=byName, mediaImage=mediaImage, related=related,
                     status="active")
    addMedia.save()
    messages.success(request, "Media successfully saved.")
    return redirect('/admin/viewmedia')


def adminViewMedia(request):
    mediaList = Media.objects.all().order_by('-pub_date')
    return render(request, 'admin/viewmedia.html', {'mediaList': mediaList})


def adminDeleteMedia(request):
    id = request.GET['id']
    deleteMedia = Media.objects.get(pk=id)
    os.remove('../lawyer/media/' + str(deleteMedia.mediaImage))
    deleteMedia.delete()
    messages.success(request, "Media successfullt deleted.")
    return redirect('/admin/viewmedia')


def adminEditMedia(request):
    id = request.GET['id']
    editMedia = Media.objects.get(pk=id)
    return render(request, 'admin/media.html', {'editMedia': editMedia})


def adminUpdateMedia(request):
    id = request.POST['id']
    mediaTitle = request.POST['mediaTitle']
    mediaDesc = request.POST['mediaDesc']
    byName = request.POST['byName']
    mediaImage = request.FILES.get('mediaImage')
    related = request.POST['related']

    updateMedia = Media.objects.get(pk=id)
    if mediaImage != None:
        os.remove('../lawyer/media/' + str(updateMedia.mediaImage))
        updateMedia.mediaImage = mediaImage
    updateMedia.mediaTitle = mediaTitle
    updateMedia.mediaDesc = mediaDesc
    updateMedia.byName = byName
    updateMedia.related = related
    updateMedia.save()
    messages.success(request, "Media successfully updated.")
    return redirect('/admin/viewmedia')


def filtermedia(request, media):
    mediaId = request.GET['mediaId']
    mediaList = Media.objects.filter(mediaTitle=media)

    mediaCommentList = MediaComment.objects.filter(mediaId_id=mediaId).order_by('-id')
    otherMediaList = Media.objects.filter(~Q(mediaTitle=mediaList[0].mediaTitle), related=mediaList[0].related)

    return render(request, 'user/blog-details.html',
                  {'mediaList': mediaList, 'media': media, 'mediaCommentList': mediaCommentList, 'mediaId': mediaId,
                   'otherMediaList': otherMediaList[:2]})


#  *****  user comment  *****

def addcomment(request):
    mediaId = request.GET['mediaId']
    return render(request, 'user/blog-details.html', {'mediaId': mediaId})


def adminLoadComment(request):
    mediaCommentList = MediaComment.objects.all()
    return render(request, 'admin/viewComment.html', {'mediaCommentList': mediaCommentList})


def insertComment(request):
    mediaId = request.POST['mediaId']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    commentDesc = request.POST['commentDesc']

    MediaComment(name=name, email=email, phone=phone, commentDesc=commentDesc, status="pending",
                 mediaId_id=mediaId).save()
    getMedia = Media.objects.get(pk=mediaId)

    return redirect('user/filtermedia' + str(getMedia.id) + "?mediaId=" + str(mediaId))


def adminReplyComment(request):
    id = request.GET['id']
    return render(request, 'admin/addReply.html', {'id': id})


def adminInsertReply(request):
    id = request.POST['mediaCommentId']
    commentReply = request.POST['commentReply']
    commentMediaReply = MediaComment.objects.get(pk=id)

    from datetime import datetime
    commentReplyDate = str(datetime.today().date())

    commentMediaReply.commentReply = commentReply
    commentMediaReply.commentReplyDate = commentReplyDate

    if commentMediaReply.commentReply == commentReply:
        commentMediaReply.status = "replied"
    else:
        commentMediaReply.status = "pending"

    commentMediaReply.save()
    return redirect('/admin/comment')


def adminDeleteReply(request):
    id = request.GET['id']
    deleteReply = MediaComment.objects.get(pk=id)
    deleteReply.delete()
    messages.success(request, "Reply successfully deleted.")
    return redirect('/admin/comment')


def adminEditReply(request):
    id = request.GET['id']
    editReply = MediaComment.objects.get(pk=id)
    return render(request, 'admin/addReply.html', {'editReply': editReply})


def adminUpdateReply(request):
    id = request.POST['id']
    commentReply = request.POST['commentReply']
    updateReply = MediaComment.objects.get(pk=id)
    updateReply.commentReply = commentReply
    updateReply.save()
    messages.success(request, "Reply successfully updated.")
    return redirect('/admin/comment')


# *****  user  *****

def index(request):
    practiceList = Practices.objects.all()
    mediaList = Media.objects.all().order_by('-pub_date')
    return render(request, 'user/index.html', {'practiceList': practiceList, 'mediaList': mediaList})


def about(request):
    with open(r"C:\Users\Hardik\PycharmProjects\lawyer\lawyer.json", 'r') as openfile:
        json_object = json.load(openfile)

    aboutList = json_object
    practiceList = Practices.objects.all()

    return render(request, 'user/about.html', {'aboutList': aboutList, 'practiceList': practiceList})


def practice(request):
    return render(request, 'user/practice.html')


def practice2(request):
    practiceList = Practices.objects.all()
    return render(request, 'user/practice-2.html', {'practiceList': practiceList})


def practicedetails(request):
    return render(request, 'user/practice-details.html')


def cases(request):
    return render(request, 'user/cases.html')


def blog(request):
    mediaList = Media.objects.all().order_by('-pub_date')
    return render(request, 'user/blog.html', {'mediaList': mediaList})


def blogleft(request):
    return render(request, 'user/blogleft.html')


def blogdetails(request):
    return render(request, 'user/blog-details.html')


def team(request):
    return render(request, 'user/team.html')


def teamdetails(request):
    return render(request, 'user/team-details.html')


def faq(request):
    return render(request, 'user/faq.html')


def testimonials(request):
    return render(request, 'user/testimonials.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        thank = True
    return render(request, 'user/contact.html', {'thank': thank})


def consultation(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        message = request.POST.get("message", "")
        consulation = Consulation(name=name, email=email, phone=phone, address=address, message=message)
        consulation.save()
        thank = True
    return render(request, 'user/index.html', {'thank': thank})
