
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
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl'
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

app.controller('LoginCtrl', function ($scope, $http, $location) {
    $scope.device = {
        done: false
    };
});




app.controller('ConfigCtrl', function ($scope, $http, $location, $rootScope) {
    $http.get('/api/configs').success(function (data) {  
        $scope.configs = data;

	$rootScope.config = data[0];
	for (c of $scope.configs)
	{
		css = document.getElementById(c.Css);
		if (css == null)
		{
			head = document.getElementsByTagName("head")[0];
			new_css = document.createElement('link');
			new_css.id = c.Css;
			new_css.href = "/css/"+c.Css;
			new_css.rel="stylesheet";
			new_css.disabled = !c.Active;
			if (c.Active) $rootScope.config = c;
			head.appendChild(new_css);
		}
	}

    }).error(function (data, status) {
        console.log('Error ' + data)
    })

    $scope.triggerConfig = function (config) {
        console.log(config);

	for (c of $scope.configs)
	{
		css = document.getElementById(c.Css);
		css.disabled = true;
		c.Active = false;
	}

	css = document.getElementById(config.Css);
	css.disabled = false;

	config.Active = true;
	$rootScope.config = config;

        $http.put('/api/configs/' + config.ID, config).success(function (data) {
            console.log('status changed');
		$location.path('//');
        }).error(function (data, status) {
            console.log('Error ' + data)
        })
    }
});
