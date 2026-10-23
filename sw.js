// Dextra Sinistra · funciona sin conexión. Sube VERSION al publicar cambios.
const VERSION = "ds-v27";
const CORE = ["./", "index.html", "en.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png", "icons/favicon-32.png"];
self.addEventListener("install", e => {
  // cache:"reload" salta la caché HTTP del navegador (GitHub Pages guarda 10 minutos)
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE.map(u => new Request(u, {cache: "reload"})))).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  if(e.request.method !== "GET") return;
  const url = new URL(e.request.url);
  if(e.request.mode === "navigate"){
    // página: siempre a la red sin caché; si no hay conexión, la copia guardada de esa misma página
    const key = /\/en(\.html)?$/.test(url.pathname) ? "en.html" : "index.html";
    e.respondWith(fetch(url.href, {cache: "no-store", credentials: "same-origin"})
      .then(r => { if(r.ok){ const cp = r.clone(); caches.open(VERSION).then(c => c.put(key, cp)); } return r; })
      .catch(() => caches.match(key)));
    return;
  }
  // resto (iconos, fuentes de Google): caché primero
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
    if(r.ok || r.type === "opaque"){ const cp = r.clone(); caches.open(VERSION).then(c => c.put(e.request, cp)); }
    return r;
  })));
});
