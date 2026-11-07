// Formulário opcional do guia. Envia JSON para o servidor do Ofício, sem cookies.
// O aceite deste formulário é só para e-mails. A medição só dispara no sucesso,
// e só se a pessoa já aceitou os cookies. O e-mail não entra no evento.
(function () {
  var URL_GUIA = "https://pro.codetrade.me/guia/inscrever";
  var MENSAGEM_OK = "Se o endereço puder receber o guia, enviaremos um link para confirmar. Confira também o spam.";
  var form = document.querySelector("form.captura");
  if (!form || !window.fetch) return;

  var email = document.getElementById("captura-email");
  var aceite = document.getElementById("captura-consentimento");
  var website = document.getElementById("captura-website");
  var msg = document.getElementById("captura-msg");
  var botao = form.querySelector("button[type=submit]");
  var campos = form.querySelector(".captura-campos");
  var textoBotao = botao ? botao.textContent : "Quero o guia";
  var enviando = false;

  function mostrar(tipo, texto) {
    if (!msg) return;
    msg.className = "captura-msg " + tipo;
    msg.textContent = texto;
  }

  function minutos(segundos) {
    var n = Number(segundos);
    if (!n || n < 60) return "alguns minutos";
    var m = Math.max(1, Math.round(n / 60));
    return m + (m === 1 ? " minuto" : " minutos");
  }

  function textoErro(status, retryAfter) {
    if (status === 400) return "Confira o e-mail e marque o aceite para receber o guia.";
    if (status === 403) return "Não consegui enviar a partir desta página. Abra o site do Ofício e tente de novo.";
    if (status === 413) return "Esse pedido ficou grande demais. Use só o e-mail e tente de novo.";
    if (status === 429) return "Muitas tentativas seguidas. Espere " + minutos(retryAfter) + " e tente de novo.";
    if (status === 503) return "O envio do guia está pausado agora. Tente de novo mais tarde.";
    return "Não consegui enviar agora. Tente de novo em instantes.";
  }

  function travar(ligado) {
    enviando = ligado;
    form.setAttribute("aria-busy", ligado ? "true" : "false");
    if (!botao) return;
    botao.disabled = ligado;
    botao.textContent = ligado ? "Enviando…" : textoBotao;
  }

  function sucesso(texto) {
    mostrar("ok", texto || MENSAGEM_OK);
    enviando = true;
    form.setAttribute("aria-busy", "false");
    if (campos) campos.hidden = true;
    if (botao) botao.disabled = true;
    if (msg) msg.focus();
  }

  function falha(texto) {
    mostrar("erro", texto);
    travar(false);
    if (msg) msg.focus();
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (enviando) return;
    if (typeof form.reportValidity === "function" && !form.checkValidity()) {
      form.reportValidity();
      return;
    }
    var endereco = email ? email.value.trim() : "";
    if (email) email.setAttribute("aria-invalid", "false");
    if (!aceite || !aceite.checked) {
      falha("Marque o aceite para receber o guia e os e-mails do Ofício.");
      return;
    }
    if (!endereco || endereco.length > 254 || endereco.indexOf("@") < 1) {
      if (email) email.setAttribute("aria-invalid", "true");
      falha("Confira o e-mail e marque o aceite para receber o guia.");
      return;
    }
    // Isca preenchida: não chama o servidor e não mede. A resposta é a mesma do sucesso.
    if (website && website.value) {
      sucesso(MENSAGEM_OK);
      return;
    }

    travar(true);
    mostrar("", "");
    fetch(URL_GUIA, {
      method: "POST",
      credentials: "omit",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify({
        email: endereco,
        consentimento: true,
        website: ""
      })
    }).then(function (resposta) {
      if (resposta.status === 202) {
        return resposta.json().catch(function () { return {}; }).then(function (corpo) {
          sucesso(corpo && corpo.mensagem ? corpo.mensagem : MENSAGEM_OK);
          if (window.oficioMedir) window.oficioMedir("cadastro_guia");
        });
      }
      if (resposta.status === 400 && email) email.setAttribute("aria-invalid", "true");
      falha(textoErro(resposta.status, resposta.headers.get("Retry-After")));
    }).catch(function () {
      falha("Não consegui enviar agora. Confira a internet e tente de novo.");
    });
  });
})();
