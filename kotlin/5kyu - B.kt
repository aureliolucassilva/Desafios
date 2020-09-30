//Link -> https://www.codewars.com/kata/54e320dcebe1e583250008fd

package solution

object Dec2Fact {
    private val factorials = emptyMap<Int, Long>().toMutableMap()
    private val letters = mapOf<String, Int>(
            "A" to 10,
            "B" to 11,
            "C" to 12,
            "D" to 13,
            "E" to 14,
            "F" to 15,
            "G" to 16,
            "H" to 17,
            "I" to 18,
            "J" to 19,
            "K" to 20
    )

    fun dec2FactString(n: Long): String {
        var factString = ""
        var factorial = 1L

        //Factorials
        if(factorials.isEmpty()) {
            for(number in 1..20) {
                factorial *= number
                factorials[number] = factorial
            }
        }

        //Conversion
        val filter = factorials.filter { it.value <= n }
        var letter = 'A'
        var remainder = n

        for(v in filter.values.reversed()) {
            if(remainder / v < 10) {
                factString += "${remainder / v}"
                remainder = (n % v)
            } else {
                repeat(((remainder / v).toInt()) - 10) {
                    letter++
                }
                factString += letter
                remainder = (n % v)
                letter = 'A'
            }
        }

        //0!
        factString += "0"

        return factString
    }

    fun factString2Dec(str: String): Long {
        var dec = 0L
        var factorial = 1L

        //Factorials
        if(factorials.isEmpty()) {
            for(number in 1..20) {
                factorial *= number
                factorials[number] = factorial
            }
        }

        //Conversion
        var index = 0
        val filter = factorials.filterKeys { it <= str.length - 1 }

        for(v in filter.values.reversed()) {
            if(str[index].toString().toIntOrNull() != null){
                dec += v * str[index].toString().toLong()
                index++
            } else {
                dec += v * (letters[str[index].toString()]!!)
                index++
            }
        }

        return dec
    }
}
