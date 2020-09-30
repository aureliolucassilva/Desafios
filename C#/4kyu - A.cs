// Link -> https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

using System;
using System.Collections.Generic;
using System.Linq;
public class Parser
{
    public static int ParseInt(string s)
    {
         int result = 0;
         int[] subResult = new int[] { };

         Dictionary<string, int> translation = new Dictionary<string, int>()
         {
             {"zero", 0},
             {"one", 1},
             {"two", 2},
             {"three", 3},
             {"four", 4},
             {"five", 5},
             {"six", 6},
             {"seven", 7},
             {"eight", 8},
             {"nine", 9},
             {"ten", 10},
             {"eleven", 11},
             {"twelve", 12},
             {"thirteen", 13},
             {"fourteen", 14},
             {"fifteen", 15},
             {"sixteen", 16},
             {"seventeen", 17},
             {"eighteen", 18},
             {"nineteen", 19},
             {"twenty", 20},
             {"thirty", 30},
             {"forty", 40},
             {"fifty", 50},
             {"sixty", 60},
             {"seventy", 70},
             {"eighty", 80},
             {"ninety", 90},
         };

         string[] wordNumber = s.Split(new string[] { " ", "-" }, StringSplitOptions.None);

         foreach (string word in wordNumber)
         {
             switch(word)
             {
               case "and":
                    continue;
               case "hundred":
                    result *= 100;
                    break;
               case "thousand":
                    result *= 1000;
                    subResult = subResult.Append(result).ToArray();
                    result = 0;
                    break;
               case "million":
                    result *= 1000000;
                    subResult = subResult.Append(result).ToArray();
                    result = 0;
                    break;
               default:
                    result += translation[word];
                    break;
             }
          }

          if(subResult.Length > 0)
          {
             result += subResult.Sum();
          }

          return result;
    }
}
