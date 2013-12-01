var swapBotControllers = angular.module('swapBotControllers', ['restangular']);
 
swapBotControllers.controller('donationCtrl', ['$scope',
  function ($scope, Restangular) {

    $scope.orderProp = 'age';
  }]);
