// Link -> https://www.codewars.com/kata/51edd51599a189fe7f000015

import scala.collection.mutable.ListBuffer

object Hello extends App{

  def solution(a: Array[Int], b: Array[Int]): Double = {
    var differences = new ListBuffer[Double]()

    for(i <- 0 until a.length){
      val instance: Double = scala.math.pow(b(i) - a(i), 2)
      differences += instance
    }

    differences.sum/differences.length
  }

}
