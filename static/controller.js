memorySearch.controller("SearchCtrl", ['$scope', '$location','Memory', function($scope, $location, Memory){
    	$scope.results = [];
	$scope.advencedSearchVisible = false;
	$scope.researchedValue = "";
	$scope.researchedValues = {
		'metadata.title': "",
		'metadata.author': "",
		'metadata.content': ""
	};

	$scope.advencedSearchVisibility = function(){
		$scope.advencedSearchVisible = !$scope.advencedSearchVisible;
	}

	$scope.retriveMemory = function(){
		var value = $scope.researchedValue;
		Memory.search({search: value}, function(data){
			$scope.results = [];
			for (var i in data)
			{
				var result = data[i].metadata;
				result.id = data[i].id;
				result.year = (new Date(data[i].metadata.date)).getFullYear();
				$scope.results.push(result);
			}
		});
	};

	$scope.retriveMemoryFromFields = function(){
		Memory.search($scope.researchedValues, function(data){
			$scope.results = [];
			for (var i in data)
			{
				var result = data[i].metadata;
				result.id = data[i].id;
				result.year = (new Date(data[i].metadata.date)).getFullYear();
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
		$scope.result = data.metadata;
		$scope.result.content = data.content;
	});
}]);
