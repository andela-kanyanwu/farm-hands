(function() {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  require('angular-ui-router');

  var mainCtrl = require('./controllers/mainctrl');
  var planCtrl = require('./controllers/planctrl');
  var authCtrl = require('./controllers/authctrl');
  var planService = require('./services/plans');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl)
  .controller('AuthController', authCtrl)
  .service('PlanService', planService);

  configure.$inject = ['$locationProvider', '$urlRouterProvider', '$stateProvider'];
    function configure($locationProvider, $urlRouterProvider, $stateProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      // routes
      $stateProvider
        .state("index", {
          url: '/',
          resolve:{
            plans: ['PlanService', function(PlanService){
              return PlanService.all()
                .then(function(resp) {
                  return resp || 'error';
              });

            }]
          },
          templateUrl: "partials/home.html",
          controller: "MainController",
          controllerAs: "main"
        })
        .state("plans", {
          url: '/plans',
          templateUrl: "partials/plans.html",
          controller: "PlanController",
          controllerAs: "plan"
        })
        .state("plans.detail", {
          url: '/plans/:id',
          templateUrl: "partials/plan-details.html",
          controller: "PlanController",
          controllerAs: "plan"
        })
        .state("login", {
          url: '/login',
          templateUrl: "partials/login.html",
          controller: "AuthController",
          controllerAs: "auth"
        })
        .state("signup", {
          url: '/signup',
          templateUrl: "partials/signup.html",
          controller: "AuthController",
          controllerAs: "auth"
        });
      $urlRouterProvider.otherwise('/');
    }
  //Load controller

}());
