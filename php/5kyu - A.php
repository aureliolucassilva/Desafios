//Link -> https://www.codewars.com/kata/526dbd6c8c0eb53254000110

function alphanumeric(string $s): bool {
    $c = str_split($s);

    foreach($c as $item){
        if(ctype_alnum($item) == false) return false;
    }

    return true;
}
