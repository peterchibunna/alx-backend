#!/usr/bin/env python3
"""
0. Basic Flask app
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def home_page():
    """Displays the index page"""
    try:
        return render_template("1-index.html")
    except ValueError:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
