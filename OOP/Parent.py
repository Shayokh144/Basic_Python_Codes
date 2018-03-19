class parentClass():
    def print_class_name(self):
        print('parentClass')
    def parentIdentity(self):
        print('parentIdentity')
    class parentInner():
        def innerp(self):
            print('this is parent inner')



if __name__=='__main__':
    parentObj = parentClass()
    parentObj.print_class_name()