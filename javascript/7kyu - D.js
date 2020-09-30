//Link -> https://www.codewars.com/kata/53670c5867e9f2222f000225

function isOrthogonal(u,v) {
    const vectorDots = u.length - 1;
    var dotProduct = 0;

    for(i = 0; i <= vectorDots; i++){
        dotProduct += u[i] * v[i];
    }

    if(dotProduct == 0){
        return true;
    } else {
        return false;
    }
}
