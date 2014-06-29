memorySearch.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/',{
        templateUrl: "views/search.html",
        controller: "SearchCtrl"
    })
    .when('/:id', {
	templateUrl: "views/memory.html",
    	controller: "ViewMemoryCtrl"
    })
    .otherwise({redirectTo:"/"});

}]);
