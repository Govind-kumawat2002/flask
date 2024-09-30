from flask import Flask ,render_template,request
app=Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')
@app.route('/home')
def home():
    # return render_template("hello babu")
    return ("hello sir ")
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method =='POST':
        user=request.form['username']
        email=request.form['email']
        password = request.form['password']

        LST = ["username:",user,"user_email:",email,"user_passwor:",password]
        print(LST)
    
    return render_template('form.html')
    







if __name__=="__main__":
    app.run(debug= True)