# import pydantic


class Car():
    model = "BMW"
    engine = 1.6

a = Car()
print(type(a))
print(isinstance(a, Car))
print(a.model)
print(a.__dict__)
print(getattr(a, "eng", 2.0))

setattr(a, "x", [1, 2, 3])
print(a.x)

#delattr(a, "x")
#del a.x

a.model = "Tesla"
print(a.model)

Car.model = "Peugeot"
print(Car.model)
print(a.model)