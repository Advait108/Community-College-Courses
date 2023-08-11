/*global describe: false, it: false, expect: false, calcu: false*/
/*jslint browser: true*/
describe("A Basic Calculator Test Site", function() {
  "use strict";
  var DEBUG = true;
  it("calcu should exist", function() {
    expect(calcu).toBeDefined();
  });

  it("buttons should have their onclick event binded to calcu(this.id)", function() {
    var inputs = document.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
      if (inputs[i].type === "button") {
        var button = inputs[i];
        expect(button.onclick).toBeDefined();
        if (button.onclick == null) {
          if (button.lastListenerInfo == null) {
            console.log(
              "You didn't bind a click event for the button:",
              button
            );
            expect(button.lastListenerInfo).toBeDefined();
          } else {
            if (DEBUG) {
              console.log("addEventListeners for button:", button);
            }
            var onclickFunctionString = "";
            var useCaptureOrOptionsString = "";
            button.lastListenerInfo.forEach((listenerInfo, i) => {
              if (DEBUG) {
                console.log(i, listenerInfo);
              }
              if (listenerInfo) {
                if (listenerInfo.listener) {
                  onclickFunctionString += listenerInfo.listener.toString();
                }
                useCaptureOrOptionsString += listenerInfo.useCaptureOrOptions;
              }
            });
            console.log("click event handler:", onclickFunctionString);
            console.log(
              "useCapture boolean or options object:",
              useCaptureOrOptionsString
            );
            expect(onclickFunctionString.indexOf("calcu")).not.toBe(-1);
            expect(onclickFunctionString.indexOf("this.id")).not.toBe(-1);
            expect(useCaptureOrOptionsString.indexOf("false"))
              .withContext(
                "TODO: Your team left out making addEventListener's 3rd argument to be false to indicate you all don't want the event capture phase to be used. " +
                  "\nThat way the code is more compatible across browsers. See: " +
                  "\nhttps://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Event_bubbling_and_capture" +
                  "\nand the useCapture section at: " +
                  "\nhttps://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#Other_notes\n"
              )
              .not.toBe(-1);
          }
        } else {
          var onclickFunctionString = button.onclick.toString();
          expect(onclickFunctionString.indexOf("calcu")).not.toBe(-1);
        }
      }
    }
  });
});
