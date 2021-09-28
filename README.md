# student-management
This is an application for student management.

Follow the steps for setuping of this project
* pip install -r requirement.txt
* Add your database name,username,password in settings.py
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

The following are the endpoints in this project. Refer **Test.json** for data format of APIs

| Endpoints | Method | Description|
| --- | --- | --- |
| /api/teacher/ | POST | create new teacher |
| /api/teacher/ | GET | list all the teachers |
| /api/student/ | GET | list all the students |
| /api/student/ | POST | create new students |
| /api/student/\<id>\/| PUT | update student details |
| /api/student/\<id>\/| DELETE | delete student details |
| /api/mark/ | GET | list marks of all students |
| /api/mark/ | POST | save student marks |
| /api/mark/\<id>\/| PUT | update student marks |
| /api/mark/\<id>\/| DELETE | delete student marks |

