//Link -> https://www.codewars.com/kata/526571aae218b8ee490006f4

using System;
using System.Linq;

public class Kata
{
  public static int CountBits(int n)
  {
       var zero_one = Convert.ToString(Math.Abs(n), 2);
       int result = 0;

       result = zero_one.Count(i => i == '1');

       return result;
  }
}
