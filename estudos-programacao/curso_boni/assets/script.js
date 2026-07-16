function calcularDesconto (precoTexto, percentual){
    let num = parseFloat(precoTexto);
    let desconto = (percentual / 100) * num;
    let Final = num - desconto;
    return Final.toFixed(2);
}

console.log(calcularDesconto(100,10));