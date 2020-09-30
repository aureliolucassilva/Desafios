//Link -> https://www.codewars.com/kata/559a28007caad2ac4e000083

using System;
using System.Linq;
using System.Numerics;

public class SumFct
{
  public static BigInteger perimeter(BigInteger n) 
  {
      BigInteger f1 = 0;
      BigInteger f2 = 1;
      BigInteger f3 = 1;
      BigInteger result = 0;

      if (n > 1)
      {
         result = (f1 + f2 + f3) * 4;
      }
      else if(n == 1)
      {
         result = (f1 + f2) * 4;
      }
      else if (n == 0)
      {
         result = f1 * 4;
      }

      for(int i = 0; i <= n - 2; i++)
      {
         f1 = f2;
         f2 = f3;
         f3 = f2 + f1;

         result += f3 * 4;
      }

      return result;
  }
}
