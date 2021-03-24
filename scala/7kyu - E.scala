// Link -> https://www.codewars.com/kata/58941fec8afa3618c9000184

import scala.util.control._

object Hello extends App{

  def growingPlant(upSpeed: Int, downSpeed: Int, desiredHeight: Int): Int = {
    val loop = new Breaks;
    var height = 0
    var days = 0

    loop.breakable{
      while (height < desiredHeight){
        days = days + 1
        height = height + upSpeed

        if(height >= desiredHeight){
          loop.break
        }

        height = height - downSpeed
      }
    }

    return days
  }

}
