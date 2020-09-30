//Link -> https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

using System;
using System.Linq;

public class Accumul 
{
  public static String Accum(string s) 
  {
      char[] s_stripped = s.ToCharArray();
      string[] word = new string[s_stripped.Length];

      for(int i = 0; i <= s_stripped.Length -1; i++)
      {
         word.Append(s_stripped[i].ToString());

         for(int x = 0; x <= i; x++)
         {
            word[i] += s_stripped[i].ToString().ToLower();
         }

         char[] new_word = word[i].ToCharArray();
         new_word[0] = Char.ToUpper(new_word[0]);
         word[i] = new string(new_word);
       }

       string result = string.Join("-", word);

       return result; 
  }
}
