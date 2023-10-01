<?php
require_once('./loginfailure.php');
//require_once('./database.php');
session_start();
if(!empty($_POST['authid']) && !empty($_POST['password'])){
  //フォームからPOSTされたとき
  //try{$account = trylogin($_POST['authid'], $_POST['password']);}catch{ loginerror("接続失敗")};
  /* 未実装
  if(isset($account)){
    //ログイン成功
    loginerror("ログイン成功");
  }else{
    //ログイン失敗
    loginerror("IDまたはパスワードを確認してください");
  }
  */
}else{
  //フォームの値がないとき
  loginerror("フォームに値を入力してください");
  exit();
}

?>
