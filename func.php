<?php

$string='This is an example';
$w = str_word_count($string);

echo $w;

function echo_ip () {
global $ip;
    $s = 'ur ip addr is'.$ip;
    echo $s;
}

//echo_ip () 

// function dd($date, $month, $year)
// {
//     $r = $date + $month+ $year;

//     return $r;
// }

// function mm($date, $month)
// {
//     $r = $date*$month;

//     return $r;
// }

// echo  mm(4,4)/dd(1,1,0);



?>

