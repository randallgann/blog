from datetime import datetime
import os

from flask import redirect, render_template, session, url_for, send_from_directory

from . import main

# from .froms import NameForm
# from .. import db
# from ..models import User


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html.jinja")

@main.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html.jinja")

@main.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(main.root_path, 'static'), 'favicon.ico')
