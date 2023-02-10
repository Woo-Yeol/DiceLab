# 📖 **Manual**

## **Commit Message**

### Type

- feat : 새로운 기능 추가, 기존의 기능을 요구 사항에 맞추어 수정
- fix : 기능에 대한 버그 수정
- build : 빌드 관련 수정
- chore : 패키지 매니저 수정, 그 외 기타 수정 ex) .- gitignore
- ci : CI 관련 설정 수정
- docs : 문서(주석) 수정
- style : 코드 스타일, 포맷팅에 대한 수정
- refactor : 기능의 변화가 아닌 코드 리팩터링 ex) 변수 이름 변경
- test : 테스트 코드 추가/수정
- release : 버전 릴리즈

## **Guide**

### **Django Web Server**

1. Git Clone

   `git clone https://github.com/DICE-public/DiceLab.git`

2. 가상 환경 생성 및 종속 세팅

   `python -m venv [가상환경 명]`

   window :

   `source [가상환경 명]/Scripts/activate`

   mac :

   `source [가상환경 명]/bin/activate`

   `pip install -r requirements.txt`

3. Migration

   `python manage.py createsuperuser "username"`

   `python manage.py makemigrations`

   `python manage.py migrate`

   `python manage.py runserver`

### Celery setting (with redis)

1.  Run redis

    `redis-server`

2.  Run Celery-Beat
    Start new Terminal and Set venv

        `python -m venv [가상환경 명]`
        window :

        `celery -A [Project Name] -l info -B gevent`

        mac :

        `celery -A [Project Name] worker -l info -B`

    <aside>
    💡 1시간 간격으로 Notion DB와 Django server가 동기화 됩니다.
    </aside>
