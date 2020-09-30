// Link -> https://www.codewars.com/kata/530e15517bc88ac656000716

using System;
using System.Linq;

public class Kata
{
  public static string Rot13(string message)
  {
       int[] ascii = new int[] { };

       foreach (char item in message.ToCharArray())
       {
          ascii = ascii.Append((int)item).ToArray();
       }

       char[] newMessage = new char[] { };

       foreach(int item in ascii)
       {
          if (item + 13 > 90 && item <= 90)
          {
              newMessage = newMessage.Append((char)(item + 13 - 90 + 64)).ToArray();
          }
          else if (item + 13 > 122 && item <= 122)
          {
              newMessage = newMessage.Append((char)(item + 13 - 122 + 96)).ToArray();
          }
          else if (item >= 0 && item <= 64 || item >= 91 && item <= 96 || item >= 123 && item <= 127)
          {
              newMessage = newMessage.Append((char)(item)).ToArray();
          }
          else
          {
              newMessage = newMessage.Append((char)(item + 13)).ToArray();
          }

       }

       return new string(newMessage);
  }
}
