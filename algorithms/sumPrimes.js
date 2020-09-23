// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

// Find the sum of all the primes below two million.

let sieve = (n) =>{
    
    let myNums = new Array(n+1)
    for (let i=0; i<myNums.length; i++) {
        myNums[i] = true
    }

    console.log(myNums)

    for (let j=2; j*j<=n; j++) {
        if (myNums[j] == true) {
            for (let k = j*2; n+1; k=k*2) {
                myNums[k] = false
            }
        }
    }

    console.log(myNums)

    // let answer = 0
    // for (let l=2; l<=myNums.length; l++) {
    //     if (myNums[l] == true){
    //         answer += l
    //     }
    // }

    // return answer

}

console.log(sieve(200))