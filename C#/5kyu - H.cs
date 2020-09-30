//Link -> https://www.codewars.com/kata/52685f7382004e774f0001f7

using System;
using System.Linq;

public static class TimeFormat
{
    public static string GetReadableTime(int seconds)
    {
         double hours = 0;
         double minutes = 0;
         double sec = 0;
         string result = string.Empty;

         hours = (double)seconds / 3600;
         minutes = (hours - Math.Floor(hours)) * 60;
         sec = (minutes - Math.Floor(minutes)) * 60;

         result = string.Format("{0:00}:{1:00}:{2:00}", Math.Floor(hours), Math.Floor(minutes), sec);

         return result;
    }
}
