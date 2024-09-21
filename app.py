# Imports
from flask import Flask, render_template, redirect, request, flash
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# My App
app = Flask(__name__)
app.secret_key = "your_secret_key"
Scss(app)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


# Task model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"Task {self.id}: {self.content}"


with app.app_context():
    db.create_all()


# Route for the home page
@app.route("/", methods=["POST", "GET"])
def index():
    # Add task
    if request.method == "POST":
        current_task = request.form['content']
        if not current_task.strip():
            flash("Task content cannot be empty!", "error")
            return redirect("/")

        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash("Task added successfully!", "success")
            return redirect("/")
        except Exception as e:
            flash(f"An error occurred while adding the task: {e}", "error")
            return redirect("/")

    # Retrieve all tasks
    tasks = MyTask.query.order_by(MyTask.created).all()
    return render_template('index.html', tasks=tasks)


# Route to delete task
@app.route("/delete/<int:id>")
def delete(id: int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        flash("Task deleted successfully!", "success")
        return redirect("/")
    except Exception as e:
        flash(f"An error occurred while deleting the task: {e}", "error")
        return redirect("/")


# Edit an item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        if not task.content.strip():
            flash("Task content cannot be empty!", "error")
            return redirect(f"/edit/{id}")

        try:
            db.session.commit()
            flash("Task updated successfully!", "success")
            return redirect("/")
        except Exception as e:
            flash(f"Error updating task: {e}", "error")
            return redirect(f"/edit/{id}")
    else:
        return render_template('edit.html', task=task)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
