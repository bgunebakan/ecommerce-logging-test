import logging
import os
from flask import Flask, request, jsonify, render_template, session, redirect
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from time import sleep
from random import choice
from payment import pay
import sys
from fluent import asynchandler as fluent_asynchandler

# Fluentd logger
fluent_format = {
    'host': os.getenv('FLUENT_HOST', 'localhost'),
    'port': os.getenv('FLUENT_PORT', 24224),
    'tag': 'app.log'
}
fluent_handler = fluent_asynchandler.FluentHandler(**fluent_format)
fluent_handler.setLevel(logging.WARNING)
logger = logging.getLogger('fluentd_logger')
logger.addHandler(fluent_handler)


app = Flask(__name__)

sentry_dsn = os.getenv('SENTRY_DSN', '')

if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()]
    )

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
        logger.warning({"item": item, "message": f"{item} is added to cart"})
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


app.run(debug=True, host='0.0.0.0', port=5000)
