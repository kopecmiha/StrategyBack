# Модуль Accounts
Регистрация, авторизация, действия с профилем пользователя

Основной url - https://testing-backend.admire.social/user/

#####Регистрация пользователя
Метод POST  
url - /sign_up/  
***
Запрос
```json
{
    "email":"test@test.ru",
    "username":"Test",
    "password":"12345",
}
```
code - поле для ввода пригласительного кода

Ответ
```json
{
    "message": "User succesfully created"
}
```
Ошибка
```json
{
    "error": "Wrong invite code"
}
```
Если код не передан или передан неверный
***

#####Аутинтификация
Метод POST

url - /obtain_token/
***
Запрос
```json
{
    "login":"test.decan@test.ru",
    "password":"12345"
}
```
в login передавать email или username

Ответ
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IkRlY2FuVGVzdCIsImV4cCI6MTY0NTkwMDM0OSwiZW1haWwiOiJ0ZXN0LmRlY2FuQHRlc3QucnUifQ.iJNMXNW3d2q5HTaIqKLSdeR43ULITj7rqr9veOufZlc"
}
```
Ошибка при неверных логине или пароле
```json
{
    "error": "Please provide right login and a password"
}
```
***
#####Авторизация
Полученный токкен передавать в заголовках по ключу Authorization в формате:  
JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IkRlY2FuVGVzdCIsImV4cCI6MTY0NTkwMDM0OSwiZW1haWwiOiJ0ZXN0LmRlY2FuQHRlc3QucnUifQ.iJNMXNW3d2q5HTaIqKLSdeR43ULITj7rqr9veOufZlcJWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IkRlY2FuVGVzdCIsImV4cCI6MTY0NTkwMDM0OSwiZW1haWwiOiJ0ZXN0LmRlY2FuQHRlc3QucnUifQ.iJNMXNW3d2q5HTaIqKLSdeR43ULITj7rqr9veOufZlc
***

#####Редактирование профиля
Метод PUT  
Требует авторизации  
url - /update_profile/
***
Запрос
```json
{
    "username":"Student",
}
```
доступные поля для редактирования:
username  
first_name  
last_name  
patronymic  
avatar - картинку передавать в form-data по ключу "avatar"  

Ответ
```json
{
    "username": "Test2",
    "email": "test@test.ru",
    "avatar": null
}
```
Ошибка при неавторизованном запросе
```json
{
    "detail": "Authentication credentials were not provided."
}
```
Ошибка при недоступном для редактирования поле
```json
{
    "detail": "Invalid signature."
}
```
***

#####Запрос профиля
Метод GET  
Требует авторизации  
url - /get_profile/
***
Ответ
```json
{
    "username": "DecanTest",
    "email": "test.decan@test.ru",
    "avatar": null
}
```
Ошибка при неавторизованном запросе
```json
{
    "detail": "Authentication credentials were not provided."
}
```
***