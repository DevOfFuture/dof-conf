/* Project specific Javascript goes here. */

var daysText = $('.value.days');
var hoursText = $('.value.hours');
var minutesText = $('.value.minutes');
var secondsText = $('.value.seconds');

var updateCounter = function() {
    var eventDate = moment(new Date('2019-02:10 08:00'));
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

    setInterval(function() {
        updateCounter();
    }, 1000);
});
