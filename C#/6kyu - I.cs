//Link -> https://www.codewars.com/kata/545cedaa9943f7fe7b000048

using System;
using System.Linq;

public static class Kata
{
  public static bool IsPangram(string str)
  {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            char[] phrase = str.ToUpper().ToCharArray().Distinct().ToArray();

            string pangram = new string(phrase).Replace(" ", string.Empty);    
            
            if(pangram.Length >= alphabet.Length)
            {
                return true;
            }
            else
            {
                return false;
            }

            throw new NotImplementedException();
  }
}
