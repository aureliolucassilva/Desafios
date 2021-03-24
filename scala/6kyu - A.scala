// Link -> https://www.codewars.com/kata/51b6249c4612257ac0000005

import scala.util.control._

object Hello extends App{

  def decode(roman: String): Int = {
    val loop = new Breaks;
    val letters: Map[Char, Int] = Map('I'->1, 'V'->5, 'X'->10, 'L'->50, 'C'->100, 'D'->500, 'M'->1000)
    val hierarchy: Array[Char] = Array('M', 'D', 'C', 'L', 'X', 'V', 'I')

    val listRomans = roman.toList
    var i = 0
    var number = 0

    loop.breakable {
      while (i < listRomans.length) {
        if (i == listRomans.length - 1) {
          number = number + letters(listRomans(i))
          loop.break
        }

        if (hierarchy.indexOf(listRomans(i + 1)) < hierarchy.indexOf(listRomans(i))) {
          number = number + letters(listRomans(i)) - letters(listRomans(i + 1))
          i = i + 1
        }
        else {
          number = number + letters(listRomans(i))
        }

        i = i + 1
      }
    }

    return number
  }
  
}
