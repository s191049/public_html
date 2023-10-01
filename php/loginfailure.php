<?php
function loginerror($errmessage = ""){
  echo "<script>alert('{$errmessage}');</script>";
  echo "<script>location.href = './index.php';</script>";
  //header('Location: ./index.php');
  //exit();
}
?>
