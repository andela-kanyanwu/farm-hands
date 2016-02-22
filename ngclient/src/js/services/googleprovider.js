module.exports = GoogleAuth;

function GoogleAuth() {
    this.appConfig = {};
    this.setAppConfig = function(object) {
      this.appConfig = object;
    };
    this.$get = ['$log', function($log) {
      function getUserInfo(authResponse, cb) {
        if (authResponse.status.signed_in) {
          $log.debug(authResponse.status);


            gapi.client.load('oauth2', 'v2', function() {
              gapi.client.oauth2.userinfo.get()
                .execute(function(resp) {
                  $log.debug(resp);
                  cb(null, resp);
                });
            });
        } else {
          $log.debug('not logged in');
          cb('Not logged in');
        }
      }
      var appConfig = this.appConfig;
      return {
        init: function() {
          (function() {
            var po = document.createElement('script');
            po.type = 'text/javascript';
            po.async = true;
            po.src = 'https://apis.google.com/js/auth:plusone.js?onload=startApp';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(po, s);
          })();
          (function() {
            var po = document.createElement('script');
            po.type = 'text/javascript';
            po.async = true;
            po.src = 'https://apis.google.com/js/client:platform.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(po, s);
          })();

        },
        login: function(cb) {
          gapi.auth.signIn({
            'callback': function(authResponse) {
              getUserInfo(authResponse, cb);
            },
            'clientid': appConfig.CLIENTID,
            'scope': appConfig.SCOPE,
            'theme': 'dark',
            'cookiepolicy': appConfig.COOKIEPOLICY || 'single_host_origin',
            'accesstype': 'token'
          });

        }
      };

    }];

  };
