angular.module('testService', [])
	.factory('testRequest', function($http) { 
		var path = "http://localhost:8000/api/";
		return {
			//Login
			causes : function(){ 
				global = $http.get(path+'causes');
				return global;
			},
			cause : function(id){ 
				global = $http.get(path+'causes/'+id);
				return global;	
			}	
		}
	});