// Link -> https://www.codewars.com/kata/5467e4d82edf8bbf40000155

object Hello extends App{

  def descendingOrder(num: Int): Int = {
    var numString = num.toString

    var charList = numString.toList
    charList = charList.toList
    charList = charList.sorted
    charList = charList.reverse

    var endNumber = charList.mkString("")

    return endNumber.toInt
  }
}
