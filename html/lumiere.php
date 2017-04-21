<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" type="text/css" href="lumiere.css">
		<title>widget maison connectée</title>
	</head>
	<body>
		<h1>Maison connectée v.1<br>Projet ISN</h1>
		<p>Ici vous pouvez controler directement vos différents volets:</p>
		<img src="lamp.png" alt="lamp" style="width:304px;height:288px;">
	<h2>
		<meta name="viewport" content="width=device-width" />
				<form method="get" action="lumiere.php">
						<input type="submit" value="I" name="on" class="btn0 button">
						<input type="submit" value="O" name="off" class="btn0 button">
				</form>
				<?php
				$setmode2 = shell_exec("/usr/local/bin/gpio -g mode 2 out");
				if(isset($_GET['on'])){
						$gpio_on = shell_exec("/usr/local/bin/gpio -g write 2 1");
						echo "Lumiere allumee";
				}
				else if(isset($_GET['off'])){
						$gpio_off = shell_exec("/usr/local/bin/gpio -g write 2 0");
						echo "Lumiere eteinte";
				}
				?>
	</h2>
	<h2>
		<meta name="viewport" content="width=device-width" />
				<form method="get" action="lumiere.php">
						<input type="submit" value="I" name="on1" class="btn0 button">
						<input type="submit" value="O" name="off1" class="btn0 button">
				</form>
				<?php
				$setmode2 = shell_exec("/usr/local/bin/gpio -g mode 3 out");
				if(isset($_GET['on1'])){
						$gpio_on = shell_exec("/usr/local/bin/gpio -g write 3 1");
						echo "Lumiere allumee";
				}
				else if(isset($_GET['off1'])){
						$gpio_off = shell_exec("/usr/local/bin/gpio -g write 3 0");
						echo "Lumiere eteinte";
				}
				?>
	</h2>
	<body>
	</head>
</html>

