//Link -> https://www.codewars.com/kata/546d15cebed2e10334000ed9

using System;
using System.Linq;

public class Runes
{
  public static int solveExpression(string expression)
  {
      int missingDigit = -1;
      string[] numbers = new string[] { };
      int operandIndex = 0;
      int equalIndex = 0;
      char operand = '\0';

      if (expression.Contains('*'))
      {
          operand = '*';
          operandIndex = expression.IndexOf('*');
          equalIndex = expression.IndexOf('=');
          numbers = numbers.Append(expression.Substring(0, operandIndex)).ToArray();
          numbers = numbers.Append(expression.Substring(operandIndex + 1, equalIndex - operandIndex - 1)).ToArray();
          numbers = numbers.Append(expression.Substring(equalIndex + 1)).ToArray();
      }
      else if(expression.Contains('+'))
      {
          operand = '+';
          operandIndex = expression.IndexOf('+');
          equalIndex = expression.IndexOf('=');
          numbers = numbers.Append(expression.Substring(0, operandIndex)).ToArray();
          numbers = numbers.Append(expression.Substring(operandIndex + 1, equalIndex - operandIndex - 1)).ToArray();
          numbers = numbers.Append(expression.Substring(equalIndex + 1)).ToArray();
      }
      else
      {
          operand = '-';
          operandIndex = expression.Substring(1).IndexOf('-') + 1;
          equalIndex = expression.IndexOf('=');
          numbers = numbers.Append(expression.Substring(0, operandIndex)).ToArray();
          numbers = numbers.Append(expression.Substring(operandIndex + 1, equalIndex - operandIndex - 1)).ToArray();
          numbers = numbers.Append(expression.Substring(equalIndex + 1)).ToArray();
      }

      string firstNumber = numbers[0];
      string secondNumber = numbers[1];
      string thirdNumber = numbers[2];
      string knownNumbers = firstNumber + secondNumber + thirdNumber;
      char[] unknownNumbers = new char[] { };

      for(int i = 0; i <= 9; i++)
      {
          if(knownNumbers.Contains(Char.Parse(i.ToString())) == false)
          {
              unknownNumbers = unknownNumbers.Append(Char.Parse(i.ToString())).ToArray();
          }
      }

      bool correctForm = true;
          
      if (operand == '*')
      {
          foreach(char unknownNumber in unknownNumbers)
          {
             firstNumber = firstNumber.Replace('?', unknownNumber);
             secondNumber = secondNumber.Replace('?', unknownNumber);
             thirdNumber = thirdNumber.Replace('?', unknownNumber);

             if (Int32.Parse(firstNumber) * Int32.Parse(secondNumber) == Int32.Parse(thirdNumber))
             {
                 if (firstNumber.Length > 1 && firstNumber[0] == '0') correctForm = false;
                 if (secondNumber.Length > 1 && secondNumber[0] == '0') correctForm = false;
                 if (thirdNumber.Length > 1 && thirdNumber[0] == '0') correctForm = false;
                        
                 if(correctForm == true)
                 {
                     missingDigit = Int32.Parse(unknownNumber.ToString());
                     break;
                 }
                        
              }

              firstNumber = numbers[0];
              secondNumber = numbers[1];
              thirdNumber = numbers[2];
              correctForm = true;
            }
      }
      else if (operand == '+')
      {
            foreach (char unknownNumber in unknownNumbers)
            {
                firstNumber = firstNumber.Replace('?', unknownNumber);
                secondNumber = secondNumber.Replace('?', unknownNumber);
                thirdNumber = thirdNumber.Replace('?', unknownNumber);

                if (Int32.Parse(firstNumber) + Int32.Parse(secondNumber) == Int32.Parse(thirdNumber))
                {
                    if (firstNumber.Length > 1 && firstNumber[0] == '0') correctForm = false;
                    if (secondNumber.Length > 1 && secondNumber[0] == '0') correctForm = false;
                    if (thirdNumber.Length > 1 && thirdNumber[0] == '0') correctForm = false;

                    if (correctForm == true)
                    {
                        missingDigit = Int32.Parse(unknownNumber.ToString());
                        break;
                    }

                }

                firstNumber = numbers[0];
                secondNumber = numbers[1];
                thirdNumber = numbers[2];
                correctForm = true;
            }
      }
      else if (operand == '-')
      {
          foreach (char unknownNumber in unknownNumbers)
          {
              firstNumber = firstNumber.Replace('?', unknownNumber);
              secondNumber = secondNumber.Replace('?', unknownNumber);
              thirdNumber = thirdNumber.Replace('?', unknownNumber);

              if (Int32.Parse(firstNumber) - Int32.Parse(secondNumber) == Int32.Parse(thirdNumber))
              {
                   if (firstNumber.Length > 1 && firstNumber[0] == '0') correctForm = false;
                   if (secondNumber.Length > 1 && secondNumber[0] == '0') correctForm = false;
                   if (thirdNumber.Length > 1 && thirdNumber[0] == '0') correctForm = false;

                   if (correctForm == true)
                   {
                       missingDigit = Int32.Parse(unknownNumber.ToString());
                       break;
                   }

               }

               firstNumber = numbers[0];
               secondNumber = numbers[1];
               thirdNumber = numbers[2];
               correctForm = true;
           }
       }

       return missingDigit;
  }
}
