(function() {

  'use strict';
  require('angular');
  require('angular-route');
  require('angular-animate');
  require('angular-ui-router');

  var mainCtrl = require('./controllers/mainctrl');
  var planCtrl = require('./controllers/planctrl');
  var cropsService = require('./services/crops');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl)
  .factory('Crops', cropsService);

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
          url:'/auth',
          controller: "MainController",
          controllerAs: "main",
          template: '<ui-view/>'
        })
        .state("auth.login", {
          url: '/login',
          templateUrl: "./partials/login.html"
        })
        .state("auth.signup", {
          url: '/signup',
          templateUrl: "./partials/signup.html"
        });
      $urlRouterProvider.otherwise('/');
    }
  //Load controller


}());
