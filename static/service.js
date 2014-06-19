memorySearch.factory('Memory', ['$resource', function($resource){
    return $resource('/memory', {}, {
    	search: {method: 'POST', isArray: true}
    });
}]);
