// Digital root is the recursive sum of all the digits in a number.

// Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

function digital_root(n) {
    let numString = n.toString();
    let sum = 0
    for (let i = 0; i<numString.length; i++) {
        sum += Number(numString[i])
    }
    
    while (sum >= 10) {
        sum = digital_root(sum)
    }

    return sum

  }



digital_root(154)


// ALTERNATE VERSION
// const digital_root = (num) => {
//     let splitNum = num.toString().split(''); //Convert number into an array of strings. Each element is one digit of the number
//     let sum = 0;
//     splitNum.forEach(eachNumber => {
//       sum += Number(eachNumber); // need to convert each string back to a number
//     })
//     return sum.toString().split('').length > 1 ? digital_root(sum) : sum;
//   }