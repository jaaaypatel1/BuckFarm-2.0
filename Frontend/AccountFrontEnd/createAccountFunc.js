var accType = document.getElementById("accType");
const divShop = document.getElementById("shop");
const divBus = document.getElementById("bus");
accType.addEventListener("change", function(){
    const acc = accType.value
    if(acc.equals("Shopper")){
        divShop.style.visibility='visible';
        divBus.style.visibility='hidden';
    }else{
        divBus.style.visibility='visible';
        divShop.style.visibility='hidden';
    }
})