module.exports = authCtrl;
function authCtrl($log) {
  var vm = this;
  vm.test = "Testing...";
  $log.debug(vm.test, 'auth');
}
authCtrl.$inject = ['$log'];