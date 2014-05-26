memorySearch.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/',{
        templateUrl: "../views/search.html",
        controller: "Search"
    }).otherwise({rediretTo:"/"});
}]);