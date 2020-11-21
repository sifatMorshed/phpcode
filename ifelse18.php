<?php

$cat = 'caty';
$n1 = 12;
$n1++;
$n2=30;
$n3=29;
$s = '30';
//$n1 /= 6;

$text= 'hello';
$text .= ' world';

//echo $n1;
//echo $text;
echo $n1;
//echo $n1%$n2;

if ($n3===$s)

{
    echo 'ok';
}

else if (!($n3==$n1) && !($n3==$n2))
{
    echo "Number must be between $n1 and $n3";
}

else
{
    echo "other";
}

?>