from flask import request, jsonify
from flask_restful import Resource


class CalcCargo(Resource):

    def __init__(self):
        pass

    def post(self):
        in_data = request.get_json(force=True, silent=False)
        vehicles_list = []

        if 'total_weight' in in_data:
            total_weight = in_data['total_weight']
            remainder_weight = in_data['total_weight']
        else:
            resp = {'status_code': 500,
                    'message': 'Total weight not included'}
            return jsonify(resp)

        if 'sports_car_count' in in_data:
            for count in range(in_data['sports_car_count']):
                vehicles_list.append(SportsCar())
        if 'family_car_count'in in_data:
            for count in range(in_data['family_car_count']):
                vehicles_list.append(FamilyCar())
        if 'truck_count' in in_data:
            for count in range(in_data['truck_count']):
                vehicles_list.append(Truck())
        if 'minivan_count' in in_data:
            for count in range(in_data['minivan_count']):
                vehicles_list.append(MiniVan())
        if 'cargo_van_count' in in_data:
            for count in range(in_data['cargo_van_count']):
                vehicles_list.append(CargoVan())

        tup = self.calc_cargo(remainder_weight, vehicles_list)
        print(self.format_output(total_weight, tup[0], tup[1]))
        return jsonify({'status_code': 200,
                        'message': self.format_output(total_weight, tup[0], tup[1])
                      })

    def calc_cargo(self, remainder_weight, vehicles_list):
        for vehicle in vehicles_list:
            if remainder_weight >= vehicle.weight_limit:
                remainder_weight -= vehicle.weight_limit
                vehicle.weight_used = vehicle.weight_limit
            else:
                vehicle.weight_used = remainder_weight
                remainder_weight = 0

        return (remainder_weight, vehicles_list)

    def format_output(self, total_weight, remainder_weight, vehicles_list):
        format_lst = ['allocating {0} lbs of cargo'.format(total_weight)]

        for vehicle in vehicles_list:
            format_lst.append('a {0} with {1} lbs'.format(vehicle.vehicle_type, vehicle.weight_used))
        format_lst.append('we have {0} lbs of cargo left over'.format(remainder_weight))
        print(format_lst)
        return format_lst


class Vehicle(object):
    """
    As this is the 'object oriented' portion of the interview assignment,
    please note that this inheritance structure is to show an object oriented
    paradigm of programming only, it is not particularly necessary or useful
    in this case.
    """
    def __init__(self):
        self.vehicle_type = None
        self.weight_limit = 0
        self.weight_used = 0

class SportsCar(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Sports Car'
        self.weight_limit = 100


class FamilyCar(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Family Car'
        self.weight_limit = 300


class Truck(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Truck'
        self.weight_limit = 1500


class MiniVan(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Mini Van'
        self.weight_limit = 200


class CargoVan(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Cargo Van'
        self.weight_limit = 800

