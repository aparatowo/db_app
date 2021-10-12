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
def get_link(session, requested_id):
    return session.query(Image.id == requested_id).one()


@app.route('/', methods=["GET"])
def main_view():  # put application's code here

    id = request.args.get["id"]
    link = get_link(id)

    conn = get_session()
    conn.add(Image(link=link))

    return


@app.route('count/', methods=["GET"])
def count_view():
    return get_count()


if __name__ == '__main__':
    app.run()
