// Links de checkout da assinatura Hotmart "Ofício Pro - Assinatura" (produto 8865228).
// Deixe vazio até o link existir e estar confirmado. Não apontar para o produto antigo 8863794.
// Enquanto vazio, o botão mantém o endereço do HTML e o marcador visível [LINK CHECKOUT MENSAL] ou [LINK CHECKOUT ANUAL].
var CHECKOUTS = {
  mensal: "",
  anual: ""
};

(function () {
  document.querySelectorAll("a[data-checkout]").forEach(function (a) {
    var url = CHECKOUTS[a.getAttribute("data-checkout")];
    if (url) a.setAttribute("href", url);
  });
})();
