module.exports = mainCtrl;
function mainCtrl($log, plans) {

  var vm = this;
  vm.plans = plans
  //vm.plans = plans;
  console.log('tested..')
  console.log(vm.plans);
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