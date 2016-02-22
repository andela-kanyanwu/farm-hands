module.exports = mainCtrl;
function mainCtrl($log, plans) {

  var vm = this;
  vm.plans = plans;
  vm.scrollToFinder = scrollToFinder;
  vm.mapFarmSize = mapFarmSize;

  function mapFarmSize(farmSize) {
    var farmSizes = {
      'S': 'Small',
      'M': 'Medium',
      'L': 'Large'
    };
    return farmSizes[farmSize];
  }

  function scrollToFinder() {
	var $sel = angular.element;
	$sel('html, body').animate({
		scrollTop: $sel('.plan-list-header').offset().top - 80
	}, 2000);
  }

}
mainCtrl.$inject = ['$log', 'plans'];