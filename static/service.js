memorySearch.factory('Memory', ['$resource', function($resource){
    return $resource('/memory/:id', {id: "@id"}, {
    	search: {method: 'POST', isArray: true}
    });
}]);
