//Link -> https://www.codewars.com/kata/5848565e273af816fb000449

var encryptThis = function(text) {
    const words = text.split(" ");
    var textEncryption = "";

    for(const word of words){
        var wordSize = word.length;

        switch(wordSize){
            case 1:
                textEncryption += word[0].charCodeAt(0);
                textEncryption += " ";
                break;
            case 2:
                textEncryption += word[0].charCodeAt(0);
                textEncryption += word[1];
                textEncryption += " ";
                break;
            case 3:
                textEncryption += word[0].charCodeAt(0);
                textEncryption += word[2];
                textEncryption += word[1];
                textEncryption += " ";
                break;
            default:
                textEncryption += word[0].charCodeAt(0);
                textEncryption += word[word.length - 1];
                textEncryption += word.substring(2, word.length - 1);
                textEncryption += word[1];
                textEncryption += " ";
        }
    }     

    return textEncryption.trim();
}
