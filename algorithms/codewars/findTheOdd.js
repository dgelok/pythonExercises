// Given an array of integers, find the one that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
    let myDict = {}
    for (let i of A) {
        if (myDict[i]) {
            myDict[i] += 1;
        }
        else {
            myDict[i] = 1
        }
    }

    for (let j of Object.keys(myDict)) {
        if (myDict[j] % 2 != 0) {
            return Number(j)
        }
    }
  }