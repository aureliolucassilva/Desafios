//Link -> https://www.codewars.com/kata/51c8e37cee245da6b40000bd

function solution(input, markers) {
    var lines = input.split("\n")
    var containsMark = false
    var newString = ""

    for(a = 0; a < lines.length; a++){
        for(b = 0; b < markers.length; b++){
            if(lines[a].includes(markers[b])){
                var index = lines[a].indexOf(markers[b])
                newString += lines[a].substring(0, index).trim() 
                newString += "\n"
                containsMark = true
                break
            }
        }

        if(!containsMark){
            newString += lines[a]
            newString += "\n"
        }     

        containsMark = false
    }

    return newString.trim()
};
