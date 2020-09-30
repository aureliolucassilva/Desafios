//Link -> https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

function firstNonRepeatingLetter(s) {
    const letterArray = s.toLowerCase().split('')

    for(i = 0; i < letterArray.length; i++){
        if(letterArray.filter(x => x === letterArray[i]).length == 1){
            return s[i]
        }
    }
  
    return ""
}
