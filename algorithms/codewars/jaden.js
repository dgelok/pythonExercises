let toJadenCase = function (str) {
    //in a String.prototype.toJadenCase(), you need this.split()
    let myArr = str.split(" ")
    let newArr = []
    let alpha = "abcdefghijklmnopqrstuvwxyz";
    let ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (let i = 0; i<myArr.length; i++) {
        let myLetter = myArr[i][0]
        if (ALPHA.includes(myLetter)) {
            newArr.push(myArr[i])
        }
        else {
            let index = alpha.indexOf(myLetter);
            let myWord = myArr[i]
            newArr.push(ALPHA[index] + myWord.slice(1,));
        }
    }
    let answer = newArr.join(' ')
    return answer

};

console.log(toJadenCase('How did we get here'))