//Link -> https://www.codewars.com/kata/52de553ebb55d1fca3000371

using System;
using System.Linq;
using System.Collections.Generic;

public class Kata
{
  public static int FindMissing(List<int> list)
  {
       int step = (list.Last() - list.First()) / list.Count;
       List<int> real_sequence = new List<int> { };

       for(int i = list.First(); i <= list.Last(); i += step)
       {
          real_sequence.Add(i);
       }

       int missing = 0;

       foreach(int number in real_sequence)
       {
           if(list.Contains(number) == false)
           {
              missing = number;
           }
       }

       return missing;
  }
}
