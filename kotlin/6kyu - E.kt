//Link -> https://www.codewars.com/kata/5839edaa6754d6fec10000a2

fun findMissingLetter(array: CharArray): Char {
    val firstLetter = array[0]
    val lastLetter = array.last()
    var missingLetter = ' '

    for(letter in firstLetter until lastLetter){
        if(!array.contains(letter)){
            missingLetter = letter
            break
        }
    }

    return missingLetter
}
