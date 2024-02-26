from flask import Blueprint, render_template

# Create a Blueprint object for main routes
main_bp = Blueprint('main', __name__)


##########################################
#           Routes                       #
##########################################


# Define routes
@main_bp.route('/')
def home():
    return render_template('home.html')
