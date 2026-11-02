// Consentimento LGPD + medição (GA4 e Pixel da Meta).
// Nada é carregado antes de "Aceitar". A escolha fica no localStorage deste navegador.
// Compra e início de checkout são medidos pela Hotmart (não disparamos aqui, para não contar duas vezes).
(function () {
  var GA4_ID = "G-T3DHD1B451";
  var META_PIXEL_ID = "1150210904353081";
  var CHAVE = "oficio-consentimento"; // "aceito" | "recusado"

  function ler() { try { return localStorage.getItem(CHAVE); } catch (e) { return null; } }
  function gravar(v) { try { localStorage.setItem(CHAVE, v); } catch (e) {} }

  var ativo = false;

  function carregarGA4() {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("consent", "default", { ad_storage: "granted", analytics_storage: "granted", ad_user_data: "granted", ad_personalization: "granted" });
    window.gtag("js", new Date());
    window.gtag("config", GA4_ID, { anonymize_ip: true });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);
  }

  function carregarPixel() {
    /* código base do Pixel da Meta (oficial), carregado só após o aceite */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("consent", "grant");
    window.fbq("init", META_PIXEL_ID);
    window.fbq("track", "PageView");
  }

  function ativar() {
    if (ativo) return;
    ativo = true;
    carregarGA4();
    carregarPixel();
  }

  // Eventos: sem dados pessoais (nada de e-mail ou nome).
  var EVENTOS = {
    download_zip:        { ga: "file_download",       gaParams: { file_name: "oficio.zip" }, meta: ["trackCustom", "DownloadOficio"] },
    cadastro_guia:       { ga: "generate_lead",       gaParams: { lead_source: "guia_primeiros_passos" }, meta: ["track", "Lead"] },
    clique_comprar_pro:  { ga: "clique_comprar_pro",  gaParams: {}, meta: ["trackCustom", "CliqueComprarPro"] },
    clique_conhecer_pro: { ga: "clique_conhecer_pro", gaParams: {}, meta: ["trackCustom", "CliqueConhecerPro"] }
  };

  function medir(nome, extra) {
    if (!ativo || !EVENTOS[nome]) return;
    var ev = EVENTOS[nome], p = {};
    for (var k in ev.gaParams) p[k] = ev.gaParams[k];
    for (var j in (extra || {})) p[j] = extra[j];
    p.transport_type = "beacon";
    try { window.gtag("event", ev.ga, p); } catch (e) {}
    try { window.fbq(ev.meta[0], ev.meta[1]); } catch (e) {}
  }
  window.oficioMedir = medir;

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("[data-evento]") : null;
    if (a && a.tagName !== "FORM") medir(a.getAttribute("data-evento"), { link_text: (a.textContent || "").trim().slice(0, 40) });
  });
  document.addEventListener("submit", function (e) {
    var f = e.target;
    if (f && f.getAttribute && f.getAttribute("data-evento")) medir(f.getAttribute("data-evento"));
  });

  // Banner
  function apagarCookiesDeMedicao() {
    document.cookie.split(";").forEach(function (c) {
      var nome = c.split("=")[0].trim();
      if (/^(_ga|_gid|_gat|_fbp|_fbc)/.test(nome)) {
        var dominios = ["", location.hostname, "." + location.hostname.split(".").slice(-2).join(".")];
        dominios.forEach(function (d) {
          document.cookie = nome + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + (d ? "; domain=" + d : "");
        });
      }
    });
  }

  function mostrarBanner() {
    if (document.getElementById("consentimento")) return;
    var raiz = document.querySelector("script[src*='consent.js']").getAttribute("src").replace(/assets\/consent\.js.*$/, "");
    var div = document.createElement("div");
    div.id = "consentimento";
    div.className = "consentimento";
    div.setAttribute("role", "dialog");
    div.setAttribute("aria-live", "polite");
    div.setAttribute("aria-label", "Preferência de cookies");
    div.innerHTML =
      '<p><b>Cookies de medição?</b> Com seu aceite, usamos Google Analytics e o pixel da Meta para saber quantas pessoas visitam, baixam e clicam. ' +
      'Sem aceite, nada disso carrega. <a href="' + raiz + 'privacidade.html">Aviso de privacidade</a></p>' +
      '<div class="consentimento-botoes">' +
      '<button type="button" class="btn consentimento-recusar">Recusar</button>' +
      '<button type="button" class="btn btn-pri consentimento-aceitar">Aceitar</button></div>';
    document.body.appendChild(div);
    div.querySelector(".consentimento-aceitar").addEventListener("click", function () {
      gravar("aceito"); div.remove(); ativar();
    });
    div.querySelector(".consentimento-recusar").addEventListener("click", function () {
      var tinhaAceito = ativo;
      gravar("recusado"); div.remove(); apagarCookiesDeMedicao();
      if (tinhaAceito) location.reload(); // descarrega os scripts já ativos
    });
  }

  // Link "Preferências de cookies" (rodapé) reabre o banner.
  document.addEventListener("click", function (e) {
    var l = e.target.closest ? e.target.closest("[data-preferencias-cookies]") : null;
    if (l) { e.preventDefault(); mostrarBanner(); }
  });

  function iniciar() {
    var v = ler();
    if (v === "aceito") ativar();
    else if (v !== "recusado") mostrarBanner();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
