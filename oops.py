"""       ---> class and object just Intro <---       """

# class details:
#     name="RIZWAN"
#     age=19
# obj1=details()
# print(obj1.name)
# print(obj1.age)

# class details:
#     name="Rizwan"
#     age=19
#     def info(self):
#         print(f"my age {self.age} and name {self.name}")
# obj1=details()
# obj2=details()
# obj3=details()
# obj2.name="RIZ"
# obj2.age=19.8
# obj1.info()
# obj2.info()
# obj3.info()

# class details:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def info(self):
#         print(f"my name {self.name},my age {self.age}")
# a=details("RIZ",19)
# a.info()

# class details:
#     def __init__ (self):    
#         print("Hey I am good!!")
# obj1=details()

# class details:
#     def __init__ (self,name,place):
#         self.name=name
#         self.place=place
#     def info(self):
#         print(f"{self.name} lives in {self.place}")
# a=details("RIZ","DELHI.")
# b=details("intel","brain.")
# a.info()
# b.info()



"""       ---> Decorators in python <---       """



# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
# @greet
# def hello():
#     print("hello world")
# hello()


# def greet(func):
#     def mfx():
#         print("Before the function.")
#         func()
#         print("After the function.")
#     return mfx
# # @greet
# def hello():
#     print("Hello World!")
# greet(hello)()


# def suit(fx):
#     def mfx(*args,**kwargs) :
#         print("Before addition.")
#         fx(*args,**kwargs)
#         print("After addition.")
#     return mfx
# def Addtion(a,b):
#     print(a+b)
# suit(Addtion)(5,6)


# def suit(fx):
#     def mfx(*args,**kwargs) :
#         print("Before addition.")
#         fx(*args,**kwargs)
#         print("After addition.")
#     return mfx
# @suit
# def Addtion(a,b):
#     print(a+b)
# Addtion(5,6)


# def log_function_execution(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} execution complete.")
#         return result
#     return wrapper
# @log_function_execution
# def add_numbers(a, b):
#     return a + b
# @log_function_execution
# def multiply_numbers(a, b):
#     return a * b
# # Testing the decorated functions
# result_add = add_numbers(3, 5)
# result_multiply = multiply_numbers(2, 4)

# print(f"Result of add_numbers: {result_add}")
# print(f"Result of multiply_numbers: {result_multiply}")



"""       ---> Getter and Setter in python <---       """



# class Myclass:
#     def __init__(self,value):
#         self._value=value
#     @property
#     def value(self):
#         return 10*self._value
# obj=Myclass(10)
# print(obj.value)

# class Myclass:
#     def __init__(self,value):
#         self._value=value
#     @property
#     def value(self):
#         return 5*self._value
#     @value.setter
#     def value(self,new_value):
#         self._value=new_value/3
# obj=Myclass(10)
# obj.value=27
# print(obj.value)



"""       --->     Inheritance in python     <---       """


# class animal:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"Animal name and age : {self.name} , {self.age}")
# class domestic(animal):
#     def myinfo(self):    
#         print(f"{self.name} is also my pet and he is  {self.age+1} year old.")
# a1=animal("lion",6)
# a2=domestic("dog",2)
# a1.info()
# a2.info()
# a2.myinfo()



"""       --->    Access Modifier in python    <---       """



# class student:
#     def __init__ (self):
#         self._name="RIZ"
#     def _funName(self):
#         return "SAIFI"
# class subject(student):
#     pass
# obj=student()
# obj1=subject()
# print(obj._name)
# print(obj._funName())
# print(obj1._name)
# print(obj1._funName())

