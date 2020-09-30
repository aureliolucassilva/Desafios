//Link -> https://www.codewars.com/kata/55466989aeecab5aac00003e

using System;
using System.Linq;
using System.Collections.Generic;


public class SqInRect {
  
  public static List<int> sqInRect(int lng, int wdth) {

    List<int> result = new List<int> { };
    if(lng == wdth)
    {
        return null;
    }
    else
    {
        do
        {
            int min = Math.Min(lng, wdth);
            int max = Math.Max(lng, wdth);

            if(lng == max)
            {
               lng = lng - min;
            }
            else
            {
                wdth = wdth - min;
            }     

            result.Add(min);

            } while (Math.Abs(lng - wdth) > 0);

            result.Add(Math.Min(lng, wdth));

            return result;
    }
  }
}
