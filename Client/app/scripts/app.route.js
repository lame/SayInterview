(function() {
  'use strict';
  angular.module('SayApp')
  .config(['$stateProvider','$urlRouterProvider', '$locationProvider',
           function ($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise('landing');

    $stateProvider
    .state('cargo_allocation', {
      url:'/cargo_allocation',
      templateUrl: 'views/cargo_allocation_view.html',
      controller: 'CargoAllocation'
    })

    .state('landing', {
      url:'/landing',
      templateUrl: 'views/landing.html'
    })

  }]);
})();
