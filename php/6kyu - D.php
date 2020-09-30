<?php

//Link -> https://www.codewars.com/kata/559536379512a64472000053

function playPass($s, $n) {
     $chars = str_split($s);
     $newChars = [];
     $newS= "";

     foreach($chars as $letter){
         switch($letter){
             case is_numeric($letter):
                 $ascii = 9 - (int)$letter;
                 array_push($newChars, (string)$ascii);
                 break;
             case ctype_alnum($letter):
                 $ascii = ord(strtolower($letter)) + $n;
                 if($ascii > 122){
                    $ascii = 96 + ($ascii - 122);
                 }
                 array_push($newChars, chr($ascii));
                 break;
             case "0":
                 $ascii = 9;
                 array_push($newChars, (string)$ascii);
                 break;
             default:
                 array_push($newChars, $letter);
        }
     } 

     for($idx = 0; $idx < count($newChars); $idx++){
         if($idx % 2 == 0){
            $newS = $newS.strtoupper($newChars[$idx]);
         } else{
            $newS = $newS.strtolower($newChars[$idx]);
         }
     }

     return strrev($newS);
}

?>
