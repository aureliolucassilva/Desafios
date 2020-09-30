//Link -> https://www.codewars.com/kata/5202ef17a402dd033c000009

using System;
using System.Linq;

public class Kata
{
  public static string TitleCase(string title, string minorWords="")
  {    
      if(title != string.Empty)
      {
         string[] words = title.Split();

         if(string.IsNullOrEmpty(minorWords))
         {
             minorWords = "";
         }

         string[] exceptions = minorWords.ToLower().Split();
         string result = string.Empty;
         result += Char.ToUpper(words[0][0]) + words[0].Substring(1).ToLower() + " ";

         foreach (string word in words.Skip(1).ToArray())
         {
            if (exceptions.Contains(word.ToLower()) == false)
            {
               result += Char.ToUpper(word[0]) + word.Substring(1).ToLower() + " ";
            }
            else
            {
               result += word.ToLower() + " ";
            }

          }

          return result.Substring(0, result.Length - 1);
          }
      else
      {
        return title;
      }
  }
}
