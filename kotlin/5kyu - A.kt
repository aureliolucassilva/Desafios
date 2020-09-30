//Link -> https://www.codewars.com/kata/5282b48bb70058e4c4000fa7

fun hexStringToRGB(hexString: String): RGB {
    val hexadecimal = mapOf<String, Int>(
            "0" to 0,
            "1" to 1,
            "2" to 2,
            "3" to 3,
            "4" to 4,
            "5" to 5,
            "6" to 6,
            "7" to 7,
            "8" to 8,
            "9" to 9,
            "A" to 10,
            "B" to 11,
            "C" to 12,
            "D" to 13,
            "E" to 14,
            "F" to 15)

    //Red
    val red = hexadecimal[hexString[1].toString().toUpperCase()]!! * 16 + hexadecimal[hexString[2].toString().toUpperCase()]!!
    //Green
    val green = hexadecimal[hexString[3].toString().toUpperCase()]!! * 16 + hexadecimal[hexString[4].toString().toUpperCase()]!!
    //Blue
    val blue = hexadecimal[hexString[5].toString().toUpperCase()]!! * 16 + hexadecimal[hexString[6].toString().toUpperCase()]!!

    return  RGB(red, green, blue)
}
