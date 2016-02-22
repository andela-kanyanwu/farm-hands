(function() {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  require('angular-ui-router');

  var mainCtrl = require('./controllers/mainctrl');
  var planCtrl = require('./controllers/planctrl');
  var planService = require('./services/plans');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl)
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
                  return resp
              }, function(err){
                return(err)
              });

            }]
          },
          templateUrl: "./partials/home.html",
          controller: "MainController",
          controllerAs: "main"
        })
        .state("plans", {
          url: '/plans',
          templateUrl: "./partials/plans.html",
          controller: "PlanController",
          controllerAs: "plan"
        })
        .state("plans.detail", {
          url: '/plans/:id',
          templateUrl: "./partials/plan_details.html",
          controller: "PlanController",
          controllerAs: "plan"
        })
        .state("auth", {
          url:'/login',
          templateUrl: "./partials/login.html"
        })
        .state("signup", {
          url: '/signup',
          templateUrl: "./partials/signup.html"
        })
      $urlRouterProvider.otherwise('/');
    }
  //Load controller


}());
