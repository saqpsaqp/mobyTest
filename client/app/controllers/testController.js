angular.module('myApp', ['testService']);

angular.module('myApp').controller('testController', ['$scope','testRequest',testController]);
function testController($scope, testRequest) {
	$scope.name="saul"
	$scope.causes={};
	$scope.getAllCauses = function(){
		testRequest.causes().success(function (data){
			$scope.causes=data; // Asignaremos los datos de todos los posts
			$scope.causes.exist=1;
		});
	}
	$scope.getCause = function(){
		$scope.unCause={};
		testRequest.cause($scope.cause_id).success(function (data){
			$scope.unCause=data; // Asignaremos los datos del post
			$scope.unCause.exist=1;
			$scope.causes.exist=0;
		});
	}
}