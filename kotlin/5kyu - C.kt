//Link -> https://www.codewars.com/kata/513e08acc600c94f01000001

import kotlin.math.abs

fun rgb(r: Int, g: Int, b: Int): String {
    val hexadecimal = mapOf<Int, String>(0 to "0", 1 to "1", 2 to "2", 3 to "3", 4 to "4", 5 to "5", 6 to "6", 7 to "7",
    8 to "8", 9 to "9", 10 to "A", 11 to "B", 12 to "C", 13 to "D", 14 to "E", 15 to "F")

    var rgbToHex:String? = ""
    val red = if(r in 0..255) r else if(r > 255) 255 else 0
    val green = if(g in 0..255) g else if(g > 255) 255 else 0
    val blue = if(b in 0..255) b else if(b > 255) 255 else 0

    //Red
    val redFirst = red / 16
    val redSecond = ((red.toDouble() / 16) - redFirst) * 16
    rgbToHex = "${hexadecimal[redFirst]}${hexadecimal[redSecond.toInt()]}"

    //Green
    val greenFirst = green / 16
    val greenSecond = ((green.toDouble() / 16) - greenFirst) * 16
    rgbToHex += "${hexadecimal[greenFirst]}${hexadecimal[greenSecond.toInt()]}"

    //Blue
    val blueFirst = blue / 16
    val blueSecond = ((blue.toDouble() / 16) - blueFirst) * 16
    rgbToHex += "${hexadecimal[blueFirst]}${hexadecimal[blueSecond.toInt()]}"

    return rgbToHex
}
