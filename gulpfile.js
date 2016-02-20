// gulp
var gulp = require('gulp');

// plugins
var connect = require('gulp-connect');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var clean = require('gulp-clean');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');
var runSequence = require('run-sequence');

// tasks
gulp.task('lint', function() {
  gulp.src(['./ngclient/**/*.js', '!./ngclient/bower_components/**'])
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
    .pipe(jshint.reporter('fail'));
});
gulp.task('clean', function() {
    gulp.src('./dist/*')
      .pipe(clean({force: true}));
    gulp.src('./ngclient/js/bundled.js')
      .pipe(clean({force: true}));
});
gulp.task('minify-css', function() {
  var opts = {comments:true,spare:true};
  gulp.src(['./ngclient/**/*.css', '!./ngclient/bower_components/**'])
    .pipe(minifyCSS(opts))
    .pipe(gulp.dest('./dist/'));
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
  gulp.src('./ngclient/bower_components/**')
    .pipe(gulp.dest('dist/bower_components'));
});
gulp.task('copy-html-files', function () {
  gulp.src('./ngclient/**/*.html')
    .pipe(gulp.dest('dist/'));
});
gulp.task('connect', function () {
  connect.server({
    root: 'ngclient/',
    port: 8888
  });
});
gulp.task('connectDist', function () {
  connect.server({
    root: 'dist/',
    port: 9999
  });
});
gulp.task('browserify', function() {
  gulp.src(['ngclient/js/main.js'])
  .pipe(browserify({
    insertGlobals: true,
    debug: true
  }))
  .pipe(concat('bundled.js'))
  .pipe(gulp.dest('./ngclient/js'));
});
gulp.task('browserifyDist', function() {
  gulp.src(['ngclient/js/main.js'])
  .pipe(browserify({
    insertGlobals: true,
    debug: true
  }))
  .pipe(concat('bundled.js'))
  .pipe(gulp.dest('./dist/js'));
});


// // *** default task *** //
// gulp.task('default',
//   ['lint', 'browserify', 'connect']
// );
// // *** build task *** //
// gulp.task('build',
//   ['lint', 'minify-css', 'browserifyDist', 'copy-html-files', 'copy-bower-components', 'connectDist']
// );

// *** default task *** //
gulp.task('default', function() {
  runSequence(
    ['clean'],
    ['lint', 'browserify', 'connect']
  );
});
// *** build task *** //
gulp.task('build', function() {
  runSequence(
    ['clean'],
    ['lint', 'minify-css', 'browserifyDist', 'copy-html-files', 'copy-bower-components', 'connectDist']
  );
});
