<!DOCTYPE html>

<head>
    <title></title>
</head>
<body>
   <?php 
        ini set('display errors'.1); ini_set('display_starttup_errors'.1); error_reporting(E_ALL); //validando se existe algum erro no código php
    
        //verifica se existe conexão com o bd, caso não tenta criar uma bi==nova 
        $conexao = mysqli connect ("Localhost", "root", "Redes123!") //porta,usuário, senha
        or die("Erro de conexão com banco de dados"); //caso não consiga conectar mostra a mensagem de erro mostrada na conexão 

        select_db = mysqli_select_db($conexao, "despesas"); //seleciona o banco de dados 

        //abaixo atribuimos os valores provenientes do formulário pelo método POST 
</body>
</html>