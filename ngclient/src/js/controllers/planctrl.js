module.exports = planCtrl;
function planCtrl($log) {
  var vm = this;
  vm.test = "Testing...";
  $log.debug("required!");
  $log.debug(vm.test, 'something else');
}
planCtrl.$inject = ['$log'];