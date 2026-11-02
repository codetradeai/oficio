// Link do checkout da Hotmart. Todos os botões "Comprar" usam este valor (os href em pro/index.html repetem o link para quem navega sem JavaScript).
var HOTMART_CHECKOUT = "https://pay.hotmart.com/O108302530U?sck=site-pro";

(function () {
  document.querySelectorAll("a[data-checkout]").forEach(function (a) {
    a.setAttribute("href", HOTMART_CHECKOUT);
  });
})();
