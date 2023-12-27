from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import random

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/flip_coin')
@login_required
def flip_coin():
    return render_template('flip_coin.html', user=current_user)

@views.route('/flip_result', methods=['POST'])
@login_required
def flip_result():
    heads = request.form.get('heads')
    tails = request.form.get('tails')

    # Add your coin flip logic here (randomly choose heads or tails)
    result = "Heads" if random.choice([True, False]) else "Tails"

    return render_template('flip_coin.html', result=result, heads=heads, tails=tails, user=current_user)