//Link -> https://www.codewars.com/kata/589273272fab865136000108

package pianoKataPartOne

fun blackOrWhiteKey(keyPressCount : Int) : String {
    val blackKeys = arrayListOf<Int>(2)
    val steps = arrayOf(3,2,3,2,2)

    while (blackKeys.last() != 86){
        for (step in steps){
            blackKeys.add(blackKeys.last() + step)
        }
    }

    var equivalentKey = 0

    equivalentKey = if(keyPressCount > 88) {
        keyPressCount - (keyPressCount/88) * 88
    } else{
        keyPressCount
    }

    return if(blackKeys.contains(equivalentKey))
        "black"
    else
        "white"
}
