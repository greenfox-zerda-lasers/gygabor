var application = angular.module('application', [

]);

var gem = { name: 'Azurite', price: 2.95 };
var app = angular.module('gemStore', []);
application.controller('StoreController', function() {
  this.product = gem;
});
