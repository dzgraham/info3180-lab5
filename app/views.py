"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from flask import render_template, request, jsonify, send_from_directory, current_app
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import MovieForm
from app.models import Movie
from flask_wtf.csrf import generate_csrf
import os



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/movies', methods=['POST'])
def add_movie():
    form = MovieForm()
    
    if request.headers.get('X-CSRFToken'):
        form.csrf_token.data = request.headers.get('X-CSRFToken')
    
    if form.validate_on_submit():
        poster = form.poster.data
        filename = secure_filename(poster.filename)
        
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        poster.save(upload_path)
        
        movie = Movie(
            title=form.title.data,
            description=form.description.data,
            poster=filename
        )
        
        db.session.add(movie)
        db.session.commit()
        
        return jsonify({
            'message': 'Movie Info Successfully Added',
            'title': movie.title,
            'poster': filename,
            'description': movie.description
        }), 201
    
    return jsonify({'errors': form_errors(form)}), 400

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    """Return CSRF token for VueJS frontend"""
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
