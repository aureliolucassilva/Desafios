//Link -> https://www.codewars.com/kata/529b418d533b76924600085d

using System;
using System.Linq;

public static class Kata 
{
  public static string ToUnderscore(int str) 
  {
    return str.ToString();
  }

  public static string ToUnderscore(string str) 
  {
      string result = string.Empty;
      string copy = str;
      char[] letters = new char[] { };
      var upper = copy.Where(x => Char.IsUpper(x));
      int[] index = new int[] { };

      foreach(char letter in upper)
      {
         index = index.Append(copy.ToString().IndexOf(letter)).ToArray();
         letters = copy.ToCharArray();
         letters[copy.IndexOf(letter)] = '7';
         copy = new string(letters);
      }

      for(int idx = 0; idx <= index.Length - 1; idx++)
      {
          if (idx < index.Length - 1)
          {
              result += str.Substring(index[idx], index[idx + 1] - index[idx]).ToLower() + "_";
          }
          else if (idx == index.Length - 1)
          {
              result += str.Substring(index[idx]).ToLower();
          }
      }

      return result;
  }
}
