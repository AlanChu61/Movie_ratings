"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    # flash("This hoempage1")
    # flash("This hoempage2")
    # flash("This hoempage3")
    return render_template('hompage.html')


@app.route('/movies')
def all_movies():
    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)


@app.route("/user_rating", methods=["POST"])
def update_rating():
    new_rating = request.form.get('user_grade')
    movie_id = request.form.get('movie_id')
    # movie = crud.get_movie_by_id(movie_id)
    # print(new_rating, movie_id, movie)
    # # update rating function

    # if session['user_id']:
    #     print(session['user_id'])
    #     print(new_rating)
    #     print(movie)
    #     crud.create_rating(session['user_id'], new_rating, movie)
    movie = crud.get_movie_by_id(movie_id)
    print('movie_rating', movie)
    crud.update_rating(movie_id, new_rating)
    print('new one', movie)
    flash("You've updated the score of the movie")
    return redirect('/')


@app.route('/users')
def all_users():
    users = crud.get_users()
    return render_template('all_users.html', users=users)


@app.route('/users', methods=["POST"])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        # email exists
        flash("Cannot create an account")
        flash("Try again.")
        flash("Hi!")
    else:
        # email not exist
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
        flash("Hi!")
        flash("Welcome!")

    return redirect('/')


@app.route('/login', methods=["POST"])
def login():
    # get email and pwd from the from
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    # go to db to check if email exists
    if user:
        if user.password == password:
            session['user_id'] = user
            flash("Login!")
        else:
            flash("password incorrect")
    else:
        flash("invalid account")
    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
