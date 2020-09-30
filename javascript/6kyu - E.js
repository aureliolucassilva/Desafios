//Link -> https://www.codewars.com/kata/54da5a58ea159efa38000836

function findOdd(A) {
  for(i = 0; i < A.length; i++){
       var appearences = A.filter(n => n == A[i]).length;
       if(appearences % 2 != 0){
           return A[i];
       }
  }
}
