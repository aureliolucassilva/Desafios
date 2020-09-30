//Link -> https://www.codewars.com/kata/54d7660d2daf68c619000d95

using System;
using System.Linq;

public class Fracts {
  public static string convertFrac(long[,] lst) {
  
         long[] denominators = new long[] { };
         string result = string.Empty;

         for (int i = 0; i <= lst.Length/2 - 1; i++)
         { 
            denominators = denominators.Append(lst[i, 1]).ToArray();
         }

         long divisor = 2;
         bool repetition = false;
         long[] MMC = new long[] { };
            

         //MMC
         do
         {
            while (denominators.All(x => x % divisor != 0) == false)
            {
               for (int i = 0; i <= denominators.Length - 1; i++)
               {
                  if (denominators[i] % divisor == 0)
                  {
                       if(repetition == false) MMC = MMC.Append(divisor).ToArray();
                       denominators[i] = denominators[i] / divisor;
                       repetition = true;
                  }
               }
               repetition = false;
             }

             divisor += 1;

           } while (denominators.All(x => x == 1) == false);

           long MMC_result = 1;

           foreach(long number in MMC)
           {
              MMC_result *= number;
           }

           //Result
           for (int i = 0; i <= lst.Length/2 - 1; i++)
           {
              result += $"({lst[i, 0] * MMC_result / lst[i, 1]},{MMC_result})";
           }

           return result;
  }
}
