from datetime import datetime as dt

def timer():
    current = dt.now().second
    
    while True:
        if dt.now().second-current>=30:
            print(dt.now().second)
            return False