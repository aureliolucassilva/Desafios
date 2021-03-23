// Link -> https://www.codewars.com/kata/563b662a59afc2b5120000c6

import scala.math._

object Hello extends App{

  def nbYear(p0: Int, percent: Double, aug: Int, p: Int): Int = {
    var years: Int = 0
    var newPopulation: Double = p0

    while (newPopulation < p) {
      newPopulation = floor(newPopulation + newPopulation * (percent / 100) + aug)
      years = years + 1
    }
    return years
  }

  println(nbYear(1000,2.0,50,1214))
}
