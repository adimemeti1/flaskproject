from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def index():
    return  render_template('Hyrja.html')

@app.route('/Sami Frasheri')

def index1():
    return render_template('Sami.html')

@app.route('/Naim Frasheri')

def index2():

    return render_template('naim.html')
@app.route('/Abdyl Frasheri')

def index3():
    return render_template('abdyl.html')





if __name__== '__main__':
    app.run(debug=True)





    