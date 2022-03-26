

from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = 'count' 
# our index route will handle rendering our form
count=-1


@app.route('/',methods=['POST'] )
def index0():
    if 'count' in session:    
            if request.form['submit'] == 'add two visits':
                session['count']=session['count']+1
                return redirect('/')
            elif  request.form['submit'] == 'reset':
                session['count']=-1
                return redirect('/')
           
    
@app.route('/' )
def index3():
        if 'count' in session:  
            session['count']=session['count']+1
            return render_template('index.html',mycount=session['count'])
        session['count']=-1
        return render_template('index.html',mycount=session['count'])


@app.route('/destroy_session' )
def index1():
    
    session.pop('count')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)