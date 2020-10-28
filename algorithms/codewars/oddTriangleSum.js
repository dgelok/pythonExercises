// Given the triangle of consecutive odd numbers:

// 1                                1:1
// 3     5                          2:3
// 7     9    11                    3:6
// 13    15    17    19             4:10
// 21    23    25    27    29       5:15
// ...

// Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

// rowSumOddNumbers(1); // 1
// rowSumOddNumbers(2); // 3 + 5 = 8

function rowSumOddNumbers(n) {
    // TODO
    let starter = (x) =>{
        return x*2 - 2 
    }
    console.log(starter(1))
    console.log(starter(2))
    console.log(starter(3))
    console.log(starter(4))
    console.log(starter(5))
}

// n(1) = 1
// n(2) = 3 (2)
// n(3) = 7 (4)
// n(4) = 13 (6)
// n(5) = 21 (8)

rowSumOddNumbers(4)