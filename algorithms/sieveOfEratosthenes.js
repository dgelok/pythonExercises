// for a number n, return all the prime numbers up to n. 

const sieve = (n) =>{
    let myNums = []
    for (let i = 1; i <= n+1; i++) {
        myNums.push(true)
    }
    console.log(myNums.length)
    
    // we now have myNums - an array of length n - where all the entries are true

    // now we go through and remove all multiples
    let p = 2;
    while (p*p < n) {
        if (myNums[p]) {
            for (let y = (p*2); y < n; y += p) {
                myNums[y] = false
            }
        }
        p++
    }

    
    // at this point, myNums has true for primes, and false for all of the multiples of those primes
    // if myNums[whatever] is true, print out its index
    for (let l = 0; l < n; l++) {
        if (myNums[l] === true) {
            console.log(l)
        }
    }

    

}


sieve(100)