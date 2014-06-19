memorySearch.controller("SearchCtrl", ['$scope','Memory', function($scope, Memory){
    	$scope.results = [];
	$scope.researchedValue = "";

	$scope.retriveMemory = function(){
		var value = $scope.researchedValue;
		console.log(value);
		Memory.search({title: value, author: value}, function(data){
			$scope.results = data;
		});
	};
}]);
