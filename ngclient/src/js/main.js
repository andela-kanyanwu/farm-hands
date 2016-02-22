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
  var durationFilter = require('./filters/momentFilter');

  angular.module('FarmHandsApp', ['ui.router', 'ngAnimate'])

  .run(runBlock)
  .config(configure)
  .controller('MainController', mainCtrl)
  .controller('PlanController', planCtrl)
  .controller('AuthController', authCtrl)
  .filter('durationFilter', durationFilter)
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
        .state("plan", {
          url: '/plans/{id:int}',
          templateUrl: "partials/plan_details.html",
          controller: "PlanController",
          controllerAs: "plan",
          resolve:{
            planDetail: ['PlanService', '$stateParams', function(PlanService, $stateParams){
              return PlanService.find($stateParams.id)
                .then(function(resp) {
                  return resp
              }, function(err){
                return(err)
              });

            }]
          }
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
