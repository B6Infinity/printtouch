def decorator(*args, **kwargs):
     
    def wrapper(func, req):
         
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])
         
        func(req)
         
    return wrapper


@decorator(like = "geeksforgeeks")
def my_func(req):
    print("Inside actual function")

my_func(0)