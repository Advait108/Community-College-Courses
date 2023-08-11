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
/*jshint jquery: false*/
/*jshint node: false*/
/*jshint browser: true*/
/*jshint devel: true*/

/*eslint-env jquery: false*/
/*eslint-env browser*/
/*eslint no-console: 0*/

/*
 * TODO: Make sure you read this entire file and
 * these Web pages BEFORE you start working!:
 * https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML5_audio_and_video
 * The "HTML Audio/Video Events" section at:
 * http://www.w3schools.com/tags/ref_av_dom.asp
 * https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement
 * Then start below with the "TODO: DO THIS FIRST" section.
 *
 * Complete the code for this file, following the hints in the comments.
 * Start with the "TODO: DO THIS FIRST: section in the MIDDLE of this file!
 * Do complete the code marked by "TODO" comments,
 * but do NOT re-write function/method signatures
 * (a method's signature is its name, parameters,
 * and the order of the parameters).
 */
window.onload = function() {
	"use strict";
	// Getting the media elements
	var mediaElement1 = document.getElementById("mediaElement1");
	var mediaElement2 = document.getElementById("mediaElement2");
	var mediaElement3 = document.getElementById("mediaElement3");
	var mediaElement4 = document.getElementById("mediaElement4");
	// Getting the buttons
	var playOrPauseButton1 = document.getElementById("playOrPauseButton1");
	var playOrPauseButton2 = document.getElementById("playOrPauseButton2");
	var playOrPauseButton3 = document.getElementById("playOrPauseButton3");
	var playOrPauseButton4 = document.getElementById("playOrPauseButton4");
	var stopButton1 = document.getElementById("stopButton1");
	var stopButton2 = document.getElementById("stopButton2");
	var stopButton3 = document.getElementById("stopButton3");
	var stopButton4 = document.getElementById("stopButton4");
	var increaseVolumeButton1 = document.getElementById("increaseVolumeButton1");
	var increaseVolumeButton2 = document.getElementById("increaseVolumeButton2");
	var increaseVolumeButton3 = document.getElementById("increaseVolumeButton3");
	var increaseVolumeButton4 = document.getElementById("increaseVolumeButton4");
	var decreaseVolumeButton1 = document.getElementById("decreaseVolumeButton1");
	var decreaseVolumeButton2 = document.getElementById("decreaseVolumeButton2");
	var decreaseVolumeButton3 = document.getElementById("decreaseVolumeButton3");
	var decreaseVolumeButton4 = document.getElementById("decreaseVolumeButton4");
	

	
	var playOrPauseButtonEventHandler = function(event) {
		console.log("playOrPauseButtonEventHandler called with event:", event);
		var playOrPauseButton = event.target;
		console.log("this:", this);
		var mediaElement;
			
		if (playOrPauseButton === playOrPauseButton1) {
	      mediaElement = mediaElement1;
	    } else if (playOrPauseButton === playOrPauseButton2) {
	      mediaElement = mediaElement2;
	    } else if (playOrPauseButton === playOrPauseButton3) {
	      mediaElement = mediaElement3;
	    } else if (playOrPauseButton === playOrPauseButton4) {
	      mediaElement = mediaElement4;
	    }
	    
	    if (mediaElement.paused) {
	      mediaElement.play();
	      playOrPauseButton.innerHTML = "Pause";
	    } else {
	      mediaElement.pause();
	      playOrPauseButton.innerHTML = "Play";
	    }
	    
	    
	   
	    
	    
	    
	    
	    
	};

	playOrPauseButton1.addEventListener("click", playOrPauseButtonEventHandler, false);
	playOrPauseButton2.addEventListener("click", playOrPauseButtonEventHandler, false);
	playOrPauseButton3.addEventListener("click", playOrPauseButtonEventHandler, false);
	playOrPauseButton4.addEventListener("click", playOrPauseButtonEventHandler, false);

	var stopButtonEventHandler = function(event) {
		var stopButton = event.target;
		var mediaElement;
		
		if (stopButton === stopButton1) {
	        mediaElement = mediaElement1;
	    } else if (stopButton === stopButton2) {
	        mediaElement = mediaElement2;
	    } else if (stopButton === stopButton3) {
			mediaElement = mediaElement3;
		} else if (stopButton === stopButton4) {
			mediaElement = mediaElement4;
		}  
	    else {
	        console.error("Unexpected stop button id: " + stopButton.id);
	        return;
	    }
	    
	    mediaElement.pause();
    	mediaElement.currentTime = 0;
	};

	stopButton1.addEventListener("click", stopButtonEventHandler, false);
	stopButton2.addEventListener("click", stopButtonEventHandler, false);
	stopButton3.addEventListener("click", stopButtonEventHandler, false);
	stopButton4.addEventListener("click", stopButtonEventHandler, false);

	var mediaEventHandler = function(event) {

		var mediaElement = this; 
		console.log("mediaEventHandler called with event:", event);
		console.log("mediaEventHandler called with event.target:", event.target);
		console.log(
			"mediaEventHandler called with event.currentTarget:",
			event.currentTarget
		);
		
		console.log("mediaEventHandler called with this:", this);
		var button;

		if (mediaElement === "video1") {
			button = playOrPauseButton1;
		} else if (mediaElement === "video2") {
			button = playOrPauseButton2;
		} else if (mediaElement === "audio1") {
			button = playOrPauseButton3;
		} else if (mediaElement === "audio2") {
			button = playOrPauseButton4;
		}


		if (mediaElement.paused) {
			button.innerHTML = "Play";
		} else {
			button.innerHTML = "Pause";
		}

		if (event.type === "ended") {
			mediaElement.watched = true;
		}
		if (mediaElement.watched) {
			button.innerHTML = "✅" + button.innerHTML;
		}
	};


	mediaElement1.addEventListener('playing', mediaEventHandler, false);
	mediaElement2.addEventListener('playing', mediaEventHandler, false);
	mediaElement3.addEventListener('playing', mediaEventHandler, false);
	mediaElement4.addEventListener('playing', mediaEventHandler, false);
	
	mediaElement1.addEventListener('pause', mediaEventHandler, false);
	mediaElement2.addEventListener('pause', mediaEventHandler, false);
	mediaElement3.addEventListener('pause', mediaEventHandler, false);
	mediaElement4.addEventListener('pause', mediaEventHandler, false);
	
	mediaElement1.addEventListener('ended', mediaEventHandler, false);
	mediaElement2.addEventListener('ended', mediaEventHandler, false);
	mediaElement3.addEventListener('ended', mediaEventHandler, false);
	mediaElement4.addEventListener('ended', mediaEventHandler, false);

	var increaseVolume = function(mediaElement) {

		if (mediaElement.volume >= 0.9) {
			mediaElement.volume = 1.0;
		} else if (mediaElement.volume < 1.0) {
			mediaElement.volume += 0.1;
		}
		
	};

	increaseVolumeButton1.onclick = function(event) {
		increaseVolume(mediaElement1);
	};
	increaseVolumeButton2.onclick = function(event) {
		increaseVolume(mediaElement2);
	};
	increaseVolumeButton3.onclick = function(event) {
		increaseVolume(mediaElement3);
	};
	increaseVolumeButton4.onclick = function(event) {
		increaseVolume(mediaElement4);
	};

	var decreaseVolume = function(mediaElement) {

		if (mediaElement.volume <= 0.1) {
			mediaElement.volume = 0.0;
		} else if (mediaElement.volume > 0.0) {
			mediaElement.volume -= 0.1;
		}
		
	};

	decreaseVolumeButton1.onclick = function(event) {
		decreaseVolume(mediaElement1);
	};
	decreaseVolumeButton2.onclick = function(event) {
		decreaseVolume(mediaElement2);
	};
	decreaseVolumeButton3.onclick = function(event) {
		decreaseVolume(mediaElement3);
	};
	decreaseVolumeButton4.onclick = function(event) {
		decreaseVolume(mediaElement4);
	};
};
