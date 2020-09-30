//Link -> https://www.codewars.com/kata/5168bb5dfe9a00b126000018

using System;

public static class Kata
{
  public static string Solution(string str) 
  {
      char[] word = str.ToCharArray();
      Array.Reverse(word);

      string reversed = new string(word);

      return reversed;
      
      throw new NotImplementedException("TODO: Kata.Solution(string) => string");
  }
}
