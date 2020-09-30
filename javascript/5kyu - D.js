//Link -> https://www.codewars.com/kata/520b9d2ad5c005041100000f

function pigIt(str){
    const words = str.split(" ")
    var newString = ""

    for(i = 0; i < words.length; i++){
        if(words[i] != '!' && words[i] != '?' && words[i] != '.'){
            newString += words[i].substring(1, words[i].length) + words[i][0] + "ay" + " ";
        } else {
            newString += words[i];
        }
        
    }

    return newString.trim();
}
