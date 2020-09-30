//Link -> https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

using System;
using System.Linq;
using System.Collections.Generic;
public class PickPeaks
{
    public static Dictionary<string, List<int>> GetPeaks(int[] arr)
    { 
            
        Dictionary<string, List<int>> result = new Dictionary<string, List<int>> { };
        List<int> peaks = new List<int> { };
        List<int> positions = new List<int> { };
        int plateau = Int32.MinValue;
        int index_plateau = Int32.MinValue;
            
        for(int i = 1; i <= arr.Length -2; i++)
        {
            if (arr[i - 1] < arr[i] && arr[i] > arr[i + 1])
            {
                peaks = peaks.Append(arr[i]).ToList();
                positions = positions.Append(i).ToList();
            }

            if (arr[i - 1] < arr[i] && arr[i] == arr[i + 1])
            {
                plateau = arr[i];
                index_plateau = i;
            }

            if (plateau > arr[i])
            {
                peaks = peaks.Append(plateau).ToList();
                positions = positions.Append(index_plateau).ToList();
                plateau = Int32.MinValue;
                index_plateau = Int32.MinValue;
            }
            else if (i == arr.Length - 2)
            {
                if (plateau > arr[i + 1])
                {
                    peaks = peaks.Append(plateau).ToList();
                    positions = positions.Append(index_plateau).ToList();
                }
            }
            else if (plateau < arr[i])
            {
                plateau = Int32.MinValue;
                index_plateau = Int32.MinValue;
            }
        }

        result.Add("pos", positions);
        result.Add("peaks", peaks);
                
        return result;
    }
}
