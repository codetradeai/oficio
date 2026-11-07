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

// Primeiro play de cada vídeo, só se a medição já foi aceita. Sem e-mail, só o nome do vídeo.
(function () {
  document.querySelectorAll("video[data-video]").forEach(function (video) {
    video.addEventListener("play", function () {
      if (video.getAttribute("data-medido") === "1") return;
      var aceito = false;
      try { aceito = localStorage.getItem("oficio-consentimento") === "aceito"; } catch (e) {}
      if (!aceito || !window.oficioMedir) return;
      video.setAttribute("data-medido", "1");
      window.oficioMedir("video_play", { video_name: video.getAttribute("data-video") });
    });
  });
})();
