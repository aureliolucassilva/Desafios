// Link -> https://www.codewars.com/kata/54dc6f5a224c26032800005c

object Hello extends App{

  def stockSummary(lstOfArt: Array[String], lstOfCat: Array[String]): String = {
    var stock: Map[String, Int] = Map[String, Int]()
    var stockReport = ""

    if (lstOfArt.length == 0) return ""

    for (book <- lstOfArt) {
      val category: String = book.take(1)
      val quantity: Int = book.split(" ")(1).toInt

      if (stock.contains(category)) {
        val newValue = stock(category) + quantity
        stock = stock + (category -> newValue)
      }
      else {
        stock += (category -> quantity)
      }
    }

    for(category <- lstOfCat){
      if (!stock.contains(category)){
        stockReport = stockReport + " - " + "(" + category + " : 0" + ")"
      }
      else {
        stockReport = stockReport + " - " + "(" + category + " : " + stock(category) + ")"
      }
    }

    stockReport = stockReport.drop(2)

    return stockReport
  }
}
