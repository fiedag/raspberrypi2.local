<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">


<title>/home/pi/html/index.php </title>
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
		background-color: #027000;
	}
	.alert {
		height:80pt;
		font-size:25pt;
	}
</style>


</head>
<body>

<div class="container-fluid">
	<div class="row align-items-start top17 bot17 height35">
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="1" data-duration="20" data-state="on"># 1 20s</button>
		</div>
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="1" data-duration="10" data-state="on"># 1 10s</button>
		</div>
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="1" data-state="off"># 1 OFF</button>
		</div>
	</div>
	<div class="row align-items-center top17 bot17">
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="2" data-duration="20" data-state="on"># 2 20s</button>
		</div>
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="2" data-duration="10" data-state="on"># 2 10s</button>
		</div>
		<div class="col-4">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="2" data-state="off"># 2 OFF</button>
		</div>
	</div>
	<div class="row align-items-center top17 bot17">
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="3" data-duration="20" data-state="on"># 3 20s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="3" data-duration="10" data-state="on"># 3 10s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="3" data-state="off"># 3 OFF</button>
		</div>
	</div>
	<div class="row align-items-center top17 bot17">
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="4" data-duration="20" data-state="on"># 4 20s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="4" data-duration="10" data-state="on"># 4 10s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="4" data-state="off"># 4 OFF</button>
		</div>
	</div>
	<div class="row align-items-center top17 bot17">
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="5" data-duration="20" data-state="on"># 5 20s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="5" data-duration="10" data-state="on"># 5 10s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="5" data-state="off"># 5 OFF</button>
		</div>
	</div>
	<div class="row align-items-end top17 bot17">
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="6" data-duration="20" data-state="on"># 6 20s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="6" data-duration="10" data-state="on"># 6 10s</button>
		</div>
		<div class="col">
			<button type="button" class="btn btn-primary btn-large btn-block" class="sprinkler" data-id="6" data-state="off"># 6 OFF</button>
		</div>
	</div>



	<div id="statusmsg" class="alert alert-primary" role="alert">
	</div>

</div>




<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous">
	
</script>


<script>
$(document).ready(function() {
    $("button").click(function() {
        $.get("script.php?sprinkler=" + $(this).data("id") + "&state=" + $(this).data("state") + "&duration=" + $(this).data("duration"), function(data, status) {
        	$("#statusmsg").text(data);
        });
    });
});
</script>


</body>
</html>
