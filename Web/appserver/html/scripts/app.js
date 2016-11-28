
var app = angular.module('appserver', [
    'angularModalService',
    'ngResource',
    'ngSanitize',
    'ngRoute',
    'ngAnimate'
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


app.controller('AlertCtrl', function ($scope, $element, close, text)
{
	$scope.text = text;

    $scope.close = function(result) {
 	  close(result, 500);  // close, but give 500ms for bootstrap to animate
	};
});

app.controller('LoginCtrl', function ($scope, $element, close)
{
	$scope.username = null;
	$scope.password = null;

    $scope.cancel = function(){
	//  Manually hide the modal.
	$element.modal('hide');	
	close({
	username: null,
	password: null
	}, 500);  // close, but give 500ms for bootstrap to animate
    };

    $scope.close = function() {
 	  close({
		username: $scope.username,
		password: $scope.password
		}, 500);  // close, but give 500ms for bootstrap to animate
	};
});

app.controller('ConfigCtrl', function ($scope, $http, $location, $element, $rootScope, ModalService)
{
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

    $scope.showConfigLogin = function (config) {
	    ModalService.showModal({
	      templateUrl: "views/login_dialog.html",
	      controller: "LoginCtrl"
	    }).then(function(modal) {
	      modal.element.modal();
	      modal.close.then(function(result) {
		if (result.username && result.password)
			$scope.triggerConfig(config,result.username,result.password);
		});
	    });
    };

    $scope.showAlert = function (text) {
	    ModalService.showModal({
	      templateUrl: "views/alert_dialog.html",
	      controller: "AlertCtrl",
		inputs: {text: text}
	    }).then(function(modal) {
	      modal.element.modal();
	      modal.close.then(function(result) {
		});
	    });
    };

    $scope.triggerConfig = function (config,username,password) {
        console.log(config);
	
	var user = {id:0, Username:username, Password:password};

        $http.put('/api/configs/' + config.ID, user).success(function (data) {
		console.log('status changed');

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

		$location.path('//');
        }).error(function (data, status) {
            console.log('Error ' + data)
		$scope.showAlert("Invalid username or password");
        })
    }
});
