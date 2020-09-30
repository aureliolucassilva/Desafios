//Link -> https://www.codewars.com/kata/57feb00f08d102352400026e

function flap_display($lines, $rotors) {
     $alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789";
     $flap = [];
        
     for($a = 0; $a < sizeof($lines); $a++){
         $str = str_split($lines[$a]);
         $n = 0;

         while($n != sizeof($str)){
            for($b = 0; $b < sizeof($str); $b++){
                 if($b >= $n){
                     $idx = strpos($alphabet, $str[$b]) + $rotors[$a][$n];
                     while($idx > strlen($alphabet) - 1) $idx -= strlen($alphabet);
                     $str[$b] = $alphabet[$idx];
                 }
             }

             $n++;
         }

         array_push($flap, implode("", $str));
     }

     return $flap;
}
