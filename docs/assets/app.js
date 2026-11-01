// Botões "Copiar": copia o texto do <pre> indicado em data-copiar.
(function () {
  function copiarTexto(texto) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(texto);
    }
    return new Promise(function (ok, falha) {
      var area = document.createElement("textarea");
      area.value = texto;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      try { document.execCommand("copy") ? ok() : falha(); } catch (e) { falha(e); }
      document.body.removeChild(area);
    });
  }
  document.querySelectorAll("button.copiar").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var alvo = document.getElementById(btn.getAttribute("data-copiar"));
      if (!alvo) return;
      var original = btn.textContent;
      copiarTexto(alvo.innerText.trim()).then(function () {
        btn.textContent = "Copiado ✓";
        btn.classList.add("feito");
      }, function () {
        btn.textContent = "Selecione e copie";
      }).then(function () {
        setTimeout(function () { btn.textContent = original; btn.classList.remove("feito"); }, 1800);
      });
    });
  });
})();
