//Link -> https://www.codewars.com/kata/523f5d21c841566fde000009

function arrayDiff(a, b) {
    var distinctArray = []

    a.forEach(element => {
        if(b.includes(element) == false){
            distinctArray.push(element)
        }
    });

    return distinctArray
}
