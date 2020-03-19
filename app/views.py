"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import hashlib
import datetime
import os
import psycopg2
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.forms import LoginForm,UserForm
from app.models import UserProfile
import psycopg2
def connect_db():
 DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URI')
 return psycopg2.connect(DATABASE_URL, sslmode='require')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def createprofile():
    form = UserForm()
    if request.method == 'POST' :
        f_name = form.firstname.data
        l_name = form.lastname.data
        mail = form.email.data
        gen = form.gender.data
        loc = form.location.data
        bio = form.bio.data
        pfile = form.file.data
        jdate=datetime.datetime.now().strftime("%B %d, %Y")
        tname=f_name+mail+jdate
        filename =secure_filename(str(hash(f_name+mail))+pfile.filename)
        pfile.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        user = UserProfile(first_name=f_name, last_name=l_name, gender=gen, email=mail, location=loc, biography=bio, date_joined=jdate, pro_pic=filename)
        db.session.add(user) 
        db.session.commit() 
        flash('Profile Saved', 'success')
        return redirect('/profiles')
    
    return render_template('createprofile.html', form = form)

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_profiles;")
    users = cur.fetchall()
    return render_template('profiles.html',users=users)

@app.route('/profile/<userid>')
def profile(userid):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_profiles WHERE id=%d;"%int(userid))
    cuser = cur.fetchone()
    return render_template('profile.html',cuser=cuser)





# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
