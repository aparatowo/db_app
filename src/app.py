from flask import Flask, request
from database.db import get_session
from database.models import Image

app = Flask(__name__)


def db_query(query):
    def perform_query(*args, **kwargs):
        session = get_session()
        result = query(session, *args, **kwargs)
        session.close()
        return result

    return perform_query


@db_query
def get_count(session):
    return session.query(Image.id).count()


@db_query
def get_link(session, image_id):
    return session.query(Image.link).filter(Image.id == image_id).one()


@app.route('/', methods=["GET"])
def main_view():  # put application's code here

    image_id = request.args.get("image_id")

    return get_link(image_id)


@app.route('/count/', methods=["GET"])
def count_view():
    return get_count()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
