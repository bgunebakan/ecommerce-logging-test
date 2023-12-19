from flask import Flask, request, jsonify, render_template, session, redirect
from time import sleep
from random import choice
from loguru import logger
from payment import pay
import sys


logger.add(sys.stderr, format="{time} {level} {message}", filter="Amazon", level="DEBUG")


app = Flask(__name__)
app.config['SECRET_KEY'] = "akjsdhfljkahlskjdsfhkahkj"


goods = [
    "apple",
    "orange",
    "milk",
    "bread",
    "horse",
]


@app.get('/')
def index():
    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]
    raw_errors = request.args.get("errors", "")
    if raw_errors:
        errors = raw_errors.split(',')
    print(cart)
    return render_template('index.html', goods=goods, cart=cart)


@app.post('/add_to_cart')
def add_to_cart():
    item = request.form["item"]
    if item not in goods:
        logger.warning(f"{item} is added to cart")
    quantity = request.form["quantity"]
    session["cart"][item] = quantity
    session.modified = True
    return redirect('/')


@app.post('/pay')
def make_payment():
    cart = session.get("cart", {})
    payment_result = pay(cart)
    return render_template('result.html', success=payment_result)


@app.get('/reset')
def reset():
    session["cart"] = {}
    return redirect('/')

app.run(debug=True)
