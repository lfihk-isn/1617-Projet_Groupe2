<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" type="text/css" href="VO.css">
		<title>M.C.: Lumieres</title>
	<link rel="icon" type="image/png" href="lamp.png" />
	</head>
	<body>
		<h1>Maison connect&#233;e v.1<br>Projet ISN</h1>
		<p>Ici vous pouvez controler directement vos diff&#233;rentes lumi&#232;res:</p>
		<img src="lamp.png" alt="lamp" style="width:204px;height:228px;">
		<p>Lumi&#232;re 1:</p>
	<h2>
		<meta name="viewport" content="width=device-width" />
				<form method="get" action="lumieres.php">
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
	<p>Lumi&#232;re 2:</p>
	<h2>
		<meta name="viewport" content="width=device-width" />
				<form method="get" action="lumieres.php">
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
				 
				 <p> </p>
				 
		
	</h2>
	<h2><a href="index.html"><button type="button" class="btn3 button"><span>Retour &#224; la page d'accueil</button> </a> </p></h2>
	
	<body>
	</head>
</html>

