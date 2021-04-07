object Hello extends App{

  def solution(s: String): List[String] = {
    var idx: Int = 0
    var splitString: List[String] = List[String]()

    if(s.length == 0 ){
      return splitString
    }

    while (idx < s.length){
      splitString = s.slice(idx,idx + 2) :: splitString
      idx = idx + 2
    }

    if(splitString.head.length == 1){
      splitString = splitString.updated(0, splitString.head + '_'.toString)
    }

    splitString.reverse
  }

}
