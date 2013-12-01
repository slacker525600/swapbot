var swapBotApp = angular.module('swapBotApp', [
  'ngRoute',
  'swapBotControllers'
]);

swapBotApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
            when('/static/index.html', {
              templateUrl: 'static/partials/donation.html',
              controller: 'donationCtrl'
            }).
            otherwise({
              redirectTo: '/static/index.html'
            });
  }]);

swapBotApp.config(function(RestangularProvider) {
  RestangularProvider.setBaseUrl('/api/v1');
});