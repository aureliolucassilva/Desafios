//Link -> https://www.codewars.com/kata/515decfd9dcfc23bb6000006

using System;
using System.Linq;

namespace Solution
{
    class Kata
    {
        public static bool is_valid_IP(string ipAddres)
        {
            string[] octets = ipAddres.Split(".");
            bool result = false;
            int octet = 0;
            
            if(octets.Length == 4)
            {
                foreach(string oct in octets)
                {
                    if(oct.Contains(" ") == false && oct.Contains("-") == false)
                    {
                        try
                        {
                            octet = int.Parse(oct);

                            if (octet <= 255 && octet >= 0)
                            {
                                if (oct[0] != '0' && oct.Length > 1)
                                {
                                    result = true;
                                }
                                else if (oct.Length == 1)
                                {
                                    result = true;
                                }
                                else
                                {
                                    result = false;
                                    break;
                                }

                            }
                            else
                            {
                                result = false;
                                break;
                            }
                        }
                        catch (FormatException)
                        {
                            result = false;
                            break;
                        }
                    }
                    else
                    {
                        result = false;
                        break;
                    }
                }
            }

            return result;
        }
    }
}
