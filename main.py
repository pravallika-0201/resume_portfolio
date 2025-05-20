from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page (root URL)
@app.route('/')
def home():
    return render_template('bootstrapdemo.html')

# Route for index page (optional if you want a separate path)


if __name__ == '__main__':
    app.run(debug=True)
