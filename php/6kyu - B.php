<?php

//Link -> https://www.codewars.com/kata/59df2f8f08c6cec835000012

function meeting($s) {
    $guests = explode(";", strtoupper($s));
    $fullName = [];
    $newS = "";

    foreach($guests as $item){
        array_push($fullName, array_reverse(explode(":", $item)));
    }

    sort($fullName);

    foreach($fullName as $item){
        $newS .= "(".$item[0].", ".$item[1].")";
    }

    return $newS;
}

?>
