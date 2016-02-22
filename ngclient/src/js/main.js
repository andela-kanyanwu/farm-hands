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
  var googleAuth = require('./services/googleprovider');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .run(runBlock)
  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl)
  .controller('AuthController', authCtrl)
  .service('PlanService', planService)
  .provider('google', googleAuth);
  runBlock.$inject = ['google'];
  function runBlock(google){
    google.init();
  }
  configure.$inject = ['$locationProvider', '$urlRouterProvider', '$stateProvider', 'googleProvider'];
    function configure($locationProvider, $urlRouterProvider, $stateProvider, googleProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      googleProvider.setAppConfig(
    {
      CLIENTID: '570959447139-guockv674o8tblvqml4h3ukq61rv9kqk.apps.googleusercontent.com'
    });
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
          templateUrl: "partials/plan_details.html",
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
