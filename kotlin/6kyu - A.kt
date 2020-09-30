// Link -> https://www.codewars.com/kata/5dad6e5264e25a001918a1fc

package decod

fun decode(s: String): String {
    val alphabet = "abcdefghijklmnopqrstuvwxyz"
    var num = ""
    var r = ""
    var failedDecode = -1

    for(ch in s) {
        if (ch.toString().toIntOrNull() == null) {
            for(n in 0..25) {
                if ((n * num.toInt()) % 26 == alphabet.indexOf(ch)) {
                    failedDecode ++
                    if(failedDecode == 0) r += alphabet[n]
                    else return "Impossible to decode"
                }
            }
            failedDecode = -1
        } else {
            num += ch
        }
    }

    return r
}
