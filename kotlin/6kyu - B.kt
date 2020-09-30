//Link -> https://www.codewars.com/kata/587309155cfd6b9fb60000a0

package com.codewars.geoffp

object UnwantedDollars {
  fun moneyValue(money:String):Double {
    var moneyString = money.replace(" ","").replace("$", "")
    var monetaryValue = 0.0

    if(!moneyString.contains('.')){
        moneyString = "$moneyString.0"
    }

    if(moneyString.indexOf('.') == moneyString.length - 2){
        moneyString += "0"
    }

    monetaryValue = moneyString.toDouble()

    return monetaryValue
  }
}
