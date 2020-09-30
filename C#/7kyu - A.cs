//Link -> https://www.codewars.com/kata/54ba84be607a92aa900000f1

using System;
using System.Linq;

public class Kata
{
  public static bool IsIsogram(string str) 
  {
    char[] word = str.ToUpper().ToCharArray().Distinct().ToArray();

            string new_word = new string(word);

            if(new_word.Length == str.Length)
            {
                return true;
            }
            else
            {
                return false;
            }
  }
}
