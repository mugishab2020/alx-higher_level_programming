$(document).ready(function () {
    const eventHandler = $('DIV#red_header');
    eventHandler.click(function() {
        const head_element = $('header');

        if (head_element) {
            head_element.css('color', '#FF0000')
        }
        else {
            console.error('Header element is not found')
        }
    });
});