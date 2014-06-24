memorySearch.controller("SearchCtrl", ['$scope', '$location','Memory', function($scope, $location, Memory){
    	$scope.results = [];
	$scope.researchedValue = "";

	$scope.retriveMemory = function(){
		var value = $scope.researchedValue;
		Memory.search({title: value, author: value}, function(data){
			$scope.results = [];
			for (var i in data)
			{
				var result = data[i].metadata;
				result.id = data[i].id;
				$scope.results.push(result);
			}
		});
	};

	$scope.retriveMemoryWithId = function(id){
		$location.path("/"+id);
	};
}]);

memorySearch.controller("ViewMemoryCtrl", ['$scope', '$routeParams', 'Memory', function($scope, $routeParams, Memory){
	$scope.result = {};

	Memory.get({id: $routeParams.id}, function(data){
		$scope.result = data;
	});
}]);
