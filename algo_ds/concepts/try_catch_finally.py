
'''
Program that explains the concept of try,catch and finally  block.
Finally block is always returned irrespective of 

'''


def func():
    try:
        1/0
        print("try block")
        return 0
        
    
    except:
        print("catch block")
        return 1
    
    finally:
        print("finally block")
        return 2
        
if __name__=="__main__":
    x=func()
    print(x)