from flask import Blueprint

main = Blueprint("main", __name__)

# routes inside view and error handlers
# we import them here after main to prevent circular dependencies
# both views and errors in turn import main blueprint object
# imports will fail unless references occur after main
from . import errors, views
