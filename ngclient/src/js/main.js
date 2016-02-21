(function () {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  var mainCtrl = require('./controllers/mainctrl');

  angular.module('SampleApp', ['ngRoute', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl);

  configure.$inject = ['$locationProvider', '$routeProvider'];
    function configure($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');
      // routes
      $routeProvider
        .when("/", {
          templateUrl: "./partials/home.html",
          controller: "MainController",
          controllerAs: "main"
        })
        .otherwise({
           redirectTo: '/'
        })
        .when("/signup", {
          templateUrl: "./partials/signup.html",
          controller: "MainController",
          controllerAs: "main"
        })
        .when("/login", {
          templateUrl: "./partials/login.html",
          controller: "MainController",
          controllerAs: "main"
        });
    }
  //Load controller


}());
