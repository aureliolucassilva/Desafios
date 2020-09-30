//Link -> https://www.codewars.com/kata/52dbae61ca039685460001ae

function change(string){
    const alphabet = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 'x', 'y', 'z'];

    const stringLeters = Array.from(string.toLowerCase());
    var zeroOne = "00000000000000000000000000";
    
    for(const letter of alphabet){
        if(stringLeters.includes(letter)){
            zeroOne = zeroOne.split('');
            zeroOne[alphabet.indexOf(letter)] = '1';
            zeroOne = zeroOne.join('');
        }
    }

    return zeroOne;
}
