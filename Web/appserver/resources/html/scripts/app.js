
var app = angular.module('appserver', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute'
]);

app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'views/list.html',
        controller: 'ListCtrl'
    }).when('/create', {
        templateUrl: 'views/create.html',
        controller: 'CreateCtrl'
    }).otherwise({
        redirectTo: '/'
    })
});

app.controller('ListCtrl', function ($scope, $http) {
    $http.get('/api/devices').success(function (data) {  
        $scope.devices = data;
    }).error(function (data, status) {
        console.log('Error ' + data)
    })

    $scope.deviceStatusChanged = function (device) {
        console.log(device);
        $http.put('/api/devices/' + device.ID, device).success(function (data) {
            console.log('status changed');
        }).error(function (data, status) {
            console.log('Error ' + data)
        })
    }
    
    $scope.triggerSignal = function (signal) {
        console.log(signal);
        $http.post('/api/triggersignal', signal).success(function (data) {
            $location.path('/');
        }).error(function (data, status) {
            console.log('Error ' + data)
        })
    }
});

app.controller('CreateCtrl', function ($scope, $http, $location) {
    $scope.device = {
        done: false
    };

    $scope.createDevice = function () {
        console.log($scope.device);
        $http.post('/api/devices', $scope.device).success(function (data) {
            $location.path('/');
        }).error(function (data, status) {
            console.log('Error ' + data)
        })
    }
});