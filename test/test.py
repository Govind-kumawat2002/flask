from flask import Flask, render_template
app=Flask(__name__)

# @app.route('/')
@app.route('/')
def hello(name=None):
    return render_template('basic.html', name=name)
@app.route('/predict',methods =['GET','POST'])
def predict():
    return render_template('basic.html')


if __name__=='__main__':
    app.run(debug=True)