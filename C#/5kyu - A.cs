// Link -> https://www.codewars.com/kata/56baeae7022c16dd7400086e

using System;
using System.Linq;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class PhoneDir 
{
    public static string Phone(string strng, string num)
    {
            string[] bookEntries = strng.Split('\n');
            string searchResult = $"Phone => {num}, ";
            string info = string.Empty;

            foreach (string entries in bookEntries)
            {
                if(entries.Contains(num))
                {
                    if(info == "")
                    {
                        string number = Regex.Match(entries, @"[0-9]{1,}-[0-9]{3}-[0-9]{3}-[0-9]{4}").ToString();

                        if(number == num)
                        {
                            info = entries;
                        }
                        else
                        {
                            continue;
                        } 
                    }
                    else
                    {
                        return $"Error => Too many people: {num}";
                    }
                }
            }

            if(info == "")
            {
                return $"Error => Not found: {num}";
            }

            string name = Regex.Match(info, @"<.*>").ToString();
            name = name.Replace('<', ' ');
            name = name.Replace('>', ' ');
            name = name.Trim();
            searchResult += $"Name => {name}, ";

            string addressCode = Regex.Match(info, @"[A-Z]{1,}-[0-9]{5}").ToString();
            string address = string.Empty;
            string addressNumber = string.Empty;
            string[] infoArray = info.Split(' ');
            infoArray = infoArray.Where(x => !string.IsNullOrEmpty(x)).ToArray();

            foreach (string item in infoArray)
            {
                if(!item.Contains('<') && !item.Contains('>') && !Regex.Match(item, @"\d+").Success && !Regex.Match(item, @"[_]\W+").Success)
                {
                    if(item.Contains("PO") || item.Contains("Box"))
                    {
                        continue;
                    }

                    Regex rgx = new Regex("[^a-zA-Z0-9 .]");
                    address += $"{item} ";
                    address = rgx.Replace(address, " ");
                   
                    if(address[address.Length - 2] == ' ')
                    {
                        address = address.Substring(0, address.Length - 1);
                    }
                }
                else if(Regex.Match(item, @"^[0-9]+").Success)
                {
                    addressNumber = item;
                    Regex rgx = new Regex("[^a-zA-Z0-9 ]");
                    addressNumber = rgx.Replace(addressNumber, "");
                }
            }

            address = address.Trim();

            if(!info.Contains("PO"))
            {
                searchResult += $"Address => ";
            }
            else
            {
                searchResult += $"Address => PO Box ";
            }
            

            if (addressNumber != "" && addressCode != "")
            {
                searchResult += $"{addressNumber} {address} {addressCode}";
            }
            else if(addressNumber == "" && addressCode != "")
            {
                searchResult += $"{address} {addressCode}";
            }
            else if (addressNumber != "" && addressCode == "")
            {
                searchResult += $"{addressNumber} {address}";
            }
            else if (addressNumber == "" && addressCode == "")
            {
                searchResult += $"{address}";
            }

            return searchResult;
    }
}
