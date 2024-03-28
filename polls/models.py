# 데이터 베이스 테이블 관련은 여기서 수정
from django.db import models
from django.utils import timezone
import datetime 


class Question(models.Model):
    # 캐릭터필드 ( 문자열 필드 ) 생성 
    # 생성된 테이블 열 이름 (question_text)
    question_text = models.CharField(max_length=200)
    # 데이터 타임 필드 생성
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return f"{self.question_text}_Question"

    # 입력 받은 글자 수 세기
    def count_text(self):
        return len(self.question_text)
        # print("입력받은 텍스트의 길이 : ",len(question_text))
class Choice(models.Model):
    # Question 클래스에 있는 거를 외래키로 잡아둘 것
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 정수 필드 생성
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text