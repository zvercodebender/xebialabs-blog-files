angular.module('myRepo', []).config(function ($httpProvider) {

    // The following code retrieves credentials from the main XL Deploy application
    // and tells AngularJS to append them to every request.
    var flexApp = parent.document.getElementById("flexApplication");
    if (flexApp) $httpProvider.defaults.headers.common.Authorization = flexApp.getBasicAuth();

}).controller('RepoController', function ($http, $scope) {

    $scope.activeRoot = 'Applications';

    $scope.loadCis = function() {
        // This request will trigger execution of
        // src/main/python/ui_extension_demo/cis.py
        $http.get('/api/extension/test/cis', {"params": {"root": $scope.activeRoot}}).then(
            function (response) {
                // response.data.entity is the serialized version of what Jython script puts into
                // response.entity in the script.
                $scope.resultCis = response.data.entity;
            });
    };

    $scope.loadCis();
});
