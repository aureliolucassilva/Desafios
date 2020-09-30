//Link -> https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

import kotlin.math.abs

fun rangeExtraction(arr: IntArray): String {
    var list = ""
    var previous = arr[0]
    var next = arr[1]
    var case = 0
    var range =  emptyList<Int>().toMutableList()

    for(n in arr){
        val diffP = abs(n - previous)
        val diffN = abs(n - next)

        if(diffP != 1 && diffN != 1) case = 0
        if(diffP == 1 && diffN != 1) case = 1
        if(diffN == 1 && diffP != 1) case = 2
        if(diffP == 1 && diffN == 1) case = 3


        if(case == 0){
            if(range.size >= 3){
                list += "${range[0]}-${range.last()},"
                range = mutableListOf()
            }
            else if(range.size == 2){
                list += "${range[0]},${range[1]},"
                range = mutableListOf()
            }

            list += "$n,"
            previous = n
            next = if(arr.indexOf(n) + 1 < arr.size - 2) arr[arr.indexOf(n) + 2]
            else arr.last()

        } else if(case == 1){
            range.add(n)
            previous = n
            next = if (arr.indexOf(n) + 1 < arr.size - 2) arr[arr.indexOf(n) + 2]
            else arr.last()

            if(range.size >= 3){
                list += "${range[0]}-${range.last()},"
                range = mutableListOf()
            }
            else if(range.size == 2){
                list += "${range[0]},${range[1]},"
                range = mutableListOf()
            }

        } else if(case == 2){
            range.add(n)
            previous = n
            next = if (arr.indexOf(n) + 1 < arr.size - 2) arr[arr.indexOf(n) + 2]
            else arr.last()
            
        } else if(case == 3){
            range.add(n)
            previous = n
            next = if (arr.indexOf(n) + 1 < arr.size - 2) arr[arr.indexOf(n) + 2]
            else arr.last()
        }
    }

    return list.substring(0, list.length - 1)
}
