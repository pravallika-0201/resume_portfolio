from flask import Flask, render_template, request

app = Flask(__name__)

# # Route for the home page (root URL)
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route for index page (optional if you want a separate path)
# @app.route('/index')
# def index():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
