from django.shortcuts import render, redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_browser import opencv_browser
from .opencv_moblie import opencv_mobile
from django.http      import JsonResponse
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

def browser(request):
    if request.method == 'POST' and request.POST['flag'] == 'Bbtn':
        flag = opencv_browser(1)
        print('browser return value', flag)
        if flag == 1:
            list = [{'browser_info': 'QR 출석을 완료했습니다. '}]
            return JsonResponse(list, safe=False)
        else:
            list = [{'browser_info': 'QR을 찾지 못했습니다. '}]
            return JsonResponse(list, safe=False)
    list = [{'browser_info': 'QR을 찾지 못했습니다. '}]
    return JsonResponse(list, safe=False)

def mobile(request):
    print('ajax - 입성')
    if request.method == 'POST' and request.POST['flag'] == 'Mbtn':
        flag = opencv_mobile(1)
        print('mobile return value - ', flag)
        if flag == 1:
            list = [{'mobile_info': 'QR 출석을 완료했습니다. '}]
            return JsonResponse(list, safe=False)
        else:
            list = [{'mobile_info': 'QR을 찾지 못했습니다. '}]
            return JsonResponse(list, safe=False)
    else:
        list = [{'mobile_info': 'QR을 찾지 못했습니다. '}]
        return JsonResponse(list, safe=False)

def alarm_check(request):
    if request.method == 'POST' and request.POST['Abtn'] == 'Abtn':
        content = {'alarm_info': '신호 출결을 완료했습니다.'}
        print('dd')
        return render(request, 'web_ver.html', content)
    else:
        return render(request, 'web_ver.html')

def alarm_ajax(request):
    if request.method == 'POST' and request.POST['flag'] == 'Abtn':
        print(request.POST['flag'])
    # print('ajax - param - ', flag)
    list = [{'info': '신호출결이 완료 되었습니다. '}]
    return JsonResponse(list, safe=False)
