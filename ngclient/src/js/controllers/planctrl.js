module.exports = planCtrl;
function planCtrl($log) {
  var vm = this;
  vm.test = "Testing...";
  $log.debug(vm.test, 'plans');
}
planCtrl.$inject = ['$log'];