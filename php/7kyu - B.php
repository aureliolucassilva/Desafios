<?php

//Link -> https://www.codewars.com/kata/5841f680c5c9b092950001ae

function generate_integers(int $m, int $n): array {
    $sequence = array();

    for($i = $m; $i <= $n; $i++){
        array_push($sequence, $i);
    }

    return $sequence;
}

?>
