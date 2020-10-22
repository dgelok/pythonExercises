

function add(num1, num2) {

    // turn the nums into strings
    let st1 = num1.toString()
    let st2 = num2.toString()

    let ar1 = st1.split('')
    let ar2 = st2.split('')

    while (ar1.length < ar2.length) {
        ar1.unshift("0")
    }
    while (ar2.length < ar1.length) {
        ar2.unshift("0")
    }

    let totals = []

    
    for (let i = 0; i < ar1.length; i++) {
        let num1 = Number(ar1[i])
        let num2 = Number(ar2[i])
        totals.push(num1 + num2)
    }


    // console.log(ar1)
    // console.log(ar2)
    // console.log(totals)

    let answer = ""
    for (let j = 0; j < totals.length; j++) {
        answer += (totals[j].toString())
    }

    console.log(answer)
    // pull the digits out
    // add the digits together, push the answer to an array
    // concat the array
    // turn that into an int
    // return

    return Number(answer)

}

add(122, 81)