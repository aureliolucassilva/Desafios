<?php

//Link -> https://www.codewars.com/kata/56af1a20509ce5b9b000001e

function travel($r, $zipcode) {
     if(strlen($r) == 0 || strlen($zipcode) == 0) return $zipcode.":/";

     $adress = explode(",", $r);
     $zipCodeAdress = [];      

     foreach($adress as $item){
        $zip = substr($item, -8);
        if($zip == $zipcode){
            $organizedAdress = [];
            $streetTown = str_replace(" ".$zipcode, "", explode(' ', $item, 2)[1]);
            $houseNumber = explode(' ', $item, 2)[0];
            array_push($organizedAdress, $streetTown);
            array_push($organizedAdress, $houseNumber);
            array_push($zipCodeAdress, $organizedAdress);
        }
     }

     if(sizeof($zipCodeAdress) == 0){
        return $zipcode.":/";
     }

     $newR = $zipcode.":";
     for($i = 0; $i < sizeof($zipCodeAdress); $i++){
        if($i != sizeof($zipCodeAdress) - 1) $newR .= $zipCodeAdress[$i][0].",";
        else  $newR .= $zipCodeAdress[$i][0]."/";
     }

     for($i = 0; $i < sizeof($zipCodeAdress); $i++){
        if($i != sizeof($zipCodeAdress) - 1) $newR .= $zipCodeAdress[$i][1].",";
        else  $newR .= $zipCodeAdress[$i][1];
     }

     return $newR;
}


?>
