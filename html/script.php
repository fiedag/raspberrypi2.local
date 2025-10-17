<?php

if($_GET['state']=='off') {
	$cmd = 'python3 /home/pi/sprinklers3.py -r' . $_GET['sprinkler'] . ' 0,0';
}
else {
	$cmd = 'python3 /home/pi/sprinklers3.py -r' . $_GET['sprinkler'] . ' ' . $_GET['duration'] . ',0';
}
echo $cmd . "\n";


e.xec($cmd, $output);

foreach($output as $line) {
	echo $line . "\n";
}

?>
