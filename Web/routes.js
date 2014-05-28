memorySearch.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/',{
        templateUrl: "../views/search.html",
        controller: "SearchCtrl"
    }).otherwise({rediretTo:"/"});
}]);