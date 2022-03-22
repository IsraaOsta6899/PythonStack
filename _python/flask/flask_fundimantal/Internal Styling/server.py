from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index0():
    return "hello"
@app.route('/play')
def index1():
    return render_template('index.html')
@app.route('/play/<count>')
def index2(count):
    count=int(count)
    return render_template('index2.html',countdiv=count,countt=int(count/4))
@app.route('/play/<x>/<color>')
def index3(x,color):
    x=int(x)
    return render_template('index3.html',countdiv=x,countt=int(x/4),Bcolor=color)

if __name__=="__main__":
    app.run(debug=True)