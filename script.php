<?php

$cmd = 'python3 pool.py -pump ' . $_GET['duration'];


exec($cmd, $output);

foreach($output as $line) {
	echo $line . "\n";
}

?>
