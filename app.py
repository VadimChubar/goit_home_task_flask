from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Contact, db_session


app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/show')
def show():
    contacts = db_session.query(Contact)
    return render_template("show.html", contacts=contacts)


@app.route('/show/<int:id>')
def show_edit(id):
    contact = db_session.query(Contact).get(id)
    return render_template("show_edit.html", contact=contact)


@app.route('/show/<int:id>/delete')
def show_delete(id):
    contact = db_session.query(Contact).get(id)

    try:
        db_session.delete(contact)
        db_session.commit()
        return redirect('/')
    except:
        return "Error check and replace"


@app.route('/add_contact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        contact = Contact(name=name, phone=phone, email=email)
        try:
            db_session.add(contact)
            db_session.commit()
            return redirect('/')
        except:
            return "Error check and replace"
    else:
        return render_template("add_contact.html")


@app.route('/show/<int:id>/update', methods=['POST', 'GET'])
def show_update(id):
    contact = db_session.query(Contact).get(id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']

        try:
            db_session.commit()
            return redirect('/')
        except:
            return "Error check and replace"
    else:
        return render_template("show_update.html", contact=contact)


if __name__ == "__main__":
    app.run()





