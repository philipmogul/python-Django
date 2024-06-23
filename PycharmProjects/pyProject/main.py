
class hello:
    name = "Philip Mumo"
    age = 30
    occupation = "Professional Software Developer & Investor"
    mood = "Gogetter"

    def hey(self):
        self.title = "Methods title."
        print(self.title)
        print("Welcome to Python Programing!")

    def adding(self):
        a = 1000
        b = 60000
        c = a + b
        print("The Goal is = ", c)

    def minus(self):
        final = 61000
        principal = 500
        profit = final - principal
        print("The Goal is = ", profit)

helloObj = hello()
helloObj.hey()
print(helloObj.name)
print(helloObj.age)
print(helloObj.occupation)
print(helloObj.mood)
helloObj.adding()
helloObj.minus()
