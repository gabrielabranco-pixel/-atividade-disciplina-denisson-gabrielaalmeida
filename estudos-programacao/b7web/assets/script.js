
/*
function calcularDesconto (precoTexto, percentual){
    let num = parseFloat(precoTexto);
    let desconto = (percentual / 100) * num;
    let Final = num - desconto;
    return Final.toFixed(2);
}

console.log(calcularDesconto(100,10));


function renderizarLista(Lista){
    let ul = document.querySelector('ul')
    ul.innerHTML = '';

}
*/

#callback 
function fazerPizza(sabor, callback){
    console.log("Fazendo a pizza de ${sabor}...");
    setTimeout(() => {
      callback
    }, 1500);
}

//Função que será chamada quando a pizza estiver pronta 
function pizzaPronta(){
   console.log("A pizza está pronta! Aproveite!"); 
}

//Chamando a função fazerPizza e passando o callback pizzaPronta
fazerPizza("Calabresa", pizzaPronta);

// EXEMPLO DE CALLBACK COM FUNÇÃO ANÔNIMA 
fazerPizza("Mussarela", function(){
    console.log("A pizza de ${sabor} esta pronta! Aproveite!");
//funciona para ter um tipo de retorno personalizado, para a uma função especifica 
});
