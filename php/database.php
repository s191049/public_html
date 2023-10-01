<?php
function trylogin($authid, $password){
  try{
    $dsn = 'mysql:host=localhost;dbname=minachan;charset=UTF-8';
    $db_user = "minachan";
    $db_pass = "1967011003";
    $pdo = new PDO($dsn, $db_user, $db_pass);
    $stmt = $pdo->query("SELECT * FROM users WHERE id = ? AND password = ?");
    $stmt->execute(array($authid, $password));
    while($row=$stmt->fetch()){
      $result['num'] = $row['num'];
      $result['authid'] = $row['id'];
    }
    if(isset($result)){
      return $result;
    }
  }catch(PDOException $e){
    echo "failure";
  }
}
?>
