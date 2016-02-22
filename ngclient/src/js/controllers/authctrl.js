module.exports = authCtrl;
function authCtrl($log, google, $rootScope, $state) {
  var vm = this;
  vm.googleLogin = function(){
    google.login(function(res){
        $rootScope.currentUser = res;
        $state.go('index');
    })
  }
  vm.test = "Testing...";
  $log.debug(vm.test, 'auth');
}
authCtrl.$inject = ['$log', 'google', '$rootScope', '$state'];