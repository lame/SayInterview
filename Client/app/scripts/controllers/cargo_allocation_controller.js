angular.module('SayApp').controller('CargoAllocationController', ["$scope", "$element", "$compile", "$http", "$q", "cargoAllocationService", function($scope, $element, $compile, $http, $q, cargoAllocationService){

    var vm = this;

    vm.calcCargo = function() {

        var in_data = $.param({
            json: JSON.stringify({
                sports_car_count: vm.data.sports_car_count,
                family_car_count: vm.data.family_car_count,
                truck_count: vm.data.truck_count,
                minivan_count: vm.data.minivan_count,
                cargo_van_count: vm.data.cargo_van_count,
                total_weight: vm.data.total_weight
            })
        })

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
