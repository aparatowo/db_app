from flask import Flask, request
from database.db import get_session
from database.models import Image
from database.credentials import get_secret


secrets = get_secret()
app = Flask(__name__)


def db_query(query):
    def perform_query(*args, **kwargs):
        session = get_session(secrets=secrets)
        result = query(session, *args, **kwargs)
        session.commit()
        session.close()
        return result

    return perform_query


@db_query
def get_count(session):
    return session.query(Image.id).count()


@db_query
def get_link(session, image_id):
    return session.query(Image.link).filter(Image.id == image_id).one()


def add_link(image_key):
    session = get_session()
    session.add(Image(link=image_key))
    session.commit()
    session.close()
    return 'ok'


@app.route('/', methods=["GET"])
def main_view():  # put application's code here
    image_id = request.args.get("image_id")
    if image_id is not None:

        return get_link(image_id)
    return {"response": "sample"}


@app.route('/count/', methods=["GET"])
def count_view():
    return {'count': get_count()}


@app.route('/add/', methods=["GET"])
def add_image_link():
    image_key = request.args.get("image_key")
    add_link(image_key)
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
