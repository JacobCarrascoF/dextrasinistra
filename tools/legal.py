#!/usr/bin/env python3
"""Genera la página legal de dextrasinistra.com: aviso legal, privacidad, condiciones de uso y de venta de Plus.
Salida: legal.html (español) y legal-en.html (inglés). Uso: python3 legal.py <carpeta del repositorio>"""
import sys

REPO = sys.argv[1]
FONTS = open(REPO + "/tools/fontface.css").read()

CSS = FONTS + """
:root{--bg:#ECEFF4;--card:#F7F8FA;--line:#D8DEE9;--fg:#2E3440;--muted:#4C566A;--faint:#7A8599;--acc-d:#5E81AC;
--f-ui:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--f-mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme: dark){:root{--bg:#2E3440;--card:#353C4A;--line:#434C5E;--fg:#ECEFF4;--muted:#D8DEE9;--faint:#9AA5B8;--acc-d:#88C0D0;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16.5px/1.65 var(--f-ui);-webkit-font-smoothing:antialiased}
a{color:inherit}.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:14px;height:60px}
.brand{font-weight:600;text-decoration:none;display:flex;align-items:center;gap:9px;margin-right:auto;white-space:nowrap}.brand img{width:26px;height:26px;border-radius:7px}
.lang{font:500 13px var(--f-mono);text-decoration:none;color:var(--faint);border:1px solid var(--line);border-radius:999px;padding:5px 10px}
.btn{display:inline-block;text-decoration:none;font-weight:600;border-radius:999px;padding:9px 16px;background:var(--fg);color:var(--bg);font-size:15px;white-space:nowrap}
article{padding:32px 0 40px}
h1{font-size:clamp(30px,6vw,42px);line-height:1.12;letter-spacing:-.025em;margin:0 0 8px;font-weight:600}
h2{font-size:clamp(23px,4vw,28px);line-height:1.2;letter-spacing:-.02em;margin:48px 0 10px;font-weight:600;scroll-margin-top:76px}
h3{font-size:17px;margin:24px 0 4px;font-weight:600}
p{margin:0 0 12px}.upd{color:var(--faint);font-size:14px;margin-bottom:20px}
.toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 10px}.toc a{text-decoration:none;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:7px 14px;font-size:14.5px}
.data{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0 16px}
.data p{margin:0 0 4px}
ul{padding-left:22px}li{margin:6px 0}
footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--faint);font-size:14px}footer .wrap{display:flex;gap:16px;flex-wrap:wrap}footer a{text-decoration:none}
@media (max-width:520px){.top .wrap{gap:10px}}
"""

OWNER = "Jacob Carrasco Falcó"
NIF = "38098720W"
ADDR_ES = "C/ Jaume Balmes, 4, 3.º 1.ª, 08830 Sant Boi de Llobregat (Barcelona), España"
ADDR_EN = "C/ Jaume Balmes, 4, 3.º 1.ª, 08830 Sant Boi de Llobregat (Barcelona), Spain"
MAIL = "jcfabricalenta@gmail.com"

ES = f"""
<h1>Aviso legal, privacidad y condiciones</h1>
<p class="upd">Última actualización: 26 de noviembre de 2026.</p>
<nav class="toc" aria-label="Apartados"><a href="#aviso">Aviso legal</a><a href="#privacidad">Privacidad</a><a href="#uso">Condiciones de uso</a><a href="#condiciones">Condiciones de venta de Plus</a></nav>

<h2 id="aviso">Aviso legal</h2>
<div class="data"><p><b>Titular:</b> {OWNER}</p><p><b>NIF:</b> {NIF}</p><p><b>Domicilio:</b> {ADDR_ES}</p><p><b>Correo de contacto:</b> <a href="mailto:{MAIL}">{MAIL}</a></p><p><b>Sitio web:</b> dextrasinistra.com</p></div>
<p>Este sitio ofrece Dextra Sinistra, una aplicación web de ejercicios de técnica de guitarra para la mano derecha, la mano izquierda y las dos a la vez, con tablatura, metrónomo, reloj y registro de la práctica. Su uso es gratuito. Algunas funciones forman parte de Dextra Sinistra Plus, que se adquiere de pago según las condiciones de venta de esta página.</p>
<h3>Propiedad intelectual</h3>
<p>Dextra Sinistra, sus ejercicios, textos, tablaturas, numeración, diseño, código y logotipo pertenecen a su titular. Se permite su uso personal dentro de la aplicación. No está permitido copiarlos, distribuirlos ni reutilizarlos en otros productos sin autorización. Las tipografías Instrument Sans y JetBrains Mono se usan bajo la licencia SIL Open Font License 1.1.</p>
<h3>Responsabilidad y copias de seguridad</h3>
<p>Tu práctica se guarda únicamente en tu dispositivo, así que no podemos recuperarla si se pierde, por ejemplo al borrar los datos del navegador, desinstalar la aplicación o cambiar de teléfono. Usa «Exportar copia» en Ajustes con regularidad. Trabajamos para que la aplicación funcione correctamente, pero no podemos garantizar que esté libre de errores ni disponible en todo momento.</p>
<h3>Ley aplicable</h3>
<p>Este sitio se rige por la legislación española.</p>

<h2 id="privacidad">Política de privacidad</h2>
<p><b>Responsable del tratamiento:</b> {OWNER}, NIF {NIF}, {ADDR_ES}. Contacto: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h3>Lo más importante</h3>
<p>Dextra Sinistra está diseñada para no recoger tus datos. No hay cuentas de usuario, ni servidores que guarden tu práctica, ni publicidad, ni herramientas de analítica o seguimiento dentro de la app. Solo la portada y las guías de dextrasinistra.com cuentan las visitas con GoatCounter, sin cookies y sin guardar datos personales ni tu dirección IP, para saber cuánta gente llega y desde qué web.</p>
<h3>Almacenamiento en tu dispositivo</h3>
<p>Tus sesiones, notas, planes, récords, nombre y objetivo semanal se guardan en el almacenamiento interno del navegador o de la app. Es técnicamente necesario para el servicio que pides, no se usa para seguirte ni se comparte con nadie, y puedes borrarlo en cualquier momento desde los ajustes del navegador. No se usan cookies de publicidad ni de análisis.</p>
<h3>Datos que sí tratamos, y solo si tú los facilitas</h3>
<ul>
<li><b>Si compras Dextra Sinistra Plus:</b> la venta se realiza en la plataforma Payhip y el pago lo procesa Stripe (o PayPal, si lo eliges). Recibimos tu nombre, tu correo y los datos del pedido, nunca los de tu tarjeta. Los usamos para entregarte el código, emitir la factura, cumplir las obligaciones fiscales y atenderte si nos escribes. La base legal es la ejecución del contrato de compra y el cumplimiento de obligaciones legales.</li>
<li><b>Si nos escribes por correo o por redes sociales:</b> usamos tus datos solo para responderte.</li>
<li><b>Al visitar la web:</b> el alojamiento (Cloudflare) puede registrar datos técnicos, como la dirección IP, por seguridad y funcionamiento. No los usamos para identificarte. Las tipografías se sirven desde la propia web, sin conectar con Google Fonts.</li>
</ul>
<h3>Con quién se comparten</h3>
<p>Solo con los servicios necesarios para lo anterior: Payhip, Stripe y PayPal para los pagos, Cloudflare para el alojamiento, GoatCounter para el recuento anónimo de visitas y nuestra gestoría para la contabilidad. Algunos pueden tratar datos fuera del Espacio Económico Europeo, con las garantías que exige la normativa de protección de datos. No vendemos ni cedemos tus datos a nadie más.</p>
<h3>Cuánto tiempo los guardamos</h3>
<p>Los datos de las compras, durante los plazos que exige la normativa fiscal y mercantil. Los mensajes que nos envías, el tiempo necesario para atenderte.</p>
<h3>Menores</h3>
<p>La aplicación no recoge datos personales de nadie, tampoco de menores.</p>
<h3>Tus derechos</h3>
<p>Puedes pedir el acceso, la rectificación o la supresión de tus datos, oponerte a su tratamiento, limitarlo o solicitar su portabilidad escribiendo a <a href="mailto:{MAIL}">{MAIL}</a>. Los datos de tu práctica puedes consultarlos, exportarlos y borrarlos tú mismo desde Ajustes. Si consideras que no hemos atendido bien tu petición, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>

<h2 id="uso">Condiciones de uso</h2>
<p>La aplicación se ofrece para el estudio personal de la guitarra. Su contenido es orientativo y no sustituye a un profesor.</p>
<p><b>Salud.</b> Practica sin dolor. Si notas dolor, hormigueo, pérdida de control de un dedo o tensión que no desaparece al parar, deja de practicar y consulta a un profesional sanitario. Haz pausas y calienta antes de trabajar tempos altos.</p>
<p>Al usar Dextra Sinistra te comprometes a hacerlo de forma lícita y a no intentar dañar su funcionamiento.</p>

<h2 id="condiciones">Condiciones de venta de Dextra Sinistra Plus</h2>
<h3>Quién vende</h3>
<p>{OWNER}, con los datos indicados en el aviso legal. La compra se realiza a través de la plataforma Payhip.</p>
<h3>Qué compras</h3>
<p>Dextra Sinistra Plus es un código personal que desbloquea en la aplicación todos los ejercicios de los niveles I a V de Dextra, Sinistra y Ambas, Tabula completa, los planes guiados y el plan personalizado. Es contenido digital, no un producto físico.</p>
<h3>Precio y modalidades</h3>
<p>Plus anual, 19,99 €, y Plus para siempre, 49,99 €, con el IVA incluido. El precio final y la modalidad se indican antes de pagar. Plus no se renueva de forma automática: no hacemos cobros periódicos sin tu acción. El plan anual dura un año a partir del día en que activas el código; si lo renuevas antes de que termine, el año nuevo se suma al tiempo que te queda.</p>
<h3>Prueba gratuita</h3>
<p>Al empezar a usar la aplicación tienes 14 días de Plus gratis, sin compromiso y sin dar ningún dato. Al terminar conservas todo tu progreso y los ejercicios gratuitos.</p>
<h3>Entrega y activación</h3>
<p>Al completar el pago recibirás el código por correo. Para activarlo, pégalo en Ajustes → Plus. La activación se hace en tu dispositivo, sin conexión a ningún servidor. Guarda tu código: lo necesitarás para activar Plus en otro dispositivo, porque no se incluye en la copia de seguridad.</p>
<h3>Uso del código</h3>
<p>El código es personal. Puedes usarlo en todos tus dispositivos, pero no está permitido compartirlo, publicarlo ni revenderlo.</p>
<h3>Si eliges el plan anual</h3>
<p>Cuando termine, conservarás todo lo que hayas registrado y seguirás pudiendo verlo. Solo dejarás de tener acceso a las funciones de Plus hasta que lo renueves.</p>
<h3>Derecho de desistimiento</h3>
<p>Como consumidor, dispones en general de 14 días naturales para desistir de una compra a distancia. Sin embargo, Dextra Sinistra Plus es contenido digital que se entrega de forma inmediata. Al comprarlo, das tu consentimiento expreso para recibirlo al momento y reconoces que, una vez recibido el código, pierdes el derecho de desistimiento, conforme al artículo 103 m) del Real Decreto Legislativo 1/2007. Aun así, si tienes cualquier problema con tu compra, escríbenos y buscaremos una solución.</p>
<h3>Funcionamiento</h3>
<p>Dextra Sinistra es una aplicación web que funciona en navegadores actuales. Si una función de Plus deja de funcionar por una causa que dependa de nosotros, lo solucionaremos o te ofreceremos una alternativa.</p>
<h3>Cambios</h3>
<p>Podemos mejorar o modificar los ejercicios y las funciones de la aplicación. Si un cambio afectara de forma importante a lo que compraste, te lo comunicaremos.</p>
<h3>Ley y tribunales</h3>
<p>Estas condiciones se rigen por la legislación española. Si eres consumidor, puedes acudir a los tribunales de tu domicilio.</p>
<p>¿Dudas? Escríbenos a <a href="mailto:{MAIL}">{MAIL}</a>.</p>
"""

EN = f"""
<h1>Legal notice, privacy and terms</h1>
<p class="upd">Last updated: November 26, 2026.</p>
<nav class="toc" aria-label="Sections"><a href="#notice">Legal notice</a><a href="#privacy">Privacy</a><a href="#use">Terms of use</a><a href="#terms">Plus terms of sale</a></nav>

<h2 id="notice">Legal notice</h2>
<div class="data"><p><b>Owner:</b> {OWNER}</p><p><b>Tax ID (NIF):</b> {NIF}</p><p><b>Address:</b> {ADDR_EN}</p><p><b>Contact email:</b> <a href="mailto:{MAIL}">{MAIL}</a></p><p><b>Website:</b> dextrasinistra.com</p></div>
<p>This site offers Dextra Sinistra, a web app of guitar technique exercises for the picking hand, the fretting hand and both together, with tab, metronome, timer and a practice log. It is free to use. Some features are part of Dextra Sinistra Plus, which is purchased under the terms of sale on this page.</p>
<h3>Intellectual property</h3>
<p>Dextra Sinistra, its exercises, texts, tabs, numbering, design, code and logo belong to its owner. Personal use within the app is permitted. Copying, distributing or reusing them in other products without permission is not allowed. The Instrument Sans and JetBrains Mono typefaces are used under the SIL Open Font License 1.1.</p>
<h3>Liability and backups</h3>
<p>Your practice is stored only on your device, so we cannot recover it if it is lost, for example when you clear your browser data, uninstall the app or change phones. Use “Export backup” in Settings regularly. We work to keep the app running properly, but we cannot guarantee that it is error-free or always available.</p>
<h3>Applicable law</h3>
<p>This site is governed by Spanish law.</p>

<h2 id="privacy">Privacy policy</h2>
<p><b>Data controller:</b> {OWNER}, Tax ID {NIF}, {ADDR_EN}. Contact: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h3>The most important part</h3>
<p>Dextra Sinistra is designed not to collect your data. There are no user accounts, no servers storing your practice, no ads and no analytics or tracking inside the app. Only the home page and the guides on dextrasinistra.com count visits with GoatCounter, without cookies and without storing personal data or your IP address, to know how many people arrive and from which website.</p>
<h3>Storage on your device</h3>
<p>Your sessions, notes, plans, records, name and weekly goal are kept in the browser’s or the app’s internal storage. This is technically necessary for the service you ask for, is not used to track you, is not shared with anyone, and you can delete it at any time from your browser settings. No advertising or analytics cookies are used.</p>
<h3>Data we do process, only if you provide it</h3>
<ul>
<li><b>If you buy Dextra Sinistra Plus:</b> the sale takes place on the Payhip platform and the payment is processed by Stripe (or PayPal, if you choose it). We receive your name, your email and the order details, never your card details. We use them to deliver your code, issue the invoice, meet our tax obligations and help you if you write to us. The legal basis is the performance of the purchase contract and compliance with legal obligations.</li>
<li><b>If you write to us by email or on social media:</b> we use your data only to reply.</li>
<li><b>When you visit the website:</b> the host (Cloudflare) may log technical data, such as your IP address, for security and operation. We do not use it to identify you. The fonts are served from our own website, without connecting to Google Fonts.</li>
</ul>
<h3>Who we share it with</h3>
<p>Only the services needed for the above: Payhip, Stripe and PayPal for payments, Cloudflare for hosting, GoatCounter for the anonymous visit count and our accountants. Some may process data outside the European Economic Area, with the safeguards required by data protection law. We do not sell or pass on your data to anyone else.</p>
<h3>How long we keep it</h3>
<p>Purchase data, for the periods required by tax and commercial law. Messages you send us, for as long as needed to help you.</p>
<h3>Children</h3>
<p>The app does not collect personal data from anyone, including children.</p>
<h3>Your rights</h3>
<p>You can request access to, rectification or erasure of your data, object to or restrict its processing, or ask for its portability by writing to <a href="mailto:{MAIL}">{MAIL}</a>. You can view, export and delete your practice data yourself from Settings. If you feel we have not handled your request properly, you can complain to the Spanish Data Protection Agency (aepd.es).</p>

<h2 id="use">Terms of use</h2>
<p>The app is offered for personal guitar study. Its content is for guidance and does not replace a teacher.</p>
<p><b>Health.</b> Practice without pain. If you feel pain, tingling, loss of control of a finger or tension that does not go away when you stop, stop practicing and see a healthcare professional. Take breaks and warm up before working at high tempos.</p>
<p>By using Dextra Sinistra you agree to use it lawfully and not to try to harm its operation.</p>

<h2 id="terms">Dextra Sinistra Plus terms of sale</h2>
<h3>Who sells</h3>
<p>{OWNER}, with the details given in the legal notice. The purchase is made through the Payhip platform.</p>
<h3>What you buy</h3>
<p>Dextra Sinistra Plus is a personal code that unlocks in the app every exercise from levels I to V in Dextra, Sinistra and Both, the full Tabula, the guided plans and the custom plan. It is digital content, not a physical product.</p>
<h3>Price and plans</h3>
<p>Plus yearly, €19.99, and Plus forever, €49.99, VAT included. The final price and the plan are shown before you pay. Plus does not renew automatically: we never charge you periodically without your action. The yearly plan lasts one year from the day you activate the code; if you renew before it ends, the new year is added to the time you have left.</p>
<h3>Free trial</h3>
<p>When you start using the app you get 14 days of Plus for free, with no commitment and without giving any data. When it ends you keep all your progress and the free exercises.</p>
<h3>Delivery and activation</h3>
<p>When the payment is complete you will receive the code by email. To activate it, paste it in Settings → Plus. Activation happens on your device, without connecting to any server. Keep your code: you will need it to activate Plus on another device, because it is not included in the backup.</p>
<h3>Use of the code</h3>
<p>The code is personal. You can use it on all your devices, but you may not share, publish or resell it.</p>
<h3>If you choose the yearly plan</h3>
<p>When it ends, you will keep everything you have logged and can still see it. You will only lose access to the Plus features until you renew.</p>
<h3>Right of withdrawal</h3>
<p>As a consumer, you generally have 14 calendar days to withdraw from a distance purchase. However, Dextra Sinistra Plus is digital content delivered immediately. By buying it, you expressly consent to receive it at once and acknowledge that, once the code has been delivered, you lose the right of withdrawal, under Article 103(m) of Spanish Royal Legislative Decree 1/2007. Even so, if you have any problem with your purchase, write to us and we will find a solution.</p>
<h3>Operation</h3>
<p>Dextra Sinistra is a web app that works in current browsers. If a Plus feature stops working for a reason within our control, we will fix it or offer you an alternative.</p>
<h3>Changes</h3>
<p>We may improve or change the app’s exercises and features. If a change significantly affected what you bought, we would let you know.</p>
<h3>Law and courts</h3>
<p>These terms are governed by Spanish law. If you are a consumer, you may go to the courts of your place of residence.</p>
<p>Questions? Write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
"""

PAGES = {
  "es": dict(file="legal.html", url="https://dextrasinistra.com/legal", alt="https://dextrasinistra.com/legal-en", title="Aviso legal, privacidad y condiciones · Dextra Sinistra",
             desc="Aviso legal, política de privacidad y condiciones de uso y de venta de Dextra Sinistra Plus.", home="/", app="/app/", open="Abrir la app",
             other_href="/legal-en", other="EN", body=ES, rights="© 2026 Jacob Carrasco", back="Inicio"),
  "en": dict(file="legal-en.html", url="https://dextrasinistra.com/legal-en", alt="https://dextrasinistra.com/legal", title="Legal notice, privacy and terms · Dextra Sinistra",
             desc="Legal notice, privacy policy, terms of use and terms of sale of Dextra Sinistra Plus.", home="/en", app="/app/en", open="Open the app",
             other_href="/legal", other="ES", body=EN, rights="© 2026 Jacob Carrasco", back="Home"),
}

for code, p in PAGES.items():
    other = "en" if code == "es" else "es"
    page = f"""<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title><meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{p["url"]}"><link rel="alternate" hreflang="{code}" href="{p["url"]}"><link rel="alternate" hreflang="{other}" href="{p["alt"]}">
<meta name="theme-color" content="#ECEFF4" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#2E3440" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/icons/icon.svg" type="image/svg+xml"><link rel="icon" href="/icons/favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="preload" href="/fonts/sans-400.woff" as="font" type="font/woff" crossorigin>
<style>{CSS}</style>
</head><body>
<header class="top"><div class="wrap"><a class="brand" href="{p["home"]}"><img src="/icons/icon.svg" alt="" width="26" height="26">Dextra Sinistra</a><a class="lang" href="{p["other_href"]}" hreflang="{other}" lang="{other}">{p["other"]}</a><a class="btn" href="{p["app"]}">{p["open"]}</a></div></header>
<main class="wrap"><article>{p["body"]}</article></main>
<footer><div class="wrap"><span>{p["rights"]}</span><a href="{p["home"]}">{p["back"]}</a><a href="{p["app"]}">{p["open"]}</a></div></footer>
</body></html>
"""
    open(f"{REPO}/{p['file']}", "w").write(page)
print("ok")
