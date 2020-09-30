//Link -> https://www.codewars.com/kata/5544c7a5cb454edb3c000047

public class BouncingBall {
  
  public static int bouncingBall(double h, double bounce, double window) {
      // your code
       int sights = 1;

            if(h > 0 && bounce < 1 && 0 < bounce && h > window)
            {
                do
                {
                    if (h * bounce > window)
                    {
                        sights += 2;
                    }

                    h = h * bounce;
                }
                while (h > window);

                return sights;
            }
            else
            {
                return -1;
            }
  }
}
