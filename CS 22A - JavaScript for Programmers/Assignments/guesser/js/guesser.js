// The following comments are settings for various linters
/*jslint es6: true*/ // Causes an "Unexpected 'es6'." warning in JSLint that you should ignore.
/*jshint globalstrict: true*/
/*jshint esversion: 6 */
/*jshint jquery: false*/
/*jshint node: false*/
/*jshint browser: true*/
/*jshint devel: true*/
/*eslint-env es6*/
/*eslint-env jquery: false*/
/*eslint-env browser*/
/*eslint no-console: 0*/

/*
 * INSTRUCTIONS:
 * Make a guessing game where the computer guesses what the human user's
 * number is between 0 and 100 (inclusive). Do NOT use Arrays,
 * do NOT use a linear search algorithm, and do NOT use the prompt functions!
 * Use if-else and confirm("some question") inside the while-loop.
 * The human is expected to click the cancel button to indicate No
 * (and thus the confirm function retuns false)
 * or the OK button to indicate Yes (confirm function returns true).
 * Do NOT change the line "guess = Math.round((min + max) / 2);"
 * because the computer is supposed to guess efficiently by
 * asking the human if their number is higher, lower, or equal to
 * the computer's current guess.
 * Do NOT use break or continue. You can use the "return;" statement inside
 * the while-loop to get the computer to leave the guesser function.
 * For info on how while loops work see:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while
 * For info on how return works see:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return
 */
const guesser = event => {
	let min = 0;
	let max = 100;
	let guess;
	// If this guesser function was called correctly both event.currentTarget
	// and this should be the window object. If event is undefined you probably
	// changed the code at the end of this file even though you are not allowed to.
	console.log("this:", this);
	console.log("event.currentTarget:", event.currentTarget);

	alert("Think of a number betwwen " + min + " and " + max + ". (inclusive)");

	while (min <= max) {
		guess = Math.round((min + max) / 2);

		// DONE: Add your code below here ONLY!

		//ask the user if their number was guessed
		if (confirm("Is your number " + guess + " ? \n\nPress 'OK' for yes, and 'Cancel' for no.")) {
			//the number was guessed
			alert("Yay, I guessed it! Thanks for playing, and reload the page to play again.")
			//the function returns, so the program stops
			return

			//the number was not guessed
		} else {
			//this is for edge cases, where we have hit absolute max or min a number could be, and the user hasn't confirmed a number yet
			
			//asking if the number is higher or lower than the previous guess
			/*
			TODO:
			The above
			 if (guess === 100 || guess === 0)
			and the below
			 if (guess === 1)
			checks are NOT needed!
			We already know the secret number is not guess, 
			so if the secret number is higher than guess then 
			guess + 1 should be the new min, otherwise the secret number is 
			less than guess, so guess - 1 should be the new max.
			That way you code is simpler and you don't break my rule that you
			can't change the code below the
			"Add your code above here ONLY!" comment.
			*/
			if (confirm("Is your number higher or lower? \n\nPress 'OK' for higher, and 'Cancel' for lower.")) {
				//the number was higher, so the current guess was set as the new lowest bound
				min = guess + 1
			} else {
				//the number was lower, so the current guess was set as the new highest bound
				max = guess - 1
				//since the Math.round statement wont ever go lower than 1, I manually make max = 0 once the user has confirmed their number is lower than 0, so that guess will equal 0 on the next while loop iteration
			
			}
		}

		// TODO: Add your code above here ONLY!
	}

	alert("I could not guess your number. I think you are cheating!");
};

window.onload = guesser;
