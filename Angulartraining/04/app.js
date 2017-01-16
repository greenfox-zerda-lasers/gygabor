

var angularPractice = angular.module('angularPractice', []);


angularPractice.controller('PracticeController', function($scope){

  $scope.message = "Wow";
  $scope.persons = [
    {
      name: 'Lajos',
      color: 'red'
    },
    {
      name: 'Mari',
      color: 'blue'
    },
    {
      name: 'Gizi',
      color: 'black'
    },
    {
      name: 'Feri',
      color: 'yellow'
    }
  ]

});
