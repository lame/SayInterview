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

        for x in in_data:
            if x == 'sports_car_count':
                for count in range(in_data[x]):
                    vehicle_list.append(SportsCar())
            elif x == 'family_car_count':
                for count in range(in_data[x]):
                    vehicle_list.append(FamilyCar())
            elif x == 'truck_count':
                for count in range(in_data[x]):
                    vehicle_list.append(Truck())
            elif x == 'minivan_count':
                for count in range(in_data[x]):
                    vehicle_list.append(MiniVan())
            elif x == 'cargo_van_count':
                for count in range(in_data[x]):
                    vehicle_list.append(CargoVan())
            else:
                resp = { 'status_code': 500,
                         'message': 'unrecognized value {0}'.format(x)
                       }
                return jsonify(resp)

            tup = self.calc_cargo(remainder_weight, vehicles_list)
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
        self.vehicle_type = 'SportsCar'
        self.weight_limit = 100


class FamilyCar(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'FamilyCar'
        self.weight_limit = 300


class Truck(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Truck'
        self.weight_limit = 1500


class MiniVan(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'MiniVan'
        self.weight_limit = 200


class CargoVan(Vehicle):

    def __init__(self):
        super().__init__()
        self.vehicle_type = 'CargoVan'
        self.weight_limit = 800

