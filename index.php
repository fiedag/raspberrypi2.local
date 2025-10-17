<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">



<title>Welcome to nginx in the pi user directorry!</title>
<style>

    body {
        width: 100%;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }



	.top5 { margin-top:5px; }
	.top7 { margin-top:7px; }
	.top10 { margin-top:10px; }
	.top15 { margin-top:15px; }
	.top17 { margin-top:17px; }
	.top30 { margin-top:30px; }

	.bot17 { margin-bottom:17px; }

	.height5 { height:5%; }
	.height10 { height:10%; }
	.height35 { height:35%; }

	.btn {
		height:80pt;
		font-size: 25pt;
	}
	.alert {
		height:80pt;
		font-size:25pt;
	}
</style>


</head>
<body>
<h1>Pool Pump Trigger</h1>

<div class="container-fluid">

    <?php 

    $durations = array("5","10","20","60","120");

    foreach($durations as $val) {
    	$out = <<<EOF
    	<div class="row align-items-start top17 bot17 height35">  <div class="col-4"> <button type="button" class="btn btn-primary btn-large btn-block" class="pump" data-id="1" data-duration="$val" data-state="on">$val</button> </div></div>
EOF;
    echo $out;
    }

    ?>

	<div id="statusmsg" class="alert alert-primary" role="alert">
	</div>

</div>




<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous">
	
</script>


<script>
$(document).ready(function() {
    $("button").click(function() {
        alert("script.php?pump=" + $(this).data("id") + "&duration=" + $(this).data("duration"));
        $.get("script.php?pump=" + $(this).data("id") + "&duration=" + $(this).data("duration"), function(data, status) {
        	$("#statusmsg").text(data);
        });
    });
});
</script>


</body>
</html>
