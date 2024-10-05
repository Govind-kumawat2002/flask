from flask import Flask ,render_template ,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('basic.html')

@app.route('/predict',methods= ['POST','GET'])
def predict():
    email=request.form['predict']
    print(email)




if __name__=="__main__":
    app.run(debug=True)