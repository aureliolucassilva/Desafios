<?php

//Link -> https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

function duplicateCount($text) {
    $letters = str_split(strtolower($text));
    $count = array_count_values($letters);
    $duplicates = 0;

    foreach($count as $number){
       if($number > 1){
           $duplicates++;
       }
    }

    return $duplicates;
}

?>
