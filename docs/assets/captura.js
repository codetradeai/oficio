// Formulário opcional do guia (Brevo). O embed simples da Brevo não mostra mensagem,
// então enviamos por fetch (no-cors) e mostramos a nossa. Sem JavaScript, o POST normal continua funcionando.
(function () {
  var form = document.querySelector("form.captura");
  if (!form || !window.fetch || !window.FormData) return;
  var ok = form.querySelector(".captura-ok");

  function sucesso() {
    Array.prototype.forEach.call(form.children, function (el) { if (el !== ok) el.hidden = true; });
    ok.hidden = false;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var botao = form.querySelector("button[type=submit]");
    var isca = form.querySelector("[name=email_address_check]");
    if (isca && isca.value) { sucesso(); return; } // robô: não envia
    if (botao) { botao.disabled = true; botao.textContent = "Enviando…"; }
    fetch(form.action, { method: "POST", mode: "no-cors", body: new FormData(form) })
      .then(sucesso)
      .catch(function () {
        // Sem rede ou bloqueado: cai no envio normal (abre a página da Brevo em outra aba).
        if (botao) { botao.disabled = false; botao.textContent = "Quero o guia"; }
        HTMLFormElement.prototype.submit.call(form);
      });
  });
})();
