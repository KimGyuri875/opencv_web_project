from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dface import opencv_dface
from .opencv_moblie import opencv_mobile
# Create your views here.
def web_ver(request):
    return render(request, 'web_ver.html')

def uimage(request):
    if request.method =='POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'uimage.html', {'form':form,'uploaded_file_url':uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'uimage.html', {'form':form})

def check(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)
            return render(request, 'check.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'check.html', {'form':form})

def mobile(request):
    if request.method == 'POST' and request.POST['btn'] == 'upload':
        flag = opencv_mobile()
        print('mobile return value - ', flag)
        return render(request, 'mobile_ver.html')
    else:
        return render(request, 'mobile_ver.html')