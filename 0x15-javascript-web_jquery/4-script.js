$(document).ready(function() {
    // select the div
    const selectedDiv = $('DIV#toggle_header');
    const Element = $('header');

    // add a click event handler
    selectedDiv.click(function () {
        Element.toggleClass('red green');
    });
});
