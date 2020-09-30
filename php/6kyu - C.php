<?php

//Link -> https://www.codewars.com/kata/58223370aef9fc03fd000071

function dashatize(int $num): string {
      $str = (string)$num;
      $chars = str_split($str);
      $dashs = "";

      foreach($chars as $char){
          if((int)$char % 2 != 0 && substr($dashs, -1) != '-'){
              $dashs = $dashs.'-'.$char.'-';
          } else if((int)$char % 2 != 0 && substr($dashs, -1) == '-'){
              $dashs = $dashs.$char.'-';
          } else{
              $dashs = $dashs.$char;
          }
      }

      if(substr($dashs, -1) == '-'){
          $dashs = substr_replace($dashs, "", -1);
      } 
       
      if($dashs[0] == '-'){
          $dashs = ltrim($dashs, '-');
      }

      return $dashs;
}

?>
