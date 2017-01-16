

var angularPractice = angular.module('angularPractice', []);


angularPractice.controller('PracticeController', function($scope){

  $scope.message = "Wow";
  $scope.tasks = ['Lajos', 'Mari', 'Gizi', 'Feri'];

});
