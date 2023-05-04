"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

# Functions start here!


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_users():
    return User.query.all()


def get_user_by_id(id):
    return User.query.get(id)


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview,
                  release_date=release_date, poster_path=poster_path)

    return movie


def get_movies():
    return Movie.query.all()


def get_movie_by_id(id):
    return Movie.query.get(id)


def create_rating(user, movie, score):
    rating = Rating(user=user, score=score, movie=movie)
    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
