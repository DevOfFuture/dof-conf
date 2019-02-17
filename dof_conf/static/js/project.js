/* Project specific Javascript goes here. */

var daysText = $('.value.days');
var hoursText = $('.value.hours');
var minutesText = $('.value.minutes');
var secondsText = $('.value.seconds');

var updateCounter = function() {
    var eventDate = moment(new Date('2019-03-09 08:00'));
    var now = moment(new Date());
    // This is ugly but it will do for now ;-)
    daysText.text(eventDate.diff(now, 'days'));
    hoursText.text(eventDate.subtract(eventDate.diff(now, 'days'), 'days').diff(now, 'hours'));
    minutesText.text(eventDate.subtract(eventDate.diff(now, 'hours'), 'hours').diff(now, 'minutes'));
    secondsText.text(eventDate.subtract(eventDate.diff(now, 'minutes'), 'minutes').diff(now, 'seconds'));
}

$(document).ready(function() {
    $(window).scroll(function() {
        if ($(window).scrollTop() > 100) {
            $('.navbar').removeClass('hidden');
        } else {
            $('.navbar').addClass('hidden');
        }
    });

    // Add smooth scrolling to all links
    $("a").on('click', function(event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "" && $(this.hash).length !== 0) {
        // Prevent default anchor click behavior
        event.preventDefault();

        // Store hash
        var hash = this.hash;

        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800, function(){

            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
        });
        } // End if
    });

    setInterval(function() {
        updateCounter();
    }, 1000);
});
