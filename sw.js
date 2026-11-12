// Dextra Sinistra · funciona sin conexión. Sube VERSION al publicar cambios.
const VERSION = "ds-v45";
const PAGES = {es: "index.html", en: "en.html"};
const ASSETS = ["manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png", "icons/favicon-32.png", "icons/maskable-512.png"];
const NET_WAIT = 3500; // ms: con wifi de avión o de tren que no responde, se abre la copia guardada

// Cloudflare redirige /index.html → / y /en.html → /en. Una respuesta «redirigida» no sirve para abrir
// una página, así que se guarda siempre una copia limpia, pidiendo las direcciones sin redirección.
const clean = r => r.redirected ? r.blob().then(b => new Response(b, {status: r.status, statusText: r.statusText, headers: r.headers})) : Promise.resolve(r);
const pageUrl = k => k === "en.html" ? "en" : "./";
const keyOf = url => /\/en(\.html)?$/.test(url.pathname) ? PAGES.en : PAGES.es;
const isHtml = r => r && r.ok && (r.headers.get("content-type") || "").includes("text/html");

async function savePage(c, key, r){ if(isHtml(r)) await c.put(key, await clean(r)); }

self.addEventListener("install", e => {
  e.waitUntil((async () => {
    const c = await caches.open(VERSION);
    await Promise.all(Object.values(PAGES).map(async k => {
      const r = await fetch(new Request(pageUrl(k), {cache: "reload"}));
      if(!isHtml(r)) throw new Error("page " + k);
      await savePage(c, k, r);
    }));
    await Promise.all(ASSETS.map(u => fetch(new Request(u, {cache: "reload"})).then(r => r.ok ? c.put(u, r) : null).catch(() => null)));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

async function cachedPage(key){
  const c = await caches.open(VERSION);
  let r = await c.match(key) || await c.match(key === PAGES.en ? PAGES.es : PAGES.en);
  if(!r){ for(const k of await caches.keys()){ r = await (await caches.open(k)).match(key); if(r) break; } }
  return r ? clean(r) : new Response("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width'><body style='font:16px system-ui;padding:40px;background:#ECEFF4;color:#2E3440'>Dextra Sinistra: abre la app una vez con conexión para poder usarla sin ella.", {headers: {"Content-Type": "text/html; charset=utf-8"}});
}

self.addEventListener("fetch", e => {
  const req = e.request;
  if(req.method !== "GET") return;
  const url = new URL(req.url);
  if(req.mode === "navigate"){
    // página: la red si contesta rápido (así se ven las versiones nuevas); si no hay red o tarda, la copia guardada
    const key = keyOf(url);
    const net = fetch(url.href, {cache: "no-store", credentials: "same-origin"});
    e.waitUntil(net.then(r => caches.open(VERSION).then(c => savePage(c, key, r.clone()))).catch(() => {}));
    e.respondWith(new Promise(resolve => {
      let done = false;
      const fallback = () => { if(!done){ done = true; cachedPage(key).then(resolve); } };
      const t = setTimeout(fallback, NET_WAIT);
      net.then(r => { if(done) return; if(!r.ok && r.status >= 500){ fallback(); return; } clearTimeout(t); done = true; clean(r).then(resolve); })
         .catch(() => { clearTimeout(t); fallback(); });
    }));
    return;
  }
  // resto (iconos, fuentes de Google): caché primero; sin red y sin copia, se responde vacío en vez de esperar
  e.respondWith(caches.match(req).then(hit => hit || Promise.race([
    fetch(req).then(r => {
      if(r.ok || r.type === "opaque"){ const cp = r.clone(); caches.open(VERSION).then(c => c.put(req, cp)); }
      return r;
    }),
    new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), url.origin === location.origin ? 15000 : NET_WAIT))
  ]).catch(() => new Response("", {status: 504}))));
});
