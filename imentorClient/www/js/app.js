// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('iMentor', ['ionic', 'iMentor.controllers'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if(window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

    .state('app', {
      url: "/app",
      abstract: true,
      templateUrl: "templates/menu.html",
      controller: 'AppCtrl'
    })
    .state('app.search', {
      url: "/messages/search",
      views: {
        'menuContent' :{
          templateUrl: "templates/message_search.html",
          controller: 'MessageCtrl'
        }
      }
    })
    .state('app.coach', {
      url: "/coach",
      views: {
        'menuContent' :{
          templateUrl: "templates/coach.html"
        }
      }
    })
    .state('app.stats', {
      url: "/stats",
      views: {
        'menuContent' :{
          templateUrl: "templates/stats.html"
        }
      }
    })
    .state('app.messages', {
      url: "/messages",
      views: {
        'menuContent' :{
          templateUrl: "templates/messages.html",
          controller: 'MessageCtrl'
        }
      }
    })
    .state('app.message-details', {
      url: "/messages/details/:id",
      views: {
        'menuContent' :{
          templateUrl: "templates/message.details.html",
          controller: 'MessageCtrl'
        }
      }
    })
    .state('app.landing', {
      url: "/landing",
      views: {
        'menuContent' :{
          templateUrl: "templates/landing.html",
          controller: 'LandingCtrl'
        }
      }
    })
    .state('app.login', {
      url: "/login",
      views: {
        'menuContent' :{
          templateUrl: 'templates/login.html',
          controller: 'LandingCtrl'
        }
      }
    })
    .state('app.register', {
      url: "/register",
      views: {
        'menuContent' :{
          templateUrl: 'templates/register.html',
          controller: 'LandingCtrl'
        }
      }
    })

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/landing')
});

