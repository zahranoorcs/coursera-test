//ng-route =>If you want to navigate to different pages in your application, but
//you also want the application to be a SPA (Single Page Application),
//with no page reloading, you can use the ngRoute module.


var app = angular.module("CrudDemoApp",["CrudDemoApp.controllers","ngRoute"]);

 app.config(["$routeProvider",function($routeProvider){
   $routeProvider
   .when("/" , {
     templateUrl:"/partials/PlayerList.html",
     controller:"MainController"}).
     otherwise({redirectTo:"/"});
 }])
