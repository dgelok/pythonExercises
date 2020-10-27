// Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

// Examples:
// Input: 42145 Output: 54421

// Input: 145263 Output: 654321

// Input: 123456789 Output: 987654321

function descendingOrder(n){
    //...
    let numString = n.toString()
    let myNums = []
    for (let i = 0; i<numString.length; i++) {
        myNums.push(numString[i])
    }
    myNums.sort()
    let answer = ""
    for (let j = myNums.length - 1; j >= 0; j = j-1) {
        answer = answer + myNums[j]
    }
    return Number(answer)


}

console.log(descendingOrder(54321))