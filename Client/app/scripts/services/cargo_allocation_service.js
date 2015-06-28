(function(){

    angular.module('SayApp').factory('cargoAllocationService', cargoAllocationService);
    cargoAllocationService.$inject = ['$http', '$q', '$log'];

    function cargoAllocationService($http){

        var cargoAllocationService = {
            postJson: postJson,
        };
        return cargoAllocationService;

        function postJson(in_data){
            var url = "http://localhost:5000/api/calc_cargo";
            return $http.post(url, in_data)
        }

    }

})();
