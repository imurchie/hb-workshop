"use strict";

var gulp = require('gulp'),
    path = require('path'),
    jshint = require('gulp-jshint'),
    jshintStylish = require('jshint-stylish'),
    jscs = require('gulp-jscs');

var JS_SOURCES = ['*.js', 'bin/**/*.js', 'ci/**/*.js', 'new-ci/**/*.js', 'lib/**/*.js', 'test/**/*.js'];

gulp.task('jshint', function () {
  return gulp.src(JS_SOURCES)
    .pipe(jshint())
    .pipe(jshint.reporter(jshintStylish))
    .pipe(jshint.reporter('fail'));
});
    
gulp.task('jscs', function () {
  return gulp.src(JS_SOURCES)
    .pipe(jscs({configPath: __dirname + '/.jscsrc'}));
});

gulp.task('lint', ['jshint', 'jscs']);

