# task-management

Task Management

1.Clone the repository to your local machine:
git clone https://github.com/yourusername/task-management.git

2.Navigate to the project directory:
cd task-management

3.Install packages:
pip install Flask SQLAlchemy psycopg2-binary

4.Configure the database connection:
Open the config/constant.py file.
Update the Constants class variable with your PostgreSQL database credentials
.DATABASE_USERNAME
.DATABASE_PASSWORD
.DATABASE_NAME = 'task_management'
Create the database in pgAdmin

5.Create the tables:
python createdb.py

6.Start the Flask development server:
python app.py

7.Use Postman to interact with the API endpoints:
.GET /tasks: Retrieve all tasks
.POST /tasks: Create a new task
Body: {
"title":,
"description":,
"completed":
}
.GET /tasks/{task_id}: Retrieve a specific task
.PUT /tasks/{task_id}: Update a specific task
Body: {
"title":,
"description":,
"completed":
}
.DELETE /tasks/{task_id}: Delete a specific task
