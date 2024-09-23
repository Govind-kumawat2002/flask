def update(fx):
    def mfx():
        print("good morning baby")
    fx()
    print("baby how are you ")
    return mfx
@update
def hello():
    print("hello hiii baby")
hello()



# def baby():


