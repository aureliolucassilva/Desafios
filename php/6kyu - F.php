<?php

//Link -> https://www.codewars.com/kata/550554fd08b86f84fe000a58

function inArray($array1, $array2) {
      $result = [];
      $array2String = join(",", $array2);

      foreach($array1 as $str){
          if(strpos($array2String, $str) !== false){
              array_push($result, $str); 
          }
      }

      sort($result);
      return $result;
}


?>
