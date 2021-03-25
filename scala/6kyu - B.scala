// Link -> https://www.codewars.com/kata/51e0007c1f9378fa810002a9

object Hello extends App{

  def parse(data: String): List[Int] = {
    var value: Int = 0
    var result: List[Int] = List[Int]()

    for(x <- data){
      if (x == 'i'){
        value = value + 1
      }
      else if(x == 'd'){
        value = value - 1
      }
      else if(x == 's'){
        value = value * value
      }
      else if(x == 'o'){
        result = result :+ value
      }
    }

    return result
  }
}
