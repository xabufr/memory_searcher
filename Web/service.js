memorySearch.factory('Memory', ['$resource', function($resource){
    return $resource('url', {}, {
        //actions (default: get, save, query, remove, delete
    })
}]);