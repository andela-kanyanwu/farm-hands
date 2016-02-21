// gulp
var gulp = require('gulp');

// plugins
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var clean = require('gulp-clean');
var browserSync = require('browser-sync');
var browserify = require('gulp-browserify');
var historyApiFallback = require('connect-history-api-fallback');
var concat = require('gulp-concat');

var less = require('gulp-less');
var path = require('path');
var lessInput = ['./ngclient/src/less/site.less'];
var lessOutput = './ngclient/dist/css';
var LessPluginCleanCSS = require('less-plugin-clean-css'),
    LessPluginAutoPrefix = require('less-plugin-autoprefix'),
    cleancss = new LessPluginCleanCSS({ advanced: true }),
    autoprefix = new LessPluginAutoPrefix({ browsers: ["last 2 versions"] });
var lessOptions = {
  paths: [ path.join(__dirname, 'less', 'includes') ],
  plugins: [autoprefix, cleancss]
};
var imagemin = require('gulp-imagemin');
var pngquant = require('imagemin-pngquant');

// tasks
gulp.task('lint', function() {
  gulp.src(['./ngclient/src/**/*.js', '!./ngclient/bower_components/**'])
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
    .pipe(jshint.reporter('fail'));
});
gulp.task('clean', function() {
    gulp.src('./ngclient/dist/*')
      .pipe(clean({force: true}));
    gulp.src('./ngclient/dist/js/bundled.js')
      .pipe(clean({force: true}));
});
gulp.task('minify-css', function() {
  var opts = {comments:true,spare:true};
  gulp.src(['./ngclient/src/**/*.css', '!./ngclient/bower_components/**'])
    .pipe(minifyCSS(opts))
    .pipe(gulp.dest('./ngclient/dist/'))
    .pipe(browserSync.reload({stream: true}));
});
gulp.task('minify-js', function() {
  gulp.src(['./ngclient/**/*.js', '!./ngclient/bower_components/**'])
    .pipe(uglify({
      // inSourceMap:
      // outSourceMap: "app.js.map"
    }))
    .pipe(gulp.dest('./dist/'));
});
gulp.task('copy-bower-components', function () {
  gulp.src('./ngclient/src/bower_components/**')
    .pipe(gulp.dest('./ngclient/dist/bower_components'));
});
gulp.task('copy-img-files', function () {
  gulp.src(['./ngclient/src/img/*.*'])
  .pipe(imagemin({
      progressive: true,
      svgoPlugins: [
          {removeViewBox: false},
          {cleanupIDs: false}
      ],
      use: [pngquant()]
    }))
    .pipe(gulp.dest('./ngclient/dist/img'))
    .pipe(browserSync.reload({stream: true}));
});
gulp.task('copy-html-files', function () {
  gulp.src(['./ngclient/src/**/*.html', './ngclient/src/*.html'])
    .pipe(gulp.dest('./ngclient/dist/'))
    .pipe(browserSync.reload({stream: true}));
});
gulp.task('watch', function(){
  gulp.watch(['./ngclient/src/**/*.html', './ngclient/src/*.html'], ['copy-html-files']);
  gulp.watch(['./ngclient/src/img/*.*'], ['copy-img-files']);
  gulp.watch(['ngclient/src/js/main.js', 'ngclient/src/**/*.js'], ['browserify']);
  gulp.watch(['./ngclient/src/**/*.css', '!./ngclient/bower_components/**'], ['minify-css']);
  gulp.watch('./ngclient/src/less/*.less', ['less-compile']);
})
gulp.task('connect', function () {
  browserSync({
      server: {
        baseDir: './ngclient/dist',
        // This allows for consistent instance of angular app route on direct visit of a state
        // This issue was well explained on the link below.
        // https://github.com/BrowserSync/browser-sync/issues/204#issuecomment-60410751
        middleware: [ historyApiFallback() ]
      },

      port: 5555
    });
});
// gulp.task('connectDist', function () {
//   connect.server({
//     root: 'ngclient/dist/',
//     port: 9999
//   });
// });
gulp.task('browserify', function() {
  gulp.src(['ngclient/src/js/main.js'])
  .pipe(browserify({
    insertGlobals: true,
    debug: true
  }))
  .pipe(concat('bundled.js'))
  .pipe(gulp.dest('./ngclient/dist/js'))
  .pipe(browserSync.reload({stream: true}));
});
gulp.task('browserifyDist', function() {
  gulp.src(['ngclient/src/js/main.js'])
  .pipe(browserify({
    insertGlobals: true,
    debug: true
  }))
  .pipe(concat('bundled.js'))
  .pipe(gulp.dest('./ngclient/dist/js'));
});
gulp.task('less-compile', function () {
  return gulp
    .src(lessInput)
    .pipe(less(lessOptions))
    .pipe(gulp.dest(lessOutput))
    .pipe(browserSync.reload({stream: true}));
});

// *** default task *** //

gulp.task('default',['browserify','copy-html-files', 'copy-img-files', 'minify-css', 'copy-bower-components', 'connect', 'less-compile', 'watch']);
// *** build task *** //

