//Link -> https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

using System;
using System.Linq;

public class Sudoku
{
  public static string DoneOrNot(int[][] board)
  {
     //Rows
     for (int row = 0; row <= 8; row++)
     { 
         if (board[row].Distinct().ToArray().Length < 9)
         {
            return "Try again!";
         }
     }

     int[] column = new int[] { };

     //Columns
     for (int column_element = 0; column_element <= 8; column_element++)
     {
         for (int row = 0; row <= 8; row++)
         {
             column = column.Append(board[row][column_element]).ToArray();
         }

         if (column.Distinct().ToArray().Length < 9)
         {
             return "Try again!";
         }

         column = Array.Empty<int>();
     }

     int[] region = new int[] { };

     //Regions
     for (int row_index = 0; row_index < 6; row_index += 3)
     {
         for(int column_index = 0; column_index < 6; column_index += 3)
         {
              region = region.Append(board[row_index][column_index]).ToArray();
              region = region.Append(board[row_index][column_index + 1]).ToArray();
              region = region.Append(board[row_index][column_index + 2]).ToArray();
              region = region.Append(board[row_index + 1][column_index]).ToArray();
              region = region.Append(board[row_index + 1][column_index + 1]).ToArray();
              region = region.Append(board[row_index + 1][column_index + 2]).ToArray();
              region = region.Append(board[row_index + 2][column_index]).ToArray();
              region = region.Append(board[row_index + 2][column_index + 1]).ToArray();
              region = region.Append(board[row_index + 2][column_index + 2]).ToArray();

              if (region.Distinct().ToArray().Length < 9)
              {
                 return "Try again!";
              }

              region = Array.Empty<int>();
         }
      }
            
      return "Finished!";
  }
}
