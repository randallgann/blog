import os
from datetime import datetime

from flask import redirect, render_template, send_from_directory, session, url_for

from . import main

# from .froms import NameForm
# from .. import db
# from ..models import User


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html.jinja")


@main.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blogPosts.html.jinja")


@main.route("/new", methods=["GET", "POST"])
def new():
    return render_template("home.html.jinja")


@main.route("/favicon.ico", methods=["GET", "POST"])
def favicon():
    return send_from_directory(os.path.join(main.root_path, "static"), "favicon.ico")
