// Given the triangle of consecutive odd numbers:

// 1                                
// 3     5                          
// 7     9    11                    
// 13    15    17    19             
// 21    23    25    27    29       
// ...

// Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

// rowSumOddNumbers(1); // 1
// rowSumOddNumbers(2); // 3 + 5 = 8

function rowSumOddNumbers(n) {
    // TODO
    const arr = [];
    let valueCounter = 0;
    let prevRowLastVal = 0;
    let currentValue = 1
    for (let i = 0; i < n; i++) {
        arr.push([]);
        valueCounter++;
        for (let j = 0; j < valueCounter; j++) {
            arr[i].push(currentValue)
            currentValue += 2;
        }
    }

    let answer = 0;
    for (let z of arr[n-1]) {
        answer += z
    }
    console.log(answer)
}

rowSumOddNumbers(5)
// n(1) = 1
// n(2) = 3 (2)
// n(3) = 7 (4)
// n(4) = 13 (6)
// n(5) = 21 (8)
