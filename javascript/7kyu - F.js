//Link -> https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d

function halvingSum(n) {
   var half = n;
   var sum = n;

   while(half > 1){
       half /= 2;
       sum += parseInt(half, 10);
   }

   return sum; 
}
