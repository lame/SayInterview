from config import api
from resources.calc_cargo_resource import CalcCargo

api.add_resource(CalcCargo, '/', '/api/calc_cargo')
