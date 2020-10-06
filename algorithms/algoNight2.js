

// let fib = (x) => {

//     if (x <= 2) {
//         return 1
//     }
//     else {
//         return (fib(x-1) + fib(x-2))
//     }
// }

// console.log(fib(5))

const fib = (num) => {

    if(num <= 2) { return 1 } //the first two numbers in the fib sequence are 1

    let fibCounter = 2; // start at 2 to account for the first two digits, 1 and 1, the first time we call fibSeq this will be incremented to 3 for the third digit
    let currentNum;

    const fibSeq = (prevNumber1,prevNumber2) => {
        fibCounter++;
        currentNum = prevNumber1 + prevNumber2;
        if(fibCounter === num) { return } // if we've found the nth number we were looking for return
        // shift everything to the right by one

        prevNumber1 = prevNumber2;
        prevNumber2 = currentNum;
        fibSeq(prevNumber1,prevNumber2);
    }
    fibSeq(1,1);
    return currentNum;
}