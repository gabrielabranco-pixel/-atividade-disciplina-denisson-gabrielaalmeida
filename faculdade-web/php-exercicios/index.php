<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
 <?php
//código php
// phpinfo(); mostra todas as informações do php instalado 


//2 - como imprimir na tela
echo "Olá Mundo!";


//3 - variável
$n1 = 10; - declaração de variável
$n2 = "5";


$n3 = $n1 + $n2; oper. aritmético
echo $n3;


//4
$numero = 0;
if($numero < 20){
    echo "$numero é menor que 20";
}
else{
    echo "$numero é maior que 20";
}
$conexao = mysqli_connect("localhost", "root","", "gabi_banco_de_dados", 3306 );
//$conexão = variavel que receve os dados de acesso ao banco
//onde esta o banco = loscalhost
//usuario = root
//senha = em branco
//nome do banco = mysql
//porta padrão MYSQL = 3306

?> 
</body>
texto html projeto php
</html>
