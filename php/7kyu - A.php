<?php

//Link -> https://www.codewars.com/kata/5b358a1e228d316283001892

function get_strings($city) {
     $letters = str_split(strtolower($city));
     $counts = array_count_values($letters);
     $returnString = "";
    
     foreach($counts as $key => $value){
        if($key != " "){
             $returnString .= $key . ":";

             for($i = 1; $i <= $value; $i++){
                $returnString .= "*";
             }
    
             $returnString .= ',';
        }
     }

     return substr($returnString, 0, -1);
  }

?>
