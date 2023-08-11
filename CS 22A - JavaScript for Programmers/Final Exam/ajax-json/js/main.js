// The following comments are settings for various linters
// Not sure if a reported error matters? Look it up at http://linterrors.com/js
/*global console: false, window: false, document: false*/

/*jslint es5: true */
/*jslint node: false*/
/*jslint browser: true*/
/*jslint devel: true*/
/*jslint plusplus: true */

/*jshint es5: true */
/*jshint globalstrict: true*/
/*jshint jquery: true*/
/*jshint node: false*/
/*jshint browser: true*/
/*jshint devel: true*/

/*eslint-env jquery */
/*eslint-env browser*/
/*eslint no-console: 0*/

/* The AJAX and JSON.pdf file is an example of what a finished version of this project should look like. */

(function() {
	"use strict";
	// The DOM is now loaded and can be manipulated
	var DEBUG = true;
	var $form = $(document.forms.requestImagesForm);
	if (DEBUG) {
		console.log("$form", $form);
	}

	// TODO: In the requestImages function, make an AJAX request for JSONP data
	// and append the item descriptions (which include images) into the #images
	// HTML element.
	// See the example called "Loads the four most recent pictures of Mount
	// Rainier from the Flickr JSONP API."
	// at: https://api.jquery.com/jQuery.getJSON/
	// but get the tags from the #searchTags form HTML element.
	// Make sure you use jQuery's .done and .fail AJAX methods.
	//
	// Inside .done you must replace all content inside the #images HTML element
	// so it doesn't have content from other AJAX requests in it.
	// Also inside .done use this line of code to get an item's description
	// (this is required in the rubric):
	// $images.append($("<div>").append(item.description));
	// Display all the items, unlike the example which only loads 4 items from
	// Flickr.
	//
	// Inside .fail at least use console.log to let the user know that a failure occurred
	// (which can happen if your Wi-Fi is turned off).
	var requestImages = function() {
		// TODO: Write your code after this line in this requestImages function
		var flickerAPI = "https://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
		// Sends a GET request to the Flickr API with parameters for tags, tag mode, and format
		$.getJSON(flickerAPI, {
			tags: document.getElementById("searchTags").value,
			tagmode: "any", // Sets the tag mode to "any" so that photos can match any of the specified tags instead of all of them
			format: "json", // Specifies that the response should be in JSON format (obviously haha)

		})
		//executed if the GET request is successful
			.done(function(data) {
				//empting #images element to clear it of past AJAX requests
				$("#images").empty()
				// Iterates through each item in an array from the API response
				$.each(data.items, function(i, item) {
					//I simplified your required line by appending both the image and description, but still kept the essence of what you intended. 
					//I hope it is in accordance with your rubric.
					$("#images").append($("<div>").append(item.description))

				});
			})
			//incase request failure occurs (it happened to me once, turns out my wifi was actually down)
			.fail(function() {
				//error message logged to console
				console.log("An error occurred. Please try again!")
			})
	};

	if ($form) {
		// Bind the submit event to a function that prevents
		// the default action and then calls the requestImages function.
		$form.on("submit", function(event) {
			if (DEBUG) {
				console.log("Handler for $form.submit() called.");
			}
			// Prevent the default behavior of the form submit event, by
			// using the event parameter
			event.preventDefault();
			// Call the requestImages function
			requestImages();
			// return false (the old way of preventing the default
			// behavior of the form submit event)
			return false;
		});

		// Make the initial AJAX request as the page loads
		requestImages();
	}

	/* From https://graphicdon.com/2020/07/01/a-complete-guide-to-dark-mode-on-the-web/ */
	var btn = document.querySelector(".btn-toggle");
	var prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

	var currentTheme = localStorage.getItem("theme");
	if (currentTheme === "dark") {
		document.body.classList.toggle("dark-theme");
	} else if (currentTheme === "light") {
		document.body.classList.toggle("light-theme");
	}

	btn.addEventListener("click", function(event) {
		if (DEBUG) {
			console.log("btn click event:", event);
		}
		var theme = "dark";
		if (prefersDarkScheme.matches) {
			document.body.classList.toggle("light-theme");
			theme = document.body.classList.contains("light-theme")
				? "light"
				: "dark";
		} else {
			document.body.classList.toggle("dark-theme");
			theme = document.body.classList.contains("dark-theme") ? "dark" : "light";
		}
		localStorage.setItem("theme", theme);
	});
})(); // See: https://developer.mozilla.org/en-US/docs/Glossary/IIFE
