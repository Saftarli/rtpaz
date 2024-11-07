from flask import Flask, render_template, request,redirect, url_for,flash
from prj import app, db
from .models import Contact
from prj.forms import ContactForm




# @app.route('/')
# def home():
#     return render_template('home/index.html')

@app.route('/', methods=["GET","POST"])
def contact():
    form = ContactForm(request.form)
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()
        flash("Sizin mesajınız uğurla göndərildi", 'success')
        # return redirect(url_for('contact'))
        form=ContactForm()
    return render_template('home/index.html', form=form)

    



    
    
