import scala.util.matching.Regex

object Hello extends App {

  def change(s: String, prog: String, version: String): String = {
    var fields = s.split("\n")
    val months = List("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    var newFields = ""

    for (a <- fields) {
      a.split(" ")(0) match {
        case ("Program") => newFields = "Program: " + prog
        case ("Author:") => newFields = newFields + " " + "Author: " + "g964"
        case ("Phone:") => {
          var phoneNumber = a.split(" ")(1)
          val pattern = new Regex("\\+1-\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d")
          phoneNumber = (pattern findAllIn phoneNumber).mkString
          if (phoneNumber.length > 0) {
            newFields = newFields + " " + "Phone: " + "+1-503-555-0090"
          }
          else {
            return "ERROR: VERSION or PHONE"
          }
        }
        case ("Version:") => {
          val oldVersion = a.split(" ")(1)
          val pattern = new Regex("\\d+\\.\\d+")
          val newVersion = (pattern findAllIn version).mkString
          if (newVersion.length == oldVersion.length) {
            if (newVersion != "2.0") {
              newFields = newFields + " " + "Version: " + version
            }
            else {
              newFields = newFields + " " + "Version: 2.0"
            }
          }
          else {
            return "ERROR: VERSION or PHONE"
          }
        }
        case ("Corporation:") => newFields = newFields
        case ("Level:") => newFields = newFields
        case ("Date:") => newFields = newFields + " " + "Date: 2019-01-01"
        case default => newFields = newFields + " " + a
      }
    }
    newFields
  }
}
