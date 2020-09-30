//Link -> https://www.codewars.com/kata/57eae20f5500ad98e50002c5

namespace Solution 
{
  public static class SpacesRemover
  {
    public static string NoSpace(string input)
    {
        input = input.Replace(" ", string.Empty);

        return input;
    }  
  }
}
