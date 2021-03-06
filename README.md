# ๐ฒ**DICE LAB - HomePage**
2021-08-04 ~ 2022-01-29 

### DICELAB Introduce Page

ํ๊ตญ๊ธฐ์ ๊ต์ก๋ํ๊ต ์ปดํจํฐ๊ณตํ๋ถ์ DICELAB์ ์ฐ๊ตฌ ๋ฐ ํ๋ ํํฉ์ ์๊ฐํ๋ ํ์ด์ง์๋๋ค.
์ฐ๊ตฌ์๋ค์ ํ๋์ด ๋ด๊ธด Notion DB ๋ฐ์ดํฐ๋ฅผ ์ ์ํ๊ฒ ์ ๋ฌํ๊ธฐ ์ํด
Notion DB ๋ฐ์ดํฐ๋ฅผ Web Server์ ์ฃผ๊ธฐ์ ์ผ๋ก ๋๊ธฐํํ๋ ๋น๋๊ธฐ ํ ์์์ ๊ตฌํํ์ฌ
์ต์ ์ฐ๊ตฌ๋ํฅ์ 1์๊ฐ๋ง๋ค ๊ฐฑ์ ํด ์ ๊ณตํ  ์ ์๋๋ก ๊ฐ๋ฐํ์ต๋๋ค.

# **โย Collaborator**

### [Woo-yeol](https://github.com/Woo-yeal)
### [honeyuheony](https://github.com/honeyuheony)

# ๐ฅ Project Example
<div align="center"><img src="./DiceLab.gif" width='800px'></div>

# **โ๏ธย Development Environment**

<h2 align="center">๐ Tech Stack </h2>
<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/></a>&nbsp 
 <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"></a>&nbsp   
<br>
  <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"></a>&nbsp  
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"></a>&nbsp  
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/></a>&nbsp
  <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"></a>&nbsp 
  <br>
  <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"></a>&nbsp
  <br>
  <img src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"></a>&nbsp
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"></a>&nbsp
 </p>

|Part|Version|
|------|---|
|**Front-End**|Django Templates + Bootstrap
|**Back-End**|Back : Python 3.8.5 +ย Djangoย 3.0 + Redis  
|**Database**|Sqlite3
|**Notion API**|Version : 2021-08-16
|**Distribution**|AWS-LightSail

# ๐ย **Manual**

### **Django Web Server**
1. Git Clone
    
    `git clone https://github.com/Woo-Yeol/DiceLab.git`
    
2. ๊ฐ์ ํ๊ฒฝ ์์ฑ ๋ฐ ์ข์ ์ธํ
    
    `python -m venv [๊ฐ์ํ๊ฒฝ ๋ช]`
    
    window :ย 
    
    `source [๊ฐ์ํ๊ฒฝ ๋ช]/Scripts/activate`ย 
    
    mac :ย 
    
    `source [๊ฐ์ํ๊ฒฝ ๋ช]/bin/activate`
    
    `pip install -r requirements.txt`
    
3. Migration
    
    `python manage.py createsuperuser "username"`
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
    
    `python manage.py runserver`
    

### Celery setting (with redis)

1. Run redis
    
    `redis-server`
    
2. Run Celery-Beat
    
    Start new Terminal and Set venv
    
    `python -m venv [๊ฐ์ํ๊ฒฝ ๋ช]`
    window :ย 
    
    `celery -A [Project Name] -l info -B gevent`
    
    mac :ย 
    
    `celery -A [Project Name] worker -l info -B` 
<aside>
๐ก 1์๊ฐ ๊ฐ๊ฒฉ์ผ๋ก Notion DB์ Django server๊ฐ ๋๊ธฐํ ๋ฉ๋๋ค.
</aside>
