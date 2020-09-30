//Link -> https://www.codewars.com/kata/5877e7d568909e5ff90017e6

using System;
using System.Linq;
using System.Collections.Generic;
class HowManyNumbers
{
   public static List<long> FindAll(int sumDigits, int numDigits)
   {
       string min_number = "11";
       string max_number = "99";

       for(int i = 1; i <= numDigits - 2; i++)
       {
           min_number += '1';
           max_number += '9';
       }

       List<long> valid_numbers = new List<long> { };

       for(long number = Convert.ToInt64(min_number); number <= Convert.ToInt64(max_number); number++)
       {
           char[] digits = number.ToString().ToCharArray();
           char previous = digits[0];

           for (int i = 1; i <= digits.Length - 1; i++)
           {
               if (digits[i] - previous < 0)
               {
                   for (int k = i; k <= digits.Length - 1; k++)
                   {
                        digits[k] = previous;
                   }

                   number = Convert.ToInt64(new string(digits));
                   break;
               }
               else
               {
                   previous = digits[i];
               }
           }

           int sum = number.ToString().Sum(c => c - '0');

           if (sum == sumDigits)
           {
              valid_numbers = valid_numbers.Append(number).ToList();
           }
       }

       List<long> numbers_found = new List<long> { };

       if (valid_numbers.Count() >= 1)
       {
           numbers_found = new List<long> { valid_numbers.Count(), valid_numbers[0], valid_numbers.Last() };
       }

       return numbers_found;
   }
}
