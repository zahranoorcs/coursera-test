(function(){
'use strict';
angular.module('myApp',[])
       .controller('LunchCheckController', LunchCheckController);

LunchCheckController.$inject = ['$scope'];

function LunchCheckController($scope){
         $scope.menu="";
         $scope.message="";
$scope.lunch_checker = function(){
      var data = $scope.menu;
      if(data == ""){
          $scope.message = "Please enter data first";
      }
      else {
        var splitted_data = data.split(",");
        if(splitted_data.length > 3){
          $scope.message = "Too much!";
        }
        else{
          $scope.message = "Enjoy";
        }
      }
};
     }

})();
