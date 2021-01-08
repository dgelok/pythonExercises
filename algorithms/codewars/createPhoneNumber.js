// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.


function createPhoneNumber(numbers){
    let result = "(";
    for (let i = 0; i < 3; i++) {
        // console.log(numbers[i]);
        result = result + numbers[i]
  }
    result = result + ") ";

    for (let j = 3; j < 6; j++) {
        result = result + numbers[j];
    }
    result = result + "-";
    

    for (let k = 6; k <10; k++) {
        result = result + numbers[k];
    }
    return result
}


let arr1 = [0,1,2,3,4,5,6,7,8,9];
let arr2 = [9,9,9,9,9,9,9,9,9,9];

console.log(createPhoneNumber(arr1));
console.log(createPhoneNumber(arr2));