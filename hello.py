# Flask built-in-server to localhost

from flask import Flask             # 1

app = Flask(__name__)               # 2


@app.route("/")                     # 3
def index():
    return "Hello, World!"          # 4

if __name__ == '__main__':          # 5
    app.run(port=5000, debug=True)  # 6


#1) Imports Flask from the package flask

#2) Creates an instance(app) of the Flask objekt and uses the moduls name
#   (Flask) as the parameter. Flask use this to resolve resources. In our
#   projects we always use (__name__), which links our module to the Flask
#   object

#3) Is a Python-Decorator. The function below should be directly called
#   whenever a user visits the "main root page". "/" is the sign for
#   main root page

#4) Function, that returns "Hello, World!" when a user visits our webpage

#5) Conditional Statement True, if our application is run directly. The
#   code below won't run, if the file is imported.

#6) Kicks off Flask development server on our local machine. Run on port 5000.
#   Debug True, so we can see detailed errors directly in our web browser

# https://github.com/Wasserratte/firstapp.git
