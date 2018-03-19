
from Parent import parentClass

class childClass(parentClass.parentInner):
    def print_class_name(self):
        print('childClass')



if __name__=='__main__':
    childObj = childClass()
    childObj.print_class_name()
    childObj.innerp()