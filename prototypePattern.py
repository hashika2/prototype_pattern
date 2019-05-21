import copy

class Prototype:
    _type=None
    _value=None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value


class Type1(Prototype): 

    def _init_(self,number):
        self._type="type1"
        self._value=number

    def clone(self):
        return copy.copy(self)

class Type2(Prototype):

    def _init_(self,number):
        self._type="type2"
        self._value=number

    def clone(self):
        return copy.copy(self) 

class ObejectFactory:

    _type1Value1=None
    _type1Value2=None
    _type2Value1=None
    _type2Value2=None

@staticmethod
def initialize():
    ObejectFactory._type1Value1=Type1(1)
    ObejectFactory._type1Value2=Type2(2)
    ObejectFactory._type2Value1=Type2(1)
    ObejectFactory._type2Value2=Type2(2)    

@staticmethod
def getType1Value1():
    return ObejectFactory._type1Value1.clone()

def getType1Value2():
    return ObejectFactory._type1Value2.clone()    

def getType2Value1():
    return ObejectFactory._type2Value1.clone() 

def getType2Value2():
    return ObejectFactory._type2Value2.clone()

def main():
    ObejectFactory.initialize()

    instance=ObejectFactory.getType1Value1()
    print "%s: %s" %(instance.getType(),instace.getValue()) 

    instance=ObejectFactory.getType1Value2()
    print "%s: %s" %(instance.getType(),instace.getValue())

    instance=ObejectFactory.getType2Value1()
    print "%s: %s" %(instance.getType(),instace.getValue())

    instance=ObejectFactory.getType2Value2()
    print "%s: %s" %(instance.getType(),instace.getValue())

if _name_=="_main_":
    main()    

