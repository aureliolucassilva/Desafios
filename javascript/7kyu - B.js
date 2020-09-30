//Link -> https://www.codewars.com/kata/53573877d5493b4d6e00050c

function capital(capitals){
    var statements = [];

    for(i = 0; i < capitals.length ; i++){
        if(capitals[i]["state"] !== undefined){
            statements.push("The capital of " + capitals[i]["state"] + " is " + capitals[i]["capital"]);
        } else if(capitals[i]["country"] !== undefined){
            statements.push("The capital of " + capitals[i]["country"] + " is " + capitals[i]["capital"]);
        }
    }

    return statements;
}
