module.exports = authCtrl;
function authCtrl($log, google, $rootScope) {
  var vm = this;
  vm.googleLogin = function(){
    google.login(function(res){
        $rootScope.currentUser = res;
    })
  }
  vm.test = "Testing...";
  $log.debug(vm.test, 'auth');
}
authCtrl.$inject = ['$log', 'google', '$rootScope'];