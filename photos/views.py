from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404, redirect
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required


def hello(request):
    return HttpResponse('안녕하세요!')

def detail(request, pk):

    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url)
    )
    return HttpResponse('\n'.join(messages)) ##템플릿 없이 그냥 결과물 출력해서 보여주는듯

@login_required
def create(request):

    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(obj)
        # obj는 photo 모델객체의 인스턴스, form은 Photoform 폼객체의 인스턴스. save()를 통해 폼객체->모델객체로 바꿔준다고 생각함
    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx) ##템플릿에 결과물을 보여줌