//Link -> https://www.codewars.com/kata/59f44c7bd4b36946fd000052

fun hist(s: String): String{
    var errors = mutableMapOf<Char, Int>('u' to 0, 'w' to 0, 'x' to 0, 'z' to 0)

    errors['u'] = s.count{it == 'u'}
    errors['w'] = s.count{it == 'w'}
    errors['x'] = s.count{it == 'x'}
    errors['z'] = s.count{it == 'z'}

    var asterisk = ""
    var blankSpace = ""
    var result = ""

    for ((error, number) in errors){
        repeat(number)
        {
            asterisk += "*"
        }

        repeat(6 - number.toString().length){
            blankSpace += " "
        }

        if(number != 0) {
            result += ("$error  $number$blankSpace$asterisk\r")
        }

        blankSpace = ""
        asterisk = ""
    }

    result = result.trimEnd()

    return result
}
