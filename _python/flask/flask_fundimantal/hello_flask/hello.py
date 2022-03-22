# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response
# @app.route('/success')
# def success():
#   return "success"
# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name
# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.
# from flask import Flask, render_template  # added render_template!
# app = Flask(__name__)                     
    
# @app.route('/')                           
# def hello_world():
#     # Instead of returning a string, 
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html')  
    
# if __name__=="__main__":
#     app.run(debug=True)  
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"
@app.route('/dojo')
def index1():
    return "Dojo!"
@app.route('/say/flask')
def index2():
    return "Hi Flask!"
@app.route('/say/<name>')
def index3(name):
    return ""+name
@app.route('/repeat/<count>/<name>')
def index4(count,name):
    count=int(count)
    return render_template("index.html", phrase=name, times=count)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)  