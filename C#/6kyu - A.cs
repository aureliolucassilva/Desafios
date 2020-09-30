//Link -> https://www.codewars.com/kata/587731fda577b3d1b0001196

using System;

namespace Kata
{
  public static class Problem
  {
    public static string CamelCase(this string str)  
    {  
        string[] words = (str ?? "").Split();
        string result = string.Empty;

        foreach (string word in words)
        {
            if(word.Length > 1)
            {
               result += Char.ToUpper(word[0]) + word.Substring(1);
            }
            else if(word == "")
            {
               result += "";
            }
            else
            {
               result += Char.ToUpper(word[0]);
            }
        }
            
        return result;
    }
  }
}
