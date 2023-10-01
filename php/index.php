<?php
  $login_file = file_get_contents('./login.php');
  $content = "
    <h2>ログイン</h2>
    {$login_file}
  ";
?>
<?php include('./template.php'); ?>
