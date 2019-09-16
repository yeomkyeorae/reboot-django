### DJANGO 데이터베이스 1:N 표현

만약 `Reporter` object가 `Article` object와 `1:N`관계를 맺는다면

그리고 `Article` object가 `Comment` object와 `1:N`관계를 맺는다면

아래 코드와 같이 표현 할 수 있다. 

```python
from django.db import models


class Reporter(models.Model):
    name = models.CharField(max_length=10)
    

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



#### 예제

```python
# 1. '홍길동' 이름을 갖는 reporter1 생성
reporter1 = Reporter(name = '홍길동')

# 2. '철수' 이름을 갖는 reporter2 생성
reporter2 = Reporter(name = '철수')

# 3. reporter1에 article1 추가
article1 = Article()
article1.title = '제목'
article1.content = '내용'
article1.reporter = reporter1  # Article의 reporter 컬럼이 foreign key이므로 reporter를 등록(?)하지 않으면 아래에서 오류가 발생한다.
article.save()

# 4. reporter1에 aritcle2 추가
article2 = Article.objects.create(title='제목', content='내용', reporter_id=1)

# 5. reporter1에 article3 추가
article3 = Article.objects.create(title='제목', content='내용', reporter=reporter1)

# 6. reporter1의 article들 조회
reporter1.article_set.all()
Article.objects.filter(reporter_id=1)

# 7. article1에 댓글 2개 추가
comment1 = Comment()
comment1.content = '댓글'
comment1.article_id = 1
comment1.save()

comment2 = Comment()
comment2.content = '댓글'
comment2.article = article2
comment2.save()

# 8. 해당 댓글을 작성한 기자는 누구인가?
comment1.article.reporter

# 9. 기사별 댓글 내용 출력
articles = Article.objects.all()
for article in articles:
    for comment in article.comment_set.all():
        print(comment)
        
# 10. 기자별 기사 내용 출력
reporters = Reporter.objects.all()
for reporter in reporters:
    print(reporter.name):
    for article in reporter.article_set.all():
        print(article.title)
        
# 11. reporter1의 기사 갯수
reporter1.article_set.count()
```



