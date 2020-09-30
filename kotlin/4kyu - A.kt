// Link -> https://www.codewars.com/kata/51e056fe544cf36c410000fb

fun top3(s: String): List<String> {
    val re = Regex("[^A-Za-z0-9' ]")
    val words = re.replace(s.toLowerCase(), " ").split(" ")
    val frequency = emptyList<Pair<String,Int>>().toMutableList()

    for(item in words.distinct()){
        if(item != "" && item.replace("'","").isNotEmpty()) frequency.add(Pair(item, words.filter { it == item }.count()))
    }

    val mostFrequent = emptyList<String>().toMutableList()

    for(i in 0..2){
        val wordPair = frequency.maxBy { it.second }
        if (wordPair != null) {
            mostFrequent.add(wordPair.first)
        }
        frequency.remove(wordPair)
    }
    
    println(s)
    return mostFrequent
}
