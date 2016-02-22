module.exports = durationFilter;

function durationFilter() {
    return function (duration) {
        var day = moment().add(duration, 'days');
        // day.add(duration);

        return day.from(moment(), true);
    };
}

durationFilter.$inject = [];