// Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

// HH = hours, padded to 2 digits, range: 00 - 99
// MM = minutes, padded to 2 digits, range: 00 - 59
// SS = seconds, padded to 2 digits, range: 00 - 59
// The maximum time never exceeds 359999 (99:59:59)

// You can find some examples in the test fixtures.


function humanReadable(seconds) {
    // let hours = toString(Math.floor(seconds/3600));
    let hours = Math.floor(seconds/3600).toString();
    // console.log(typeof hours, hours)
    if (hours.length === 1) {
        hours = "0" + hours;
    }
    let afterhours = seconds % 3600;
    let minutes = Math.floor(afterhours/60).toString();
    // console.log(typeof minutes, minutes)
    if (minutes.length === 1) {
        minutes = "0" + minutes;
    }
    let myseconds = (afterhours % 60).toString();
    if (myseconds.length === 1) {
        myseconds = "0" + myseconds;
    }
    // console.log(typeof myseconds, myseconds)
    let result = hours + ":" + minutes + ":" + myseconds;
    return result;
}


let num1 = 22305;
let num2 = 499;
let num3 = 288883

console.log(humanReadable(0));
console.log(humanReadable(5));
console.log(humanReadable(60));
console.log(humanReadable(86399));
console.log(humanReadable(359999));
