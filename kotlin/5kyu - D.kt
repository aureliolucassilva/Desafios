//Link -> https://www.codewars.com/kata/55c6126177c9441a570000cc

package weight

fun orderWeight(string:String):String {
    val wrongWeights = string.split(" ")
    val realWeights = emptyList<Pair<Int,String>>().toMutableList()
    var realWeight = 0

    for(weight in wrongWeights){
        if(weight != " "){
            if(weight.toLongOrNull() != null){
                for(singleNumber in weight.toCharArray()){
                    realWeight += singleNumber.toString().toInt()
                }
                realWeights += Pair(realWeight, weight)
                realWeight = 0
            }
        }
    }

    realWeights.sortBy { it.first }
    var newOrder = ""
    var subList = emptyList<Pair<Int,String>>().toMutableList()

    for(realWeight in realWeights){
        if(subList.contains(realWeight)) continue
        subList = realWeights.filter { it.first == realWeight.first }.toMutableList()

        if(subList.size == 1){
            newOrder += realWeight.second + " "
        } else{
            subList.sortBy { it.second }
            for(subWeights in subList){
                newOrder += subWeights.second + " "
            }
        }

    }

    return newOrder.trimEnd()
}
