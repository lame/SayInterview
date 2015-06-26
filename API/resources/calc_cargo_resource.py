from flask import request
from flask_restful import Resource


class CalcCargo(Resource):

    def __init__(self):
        pass

    def get(self):
        return {'Hello World': 'sup World'}

    def post(self):
        in_data = request.get_json(force=True, silent=False)
        print(in_data)


# class Vehicle(object):

#     def __init__(self):
#         pass


# class SportsCar(Vehicle):

#     def __init__(self):
#         super().__init__()
#         self.weight_limit = 100


# class FamilyCar(Vehicle):

#     def __init__(self):
#         super().__init__()
#         self.weight_limit = 300


# class Truck(Vehicle):

#     def __init__(self):
#         super().__init__()
#         self.weight_limit = 1500


# class MiniVan(Vehicle):

#     def __init__(self):
#         super().__init__()
#         self.weight_limit = 200


# class CargoVan(Vehicle):

#     def __init__(self):
#         super().__init__()
#         self.weight_limit = 800
