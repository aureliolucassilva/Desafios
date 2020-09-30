//Link -> https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

using System;
using System.Linq;

public class SnailSolution
{
   public static int[] Snail(int[][] array)
   {
       int n = array.Length;
       int[] snail = array[0];

       //Number of Inner Lines
       int inner_snail = (n - 2) * 2 - 1;
            
       //Exceptions -> n <= 2 
       if(n == 2)
       {
          foreach (int[] line in array.Skip(1))
          {
             snail = snail.Append(line[n - 1]).ToArray();
          }

          for (int idx = n - 2; idx >= 0; idx--)
          {
             snail = snail.Append(array.Last()[idx]).ToArray();
          }

          return snail;
       }
       else if(n <= 1)
       {
          return array[0];
       }
           
       //Outer Snail
       foreach(int[] line in array.Skip(1))
       {
          snail = snail.Append(line[n - 1]).ToArray();
       }

       for(int idx = n - 2; idx >= 0; idx --)
       {
          snail = snail.Append(array.Last()[idx]).ToArray();
       }

       for (int idx = n - 2; idx >= 1; idx--)
       {
          snail = snail.Append(array[idx][0]).ToArray();
       }

       //Middle
       double index_middle = Math.Ceiling((Convert.ToDouble(n) - 1) / 2);

       //Control variables

       int line_ul = 1; //Upper_lines
       //***//
       int column_foward_ll = -1; //Lower_lines
       int line_ll = n - 2;
       //***//
       int column_rc = n - 2; //Right_columns
       int line_foward_rc = -1;
       //***//
       int line_foward_lc = -1; //Left_columns
       int column_lc = 1;

       //Inner Snail
       Upper_lines:
       if (inner_snail >= 1)
       {
           if(line_ul <= index_middle)
           {
               for (int column = line_ul; column <= n - 1 - line_ul; column++)
               {
                   snail = snail.Append(array[line_ul][column]).ToArray();
               }

               line_ul += 1;
               goto Right_columns;
           }
       }

       Right_columns:
       if (inner_snail >= 3)
       {
          if (column_rc >= index_middle)
          {
             line_foward_rc += 1;

             for (int line = 2 + line_foward_rc; line <= column_rc; line++)
             {
                snail = snail.Append(array[line][column_rc]).ToArray();
             }

             column_rc -= 1;
             goto Lower_lines;
          }
       }

       Lower_lines:
       if (inner_snail >= 3)
       {
          if(line_ll >= index_middle)
          {
             column_foward_ll += 1;

             for (int column = line_ll - 1; column >= 1 + column_foward_ll; column--)
             {
                snail = snail.Append(array[line_ll][column]).ToArray();
             }

             line_ll -= 1;
             goto Left_columns;
          }
       }
            
       Left_columns:
       if (inner_snail > 3)
       {
          if(column_lc <= index_middle)
          {
             line_foward_lc += 1;

             for (int line = n - 3 - line_foward_lc; line >= 2 + line_foward_lc; line--)
             {
                snail = snail.Append(array[line][column_lc]).ToArray();
             }

             column_lc += 1;
             goto Upper_lines;
          }
       }

       return snail;
   }
}
