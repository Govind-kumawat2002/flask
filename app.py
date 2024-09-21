from flask import Flask ,url_for ,render_template ,request ,redirect
app=Flask(__name__)
# app.config[]
# app.config    == {  }  # confige is defien a dict 

#flask apna ek global storage rkhta hai jo kuch time tk hold rkta hai 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods =['GET',"POST"])
def predict():
    if request.method=='POST':
        user_name =request.form['username']
        user_email=request.form['email']
        user_pass=request.form['password']
        # lst = [[user_name,user_email,user_pass]]
        app.config['username']=user_name
        app.config['useremail']=user_email
        app.config['userpassword']=user_pass

        return redirect(url_for('profile',username =user_name,email=user_email,password=user_pass))
    


@app.route('/profile/<username>/<email>/<password>')
def profile(username, email, password):
    # print(app.config['username'])
    # print(app.config['useremail'])
    # print(app.config['userpassword']) # local var acces in local block 
    app.config['username']=username
    app.config['useremail']=email
    app.config['userpassword']=password


    return render_template('profile.html',name=username,email=email,password=password)    
    # return "hello "
    
    

@app.route('/logout')
def logout():
    user=app.config['username'] 
    email=app.config['useremail']
    pas=app.config['userpassword']
    
    return render_template('logout.html',name=user,email=email) 
@app.route('/signout/<username>/<email>')
def signout(username,email):
    # return f"username {username,}and email {email}"
    return render_template('logout.html',name=username,email=email) 


    



if __name__=='__main__':
    app.run(debug=True)