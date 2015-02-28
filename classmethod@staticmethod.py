class Class:
    @classmethod
    def a_class_method(cls):
        print 'I was called from class %s' % cls
    #
    @staticmethod
    def a_static_method():
        print 'I have no idea where I was called from'
    #
    def an_instance_method(self):
        print 'I was called from the instance %s' % self

instance = Class()

Class.a_class_method()
instance.a_class_method()
# both print 'I was called from class __main__.Class'

Class.a_static_method()
instance.a_static_method()
# both print 'I have no idea where I was called from'

Class.an_instance_method()

# raises TypeError
instance.an_instance_method()
# prints something like 'I was called from the instance <__main__.Class instance at 0x2e80d0>'
