module.exports = PlanService;

function PlanService($http, $q) {

    this.all = function() {
        var deffered = $q.defer();
        $http.get('http://localhost:8000/api/v1/plans').then(function(res){
            deffered.resolve(res);
        }, function(err) {
            deffered.reject(err);
        });

        return deffered.promise;
    }

    this.find = function(id) {
        var deffered = $q.defer();
        $http.get('http://localhost:8000/api/v1/plans/'+id).then(function(res){
            deffered.resolve(res);
        }, function(err) {
            deffered.reject(err);
        });
        return deffered.promise;
    }

}
PlanService.$inject = ['$http', '$q'];