<?php

//Link -> https://www.codewars.com/kata/5287e858c6b5a9678200083c

function narcissistic(int $value): bool {
    $valueString = (string)$value;
    $stringSize = strlen($valueString);
    $bigNumber = 0;

    for($i = 0; $i < $stringSize; $i++){
        $number = (int)$valueString[$i];
        $bigNumber += pow($number, $stringSize);
    }

    switch($bigNumber){
        case $value:
          return true;
        default:
          return false;
    }
}

?>
