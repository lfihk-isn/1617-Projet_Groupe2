<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" type="text/css" href="VE.css">
		<title>M.C.: Ventilateurs</title>
	<link rel="icon" type="image/png" href="ventilo.png" />
	</head>
	<body>
		<h1>Maison connect&#233;e v.1<br>Projet ISN</h1>
		<p>Ici vous pouvez controler directement vos diff&#233;rents ventilateurs:</p>
		<img src="ventilo.png" alt="lamp" style="width:304px;height:288px;">
	<h2>
		<meta name="viewport" content="width=device-width" />
				<form method="get" action="ventilateurs.php">
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
	<h2><a href="index.html"><button type="button" class="btn3 button"><span>Retour &#224; la page d'accueil</button> </a> </p></h2>
	
	<body>
	</head>
</html>