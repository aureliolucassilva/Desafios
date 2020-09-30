<?php

//Link -> https://www.codewars.com/kata/52449b062fb80683ec000024

function generateHashtag($str) {
     if(strlen($str) == 0) return false;
     $words = explode(" ", strtolower($str));
     $words = array_filter($words);
     if(count($words) == 0) return false;
     $hashtag = "#";

     foreach($words as $item){
         $hashtag = $hashtag.ucfirst($item);
     }

     if(strlen($hashtag) <= 140) return $hashtag;
     else return false;
}

?>
