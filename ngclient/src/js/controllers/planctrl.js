module.exports = planCtrl;
function planCtrl($log, planDetail) {
  var vm = this;
  vm.detail = planDetail.data;
  $log.debug(vm.detail);
}
planCtrl.$inject = ['$log', 'planDetail'];