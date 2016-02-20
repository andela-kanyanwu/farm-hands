module.exports = mainCtrl;
function mainCtrl($log) {
  var vm = this;
  vm.test = "Testing...";
  $log.debug("required!");
  $log.debug(vm.test, 'something else');
}
mainCtrl.$inject = ['$log'];