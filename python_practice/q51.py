def cal():
    return 5/0;

try:
    cal()
except ZeroDivisionError as zd:
    print("number can,t divide by zero")
except Exception:
    print('there is exception')

