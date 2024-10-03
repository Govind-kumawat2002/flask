# def hello(fx):
#     def hii():
#         print("hello sir")
#     fx()
#     def hiiiii():
#         print("heklnfkjgndsjfg")


# @hello
    

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# wrap = my_decorator(say_hello)
# wrap()