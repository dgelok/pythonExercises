// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

function isIsogram(str){
    //...
    let myDict = {}
    let letter = ""
    for (let i = 0; i<str.length; i++) {
        letter = str[i].toLowerCase()
        if (myDict[letter]) {
            return false
        }
        myDict[letter] = "present"
    }
    return true
  }