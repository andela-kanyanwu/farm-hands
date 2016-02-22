module.exports = mainCtrl;
function mainCtrl($log, plans) {

  var vm = this;
  $log(vm.plans);
  vm.plans = plans
  //vm.plans = plans;
  $log.debug('tested..')
  $log.debug(vm.plans);
  vm.test = "Testing...";
  vm.scrollToFinder = scrollToFinder;

  function scrollToFinder() {
	var $sel = angular.element;
	$sel('html, body').animate({
		scrollTop: $sel('.plan-list-header').offset().top - 80
	}, 2000);
  }

  $log.debug("required!");
  $log.debug(vm.test, 'something else');
}
mainCtrl.$inject = ['$log', 'plans'];