//Link -> https://www.codewars.com/kata/576757b1df89ecf5bd00073b

using System;
using System.Linq;

public class Kata
{
  public static string[] TowerBuilder(int nFloors)
  {
      string[] tower = new string[nFloors];
      string base_floor = string.Empty;
            

      for(int i = 0; i < nFloors * 2 - 1; i++)
      {
         base_floor += "*";
      }

      char[] upper_floor = base_floor.ToCharArray();
      tower[0] = base_floor;

      Tuple<int, int> index = new Tuple<int, int>(0, nFloors * 2 - 2);
      int step = 0;

      while(index.Item1 + step != index.Item2 - step && step < nFloors-1)
      {
         upper_floor[index.Item1 + step] = Char.Parse(" ");
         upper_floor[index.Item2 - step] = Char.Parse(" ");

         tower[step + 1] = new string(upper_floor);
         step++;
      }

      Array.Reverse(tower);

      return tower;
  }
}
