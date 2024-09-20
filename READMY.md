### Task Smash 2.0 
is a simple web application for task management built with Python using Flask and an SQLite database.


## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Use flash messages to notify the user (e.g., task added successfully, error messages)

## Technology Stack

- **Flask**
- **Flask-SQLAlchemy**
- **SQLite** (for the database)
- **SCSS/CSS** (for styling)
- **HTML** (Jinja2 templates)
- **Python**

## Installation

### 1. Clone the Repository

Clone the repository or copy the project to your desired directory:

```bash
git clone https://github.com/your-username/task-smash.git
cd task-smash
```

### 2. Install Dependencies

Ensure you have installed all the dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Before running the application, create the SQLite database by running:

```bash
python app.py
```

## Run the Application

To start the application, run:

```bash
python app.py
```

## Project Structure

- `app.py`: Main file containing Flask routes, database models, and application logic
- `templates/`: Folder containing HTML templates (Jinja2 templates)
- `index.html`: The main page displaying tasks and the form to add new tasks
- `edit.html`: The page for editing existing tasks
- `base.html`: The base template shared by other templates
- `static/`: Folder for static files such as CSS and SCSS files
- `styles.css`: The compiled CSS file for styling the application
- `styles.scss`: SCSS file for defining the styles
- `database.db`: The SQLite database file, automatically created during the first run of the application

## Application Functionality

### Home Page

1. The user opens http://127.0.0.1:5000
2. The main page displays a form to add a new task and a list of all existing tasks
3. The user inputs a task and clicks the "Add Task" button
4. The task is added to the database, and a success message is flashed to the user
5. The user can:
   - Edit tasks by clicking the "Edit" link next to each task
   - Delete tasks by clicking the "Delete" link

### Edit Task Page

1. The user clicks "Edit" next to a task and is taken to the edit page
2. The user can change the task content in the input field
3. After making changes, the user clicks the "Update" button to save the changes

### Deleting Tasks

- The user clicks "Delete" next to a task, and the task is removed from the database

### Flash Messages

Flash messages are used to notify the user about different actions:

- Task successfully added/updated/deleted
- Errors, such as trying to submit an empty task

## Styling

The application uses SCSS for styling, which is compiled into CSS. Basic CSS is used to improve the layout and visuals of the forms and buttons.

## Potential Enhancements

- Task sorting functionality
- Ability to mark tasks as complete
- User registration and login for personalized task lists

