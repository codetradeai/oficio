// Links de checkout da assinatura Hotmart "Ofício Pro - Assinatura" (produto 8865228).
// Os href do HTML repetem estes endereços para quem navega sem JavaScript.
var CHECKOUTS = {
  mensal: "https://pay.hotmart.com/T108304780M?off=woxgckni",
  anual: "https://pay.hotmart.com/T108304780M?off=dztnzyb3"
};

(function () {
  document.querySelectorAll("a[data-checkout]").forEach(function (a) {
    var url = CHECKOUTS[a.getAttribute("data-checkout")];
    if (url) a.setAttribute("href", url);
  });
})();
