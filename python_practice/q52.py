class CustomException(Exception):
    def __init__(self,msg):
        self.msg = msg

num = int(input())
try:
    if num < 10:
        raise CustomException('Input is less than 10')
    elif num >= 10:
        raise CustomException('number is equal or more than 10')
except CustomException as ce:
    print('there are a error: '+ce.msg)
