# FastAPI TODO App

A simple TODO application built with FastAPI and PostgreSQL using Docker Compose.

## 🧾 Example `.env` File

Create a `.env` file in the root of the project with the following content:

```env
POSTGRES_USER=todo_user
POSTGRES_PASSWORD=todo_pass
POSTGRES_DB=todo_db
DB_HOST=db
DB_PORT=5432
```

🚀 How to Run the Project
	1.	Make sure you have Docker and Docker Compose installed.
	2.	In your terminal, run:

```bash
docker compose up -d
```  
	3.	Once everything is up and running, the app will be available at:
  
```url  
http://localhost:8000/docs
```