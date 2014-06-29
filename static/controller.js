memorySearch.controller("SearchCtrl", ['$scope', '$location','Memory', function($scope, $location, Memory){
    	$scope.results = [];
	$scope.advancedSearchVisible = false;
	$scope.researchedValue = "";
	$scope.researchedValues = {
		'metadata.title': "",
		'metadata.author': "",
		'metadata.content': ""
	};

	$scope.advancedSearchVisibility = function(){
		$scope.advancedSearchVisible = !$scope.advancedSearchVisible;
	};

	$scope.retrieveMemory = function(){
		var value = $scope.researchedValue;
		Memory.search({search: value}, function(data){
			$scope.results = [];
			for (var i in data)
			{
				if(!isNaN(i)) {
                    var result = data[i].metadata;
                    result.id = data[i].id;
                    result.year = (new Date(data[i].metadata.date)).getFullYear();
                    $scope.results.push(result);
                }
			}
		});
	};

	$scope.retrieveMemoryFromFields = function(){
		Memory.search($scope.researchedValues, function(data){
			$scope.results = [];
			for (var i in data)
			{
				if(!isNaN(i)) {
                    var result = data[i].metadata;
                    result.id = data[i].id;
                    result.year = (new Date(data[i].metadata.date)).getFullYear();
                    $scope.results.push(result);
                }
			}
		});
	};

	$scope.retrieveMemoryWithId = function(id){
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
