(function(){
  // var application = angular.module('application', [
  //
  // ]);

  var app = angular.module('app', []);

  var gem = { name: 'Azurite', price: 2.95 };
  app.controller('StoreController', function() {
    this.product = gem;
  });
})();
