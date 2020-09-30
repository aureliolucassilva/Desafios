<?php

//Link -> https://www.codewars.com/kata/520446778469526ec0000001

function nestedA($arr, $x){
    $arrNested = [];
    foreach($arr as $item){
        if(is_array($item)){
            array_push($GLOBALS[$x], sizeof($item));
            array_push($arrNested, $item);
        } else{
            array_push($GLOBALS[$x], 1);
        }
    }

    if(sizeof($arrNested) != 0){
        foreach($arrNested as $item){
            nestedB($item, $x);
        }
    }
}

function nestedB($arr, $x){
    $arrNested = [];
    foreach($arr as $item){
        if(is_array($item)){
            array_push($GLOBALS[$x], sizeof($item));
            array_push($arrNested, $item);
        } else{
            array_push($GLOBALS[$x], 1);
        }
    }

    if(sizeof($arrNested) != 0){
        foreach($arrNested as $item){
            nestedA($item, $x);
        }
    }
}

function same_structure_as(array $a, array $b): bool{
    $bStructure = [sizeof($b)];
    $aStructure = [sizeof($a)];

    $GLOBALS['a'] = $aStructure;
    $GLOBALS['b'] = $bStructure;
        

    foreach($a as $item){
        if(is_array($item)){
            array_push($GLOBALS['a'], sizeof($item));
            nestedA($item, 'a');
        } else{
            array_push($GLOBALS['a'], 1);
        }
    }

    foreach($b as $item){
        if(is_array($item)){
            array_push($GLOBALS['b'], sizeof($item));
            nestedB($item, 'b');
        } else{
            array_push($GLOBALS['b'], 1);
        }
    }

    if($GLOBALS['a'] === $GLOBALS['b']) return true;
    else return false;
}

?>
