(function () {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  var mainCtrl = require('./controllers/mainctrl');
  var planCtrl = require('./controllers/planctrl');

  angular.module('FarmHandsApp', ['ngRoute', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl);

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
        .when("/plans", {
          templateUrl: "./partials/plans.html",
          controller: "PlanController",
          controllerAs: "plan"
        })
        .when("/plans/:id", {
          templateUrl: "./plan_details.html",
          controller: "PlanController",
          controllerAs: "plan"
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
