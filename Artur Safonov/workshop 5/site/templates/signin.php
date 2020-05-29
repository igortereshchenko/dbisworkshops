<?php
	include "top.php";
	if (isset($_COOKIE["logged"]) && $_COOKIE["logged"] == 1 && !isset($_COOKIE["login"]))
		setcookie("logged", 0, time() + 604800);
	if (((isset($_COOKIE["logged"]) && $_COOKIE["logged"] == 0) || !isset($_COOKIE["logged"])) && isset($_COOKIE["login"]))
		setcookie("login", null, time() - 604800);
	if (isset($_COOKIE["logged"]) && $_COOKIE["logged"] == 1 && isset($_COOKIE["login"]))
		header('Location: cabinet');
	if ($_COOKIE["logerr"] == 1) {
		setcookie("logerr", 0, time()+ 604800);
		$logerr = 1;
	}
	if (isset($_POST["signInButton"])) {
		
		$login = $_POST["login"];
		$password = $_POST["password"];
		$mysqli = new mysqli("localhost", "root", "", "base");
		$mysqli->query("SET NAMES 'utf8'");
		$account = $mysqli->query("SELECT * FROM `users` WHERE `login` = '$login'")->fetch_assoc();
		if ($acccount !== false && password_verify($password, $account["password"])) {
			setcookie("logged", 1, time()+ 604800);
			setcookie("login", $login, time()+ 604800);
			setcookie("fatc", 1, time()+ 604800);
			header('Location: cabinet');
		}
		else {
			setcookie("logerr", 1, time()+ 604800);
			header("Refresh:0");
		}
		
		$mysqli->close();
		
	}
?>

<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<title>SignIn</title>
	
</head>

<body>
	<div class="pushup error" id="pushup">
		<p>Введен неверный логин или пароль</p> 
	</div>
	<?php
		if ($logerr == 1){
			$logerr = 0;
			echo "<script type=\"text/javascript\">
						var obj=document.getElementById(\"pushup\").style;
					
						function winOpen (s, o, obj) {
								obj.visibility=\"visible\";
								obj.opacity=0;
								obj.filter='alpha(opacity=0)';
								winOpen2(s, o, obj);
	
						}
						function winOpen2 (s, o, obj) {
								
							o+=s;
							if(o<100){
								
								obj.opacity=o/100;
								obj.filter='alpha(opacity=o)';
								setTimeout(winOpen2, 55, s, o, obj);
							} else {
								obj.opacity=1;
								obj.filter='alpha(opacity=100)';
							}
								
						}
						
	
						function winClose (s, o, obj) {
							o-=s;
							if(o>0){
								obj.opacity=o/100;
								obj.filter='alpha(opacity='+o+')';
								setTimeout(winClose, 55, s, o, obj);
							} else {
								obj.opacity=0;
								obj.filter='alpha(opacity=0)';
								obj.visibility=\"hidden\";
							}
						}
						winOpen(5, 0, obj);
						
						setTimeout(winClose, 3000, 5, 100, obj);
						
				</script>";
		}
	
	?>
	<?php
		include "header.php";
	?>
	
	<main>
		
	  <div class="rib">
			
		</div>
		
		<div class="paper" style="height: 676px; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; padding-top: 100px;">
			<form style="border: rgba(124,124,124,1.00) 2px solid; height: 400px; width: 800px; border-radius: 100px; padding: 30px; padding-top: 120px; text-align: center; max-height: 400px;" name="signInForm" action="" method="post">
				<label for="log" class="formFont">Логин</label>
				
					<input type="text" class="inputData" id="log" style="width: 300px; margin: 10px 220px 20px 220px" placeholder="Логин" maxlength="16" name="login">
					
				
				
				<label for="pass" class="formFont">Пароль</label>
				<input type="password" class="inputData" id="pass" style="width: 300px; margin: 10px 220px 20px 220px" placeholder="Пароль" name="password">
				
				<input type="submit" value="Вход" class="signInButton" name="signInButton" />
			</form>	
			

				
				<!--<a href="#" class="signinLinks" style="margin: -500px 380px 0px 380px;">Забыли пароль?</a>-->
				<a href="signup" class="signinLinks" style="margin: -400px 380px 0px 380px;">Регистрация</a>
				<div id="loginStatus" style="margin: -400px 300px 0px 300px;"></div>
        </div>

		
	</main>
	
	<?php
		include "footer.php";
	?>
	
	<div class = "end"></div>
</body>
</html>