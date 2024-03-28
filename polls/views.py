# 백엔드의 직접적인 부분 = view
from django.http import HttpResponse

# 요청을 보내면 응답을 하는 함수
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    return HttpResponse("우리집 맛집입니다.")
    
def order_coffee(request):
    return HttpResponse("커피 한 잔 주세요.")
