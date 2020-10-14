//====================================
// Problem 1 - Binary Search - (2)
//====================================
// write a function called binarySearch that takes a sorted array of whole numbers and a single whole number as arguments.
// Using the binary search method, see if the sorted array contains the whole number




const binarySearch = (arr, num) =>{
    let myMin = 0
    let myMax = arr.length - 1

    let midpoint = Math.floor(arr.length / 2)

    while (myMin <= myMax) {
        if (arr[midpoint] === num) {
            return true
        }

        if (arr[midpoint] < num) {
            myMin = midpoint + 1
        }
        else if (arr[midpoint] > num) {
            myMax = midpoint - 1
        }

        midpoint = Math.floor((myMax + myMin) / 2)
        // check if midpoint == num; if so, exit out
        // check if high/low; adjust min or max accordingly.
    }
    return false 
}



const searchArray = [1,2,3,4,5,6,7,8,9,10];


console.log(binarySearch(searchArray, 11))

    // while (True) {
    //     mycheck = arr[midpoint]
    //     if (mycheck == num) {
    //         return True
    //     }

    //     if (num > mycheck) {
    //         myMin = midpoint
    //     }
    //     else if (num < mycheck){
    //         myMax = midpoint
    //     }

    //     if (myMax == midpoint) {
    //         return False
    //     }



        // check if midpoint is higher, lower, or equal
        // if it's higher, myMax = midpoint
        // if it's lower, myMin = midpoint
        // if it's equal, break

    // }

const count = () => {
    let startingNum = 13;
    let workingNum = startingNum;
    let maxChain = 0;
    let maxChainNum = 0;
    let chainCounter = 0;
    while(startingNum < 1000000){
        if(workingNum % 2 === 0){
        workingNum = workingNum / 2;
        chainCounter++;
        } else {
        workingNum = 3*workingNum + 1;
        chainCounter++;
        }
        if(workingNum === 1) {
        if(chainCounter > maxChain){
            maxChain = chainCounter;
            maxChainNum = startingNum;
            startingNum++;
        } else {
            startingNum++;
            workingNum = startingNum;
        }
        chainCounter = 0;
        }
    }
    return (`Max chain number is ${maxChainNum} with a length of ${maxChain}`)
    }
    
    console.log(count());