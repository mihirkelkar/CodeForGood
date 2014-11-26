var hostUrl = function (uri) {
  //var BASE_URL = 'http://ec2-54-80-8-90.compute-1.amazonaws.com';
  var BASE_URL = 'http://localhost:8000';
  return BASE_URL + uri;
};

angular.module('iMentor.controllers', [])

.controller('AppCtrl', function($scope) {
})

.controller('RegistrationCtrl', function($scope){

})

.controller('LandingCtrl', function($scope){

})

.controller('MessageCtrl', function($scope, $http, $stateParams){
  $scope.messages = [{}];
  $scope.current_message = {};

  $scope.skills = ["Curiosity",
                   "Optimism",
                   "Help Seeking",
                   "Critical Thinking",
                   "Perseverance",
                   "Growth Mindset",
                   "Social Capital Skills"];

  $scope.getMessages = function () {
    var url = hostUrl('/user/1/messages/');
    $http({
      url: url,
      method: 'GET',
    }).success(function (data) {
      $scope.messages = data;
    });
  };

  $scope.messageDetails = function () {
    var path = '/user/1/messages/' +  $stateParams.id + '/details/';
    var url = hostUrl(path);

    $http({
      url: url,
      method: 'GET',
    }).success(function (data) {
      $scope.message = data;
    })
  }
})



