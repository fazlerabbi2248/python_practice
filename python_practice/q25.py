class employee:
    type = 'employee'
    def __init__(self,type=None):
        self.name = type

dev = employee('developer')
dev.type= 'developer'
print(f"{employee.type} type is {dev.type}")