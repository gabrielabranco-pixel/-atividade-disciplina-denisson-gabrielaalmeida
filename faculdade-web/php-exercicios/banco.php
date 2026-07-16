<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto PHP</title>
</head>
<body>
  TEXTO LIVRE
  <?php
    ini_set ('display_erros', 1);
    ini set('display startup errors', 1);
    error reporting(E ALL);

    $conexao = mysqli_connect('localhost', 'root', '', 'mysql', '3306');
    //$conexão --> variavel que recebe os dados de acesso ao banco de dados 
    //onde esta o banco = localhost 
    //usuario = root
    //senha = em branco
    //nome do banco = mysql
    //porta padrao MYSQL = 3306
    print $conexao;

    if($conexao){
        echo "Eba, conectei no banco!";
    } else {
        echo "Ops, deu certo";
    }
  ?>
</body>
</html>