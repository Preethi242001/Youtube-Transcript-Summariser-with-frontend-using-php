<?php
	
   echo "<textarea name='mydata' rows='250' cols='200 ' >\n";
   $video_url= $_REQUEST["video_url"];
   $tlang = $_REQUEST["langauage"];

   echo "php code:arguments received video_url as : [$video_url]";
   echo "\n";
  
   echo "php code:arguments received language code as : [$tlang]";
   echo "\n";

  
   $pgm = 'C:\xampp\htdocs\project\yts.py';
   # passing arguments to python program with space as separator
   $pgm = $pgm .  " ". $video_url. " " . $tlang;
   
   echo " in php: shell_exec started program: [$pgm]";
   echo "\n";
  
   
   $command_exec = escapeshellcmd($pgm);
   echo $command_exec;
   $str_output = shell_exec($command_exec);
   
   echo " in php: shell_exec completed program: [$pgm]";
   echo $str_output;
   #echo htmlspecialchars($str_output)."\n";
  
  
   echo "</textarea >";
  
  
?>

  

  
  
?>


