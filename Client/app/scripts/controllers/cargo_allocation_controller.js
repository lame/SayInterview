angular.module('SayApp').controller('CargoAllocationController', ["$scope", "$element", "$compile", "$http", "$q", "cargoAllocationService", function($scope, $element, $compile, $http, $q, cargoAllocationService){

    var vm = this;

    vm.calcCargo = function() {

        var in_data = JSON.stringify({
            "sports_car_count": parseInt(vm.data.sports_car_count, 10) || 0,
            "family_car_count": parseInt(vm.data.family_car_count, 10) || 0,
            "truck_count": parseInt(vm.data.truck_count, 10) || 0,
            "minivan_count": parseInt(vm.data.minivan_count, 10) || 0,
            "cargo_van_count": parseInt(vm.data.cargo_van_count, 10) || 0,
            "total_weight": parseInt(vm.data.total_weight, 10) || 0
        })
        console.log('indata: ', in_data)
        cargoAllocationService.postJson(in_data)
            .success(function(data, status, headers, config) {
                console.log('success', status);
                console.log('response', data);
                vm.response = data
            })
            .error(function(data, status, headers, config) {
                console.log('error', status);
            });
    };
}]);
