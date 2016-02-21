(function () {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  require('angular-ui-router');

  var mainCtrl = require('./controllers/mainctrl');
  var planCtrl = require('./controllers/planctrl');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl);

  configure.$inject = ['$locationProvider', '$urlRouterProvider', '$stateProvider'];
    function configure($locationProvider, $urlRouterProvider, $stateProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      // routes
      $stateProvider
        .state("index", {
          url: '/',
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
          abstract: true,
          controller: "MainController",
          controllerAs: "main"
        })
        .state("auth.login",{
          url: '/auth/login',
          templateUrl: "./partials/auth.html"
        })
        .state("auth.signup",{
          url: '/auth/signup',
          templateUrl: "./partials/auth.html"
        });
      $urlRouterProvider.otherwise('/');
    }
  //Load controller


}());
