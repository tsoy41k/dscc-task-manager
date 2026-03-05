Task manager Django application 



This is a task management application built with Django. Users can register, log in, create their task lists with categories and tags 



#Technologies:

-Python
-Django
-PostgreSQL
-Docker
-Gunicorn
-Nginx
-Bootstrap 

#Architecture 

-Docker container:
	-Django application 
	-PostgreSQL database 
	-Nginx proxy

#How to run the project 

Clone the repository:
git clone <repo_url>

go to project folder: 
cd dscc_project

run containers: 
docker compose up --build 