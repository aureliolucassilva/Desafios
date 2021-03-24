// Link -> https://www.codewars.com/kata/558fc85d8fd1938afb000014

object Hello extends App{

  def sumTwoSmallest(numbers: List[Int]): Int = {
    val orderNumbers = numbers.sorted

    return orderNumbers(0) + orderNumbers(1)
  }

}
