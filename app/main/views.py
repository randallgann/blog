from datetime import datetime

from flask import redirect, render_template, session, url_for

from . import main

# from .froms import NameForm
# from .. import db
# from ..models import User


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html.jinja")
