// Link -> https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

object Hello extends App{

  def high(s: String): String = {
    val alphabet = "abcdefghijklmnopqrstuvwxyz"
    val words = s.split(" ")
    var highestSum = 0
    var highest = ""

    for (a <- words){
      var sum = 0
      for(b <- a){
        sum = sum + alphabet.indexOf(b) + 1
      }
      if (sum > highestSum) {
        highest = a
        highestSum = sum
      }
    }

    highest
  }
}
