from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/result', methods=['POST'])
def StoreInfo():
    print("Got Post Info")
    print(request.form)
    session['Name']= request.form['Name']
    session['Location']= request.form['Location']
    session['Language']= request.form['Language']
    session['Comment']= request.form['Comment']
    session['gender']=  request.form.getlist('gender')

    return redirect("/show")	# changed this line!
    
# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)