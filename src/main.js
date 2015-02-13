/* global window, document */
'use strict';

(function () {
  window.add = function (num1, num2) {
    return num1 + num2;
  };
  window.subtract = function (num1, num2) {
    return num1 - num2;
  };
  window.updateAppState = function (state) {
    window.history.pushState(state || {}, document.title, 'newstate');
  };


  // string functions
  window.reverse = function (str) {
    return str.split('').reverse().join('');
  };
  window.upcase = function (str) {
    return str.toUpperCase();
  };
  window.downcase = function (str) {
    return str.toUpperCase();
  };
  window.randomize = function(str){
    // Fisher-Yates shuffle algorithm
    array=str.split('')
    for (var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
    return array;
  };
})();

