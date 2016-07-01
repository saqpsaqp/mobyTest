angular.module('testService', [])//Declaramos el modulo
	.factory('testRequest', function($http) { //declaramos la factory
		var path = "http://localhost:8000/api/";//API path
		return {
			//Login
			causes : function(){ //Retornara la lista de posts
				global = $http.get(path+'causes.json');
				return global;
			},
			cause : function(id){ //retornara el post por el id
				global = $http.get(path+'causes/'+id);
				return global;	
			}	
		}
	});