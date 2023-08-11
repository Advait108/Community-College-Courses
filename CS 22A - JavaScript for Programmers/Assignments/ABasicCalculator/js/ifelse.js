//Names: Tim Fan, Advait Alluri

// The following comments are settings for various linters
// Not sure if a reported error matters? Look it up at http://linterrors.com/js
/*global math: false, calc: false, console: false, eval: false */

/*jslint es5: true */
/*jslint node: false*/
/*jslint browser: true*/
/*jslint devel: true*/
/*jslint plusplus: true */
/*jslint evil: true */

/*jshint es5: true */
/*jshint globalstrict: true*/
/*jshint jquery: false*/
/*jshint node: false*/
/*jshint browser: true*/
/*jshint devel: true*/

/*eslint-env jquery: false*/
/*eslint-env browser*/
/*eslint no-console: 0*/

// CS22A: A Basic Calculator Part 3 - calcu() function with if-else

var calcu = function(calcValue) {
	"use strict";
	if (calcValue) {
		// calcValue wasn't null or undefined'
		console.log("calcValue:", calcValue);

		if (calcValue === "equate") {
			calc.output.value = math.eval(calc.output.value);
		}
		else if (calcValue === "c") {
			calc.output.value = "";
		}
		else {
			calc.output.value += calcValue;
		}

		// TODO: Add missing code here
	}
};

// TODO: Complete the clickEventHandler function and then below it bind input
// elements' (only those that are buttons) onclick property to clickEventHandler.
// Don't use window.onload!
// Usually using window.onload is a good idea,
// but that prevents the Jasmine test suite from loading and since the
// script tag for ifelse.js must be deferred and there are no big images to
// slow the loading of the HTML elements down it will all work OK without that.
var clickEventHandler = function(event) {
	"use strict";
	// TODO: Add missing code here
	calcu(this.id);
};
// TODO: Add missing code here
var input = document.getElementsByTagName('input');
for (var i = 0; i < input.length; i++) {
	if (input[i].type == 'button') {
		input[i].onclick = clickEventHandler;
	}
}
