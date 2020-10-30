// Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

// Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

function isPrime(num) {
    //TODO
    if (num <= 1) {
        return false
    }
    let numArray = new Array(num+1).fill(true)
    
    let j = 2;
    while (j*j <= num) {
        if (numArray[j]) {
            for (let k = 2 * j; k <= num; k = k+j) {
                numArray[k] = false
            }
        }
        j++;
    }

    return numArray[num]

}

console.log(isPrime(104))