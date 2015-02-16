/* global describe, it, expect, window, beforeEach, beforeAll, afterEach, afterAll */
"use strict";

describe('math', function () {
  beforeAll(function () {
    console.log("Math: beforeAll()");
  });

  afterAll(function () {
    console.log("Math: afterAll()");
  });

  beforeEach(function () {
    console.log("Math: before()");
  });

  afterEach(function () {
    console.log("Math: after()");
  });
  
  it('should add two numbers', function () {
    expect(window.add(1, 2)).toBe(3);
  });

  it('should subtract two numbers', function () {
    expect(window.subtract(2, 1)).toBe(1);
  });
});

describe('updateAppState', function () {
  it('should push a new state into the browser history', function () {
    window.updateAppState({
      message: 'hi'
    });
    expect(window.history.state).toEqual({
      message: 'hi'
    });
  });
});
