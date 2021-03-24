// Link -> https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

object Hello extends App{

  def evaporator(content: Double, evapPerDay: Int, threshold: Int): Int = {
    val minimumContent: Double = content * (threshold.toDouble / 100)
    var newContent: Double = content
    var days = 0

    while(newContent >= minimumContent){
       newContent = newContent - (newContent * (evapPerDay.toDouble / 100))
       days = days + 1
    }

    return days
  }
}
