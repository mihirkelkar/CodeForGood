var iMentor = angular.module('iMentor', []);

var hostUrl = function (uri) {
  var BASE_URL = 'http://ec2-54-80-8-90.compute-1.amazonaws.com';

  return BASE_URL + uri;
};

iMentor.controller('homeController', ['$scope', '$http', function ($scope, $http) {
  $scope.current_user = {};
  $scope.messages = {};
  $scope.raw_response = {};

  $scope.getUserProfile = function () {
    var url = hostUrl('/user/1');
    $http({
      url: url,
      method: 'GET',
      data: $scope.post_request
    }).success(function (data) {
      $scope.current_user = data;
      console.log(data);
    });
  };

  $scope.getMessages = function () {
    var url = hostUrl('/user/1/messages/');
    $http({
      url: url,
      method: 'GET',
    }).success(function (data) {
      $scope.messages = data;
      console.log(data);
    });
  };

  $scope.sendMessage = function () {
    $http({
      url: hostUrl('/user/1/messages/send/'),
      method: 'POST',
      data: $scope.post_request
    }).success(function (data) {
      console.log('sent this data:');
      console.log(data);
      $scope.raw_response = data;
    }).error(function (data) {
      console.log('sent this data:');
      console.log(data);
      $scope.raw_response = data;
    });
  }
}]);

iMentor.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('<<');
  $interpolateProvider.endSymbol('>>');
});