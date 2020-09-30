//Link -> https://www.codewars.com/kata/5270d0d18625160ada0000e4

using System;
using System.Linq;

public static class Kata
{
  public static int Score(int[] dice) {
      int score = 0;

      for (int side = 1; side <= 6; side++)
      {
          int count = dice.Count(i => i == side);

          if (count >= 1)
          {
              switch (count)
              {
                  case 1:
                     if (side == 1) score += 100;
                     if (side == 5) score += 50;
                     break;
                  case 2:
                     if (side == 1) score += 200;
                     if (side == 5) score += 100;
                     break;
                  case 3: case 5:
                     if (side == 1) score += 1000;
                     if (side == 2) score += 200;
                     if (side == 3) score += 300;
                     if (side == 4) score += 400;
                     if (side == 5) score += 500;
                     if (side == 6) score += 600;
                     break;
                  case 4:
                     if (side == 1) score += 1100;
                     if (side == 2) score += 200;
                     if (side == 3) score += 300;
                     if (side == 4) score += 400;
                     if (side == 5) score += 550;
                     if (side == 6) score += 600;
                     break;
                  case 6:
                     if (side == 1) return score += 2000;
                     if (side == 6) return score += 1200;
                     if (side == 5) return score += 1000;
                     if (side == 4) return score += 800;
                     if (side == 3) return score += 600;
                     if (side == 2) return score += 400;
                     break;
                }
           }
       }

       return score;
  }
}
