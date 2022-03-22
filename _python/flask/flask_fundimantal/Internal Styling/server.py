from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index0():
    return "hello"
@app.route('/play')
def index1():
    return render_template('index.html',countdiv=3,countt=1,page=1)
@app.route('/play/<count>')
def index2(count):
    count=int(count)
    return render_template('index.html',countdiv=count,countt=int(count/4),page=2)
@app.route('/play/<x>/<color>')
def index3(x,color):
    x=int(x)
    return render_template('index.html',countdiv=x,countt=int(x/4),Bcolor=color,page=3)

if __name__=="__main__":
    app.run(debug=True)