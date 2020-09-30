//Link -> https://www.codewars.com/kata/55d24f55d7dd296eb9000030

using System;

public static class Kata 
{
    public static int summation(int num)
    {
      int soma = 0;

      for(int i = 0; i <= num; i++)
      {
          soma += i;
      }

      return soma;
    }
}
