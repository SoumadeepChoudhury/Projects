from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import defaultload
from datetime import datetime as dt
app = Flask(__name__)
db_Name = "sqlite:///"+"todo"+".db"
app.config['SQLALCHEMY_DATABASE_URI'] = str(db_Name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_Modified = db.Column(db.Date, default=dt.now)

    # def __repr__(self) -> str:
    #     return f"{self.sno} {self.title} {self.date_Modified}"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route("/done/<int:sno>")
def done(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run()
