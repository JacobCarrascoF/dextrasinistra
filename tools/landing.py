#!/usr/bin/env python3
"""Genera la portada de dextrasinistra.com en español (index.html) y en inglés (en.html).
Uso: python3 landing.py <carpeta del repositorio>"""
import sys, html, json

REPO = sys.argv[1]
FONTS = open(REPO + "/tools/fontface.css").read()
COUNTER = open(REPO + "/tools/counter.html").read()
PAY_YEAR = "https://payhip.com/b/zntXF"
PAY_LIFE = "https://payhip.com/b/N3Hnp"
MAIL = "jcfabricalenta@gmail.com"

T = {
"es": dict(
  lang="es", other="en", other_href="/en", other_label="English", app="/app/", img="es",
  title="Dextra Sinistra · técnica de guitarra para las dos manos",
  desc="9.817 ejercicios de guitarra para la mano derecha, la izquierda y las dos a la vez, con tablatura, metrónomo, reloj, registro y planes guiados. Sin cuenta y sin conexión.",
  nav=[("#ejercicios","Ejercicios"),("#metodo","Método"),("#como-funciona","Cómo funciona"),("#precios","Precios"),("#preguntas","Preguntas")],
  open_app="Abrir la app",
  back_bar="Tienes tu práctica guardada en este dispositivo.", back_cta="Seguir en la app →",
  eyebrow="App de técnica para guitarristas",
  h1="Entrena cada mano por separado.<br>Y luego, las dos juntas.",
  lead="Dextra Sinistra reúne 9.817 ejercicios de guitarra con tablatura, metrónomo, reloj y registro de cada pasada. Abres la app y sabes qué tocar hoy, cuánto tiempo y a qué tempo.",
  cta1="Empezar gratis", cta2="Cómo funciona",
  note="Sin cuenta · funciona sin conexión · 14 días de Plus incluidos",
  stats=[("2.715","Dextra","mano derecha"),("3.087","Sinistra","mano izquierda"),("4.015","Ambas","las dos a la vez"),("4","planes guiados","de 8 a 12 semanas")],
  sec_hands="Tres secciones, una guitarra",
  sec_hands_p="Cada ejercicio tiene su código, su nivel del I al V, su rango de tempo y un consejo de por qué está ahí.",
  hands=[
    ("d","Dextra","La mano que pulsa","Alternate, hybrid, sweep y economy, rasgado y rítmica, escalas y arpegios, enclosures y voicings. Con púa, con dedos (p i m a) y en híbrido."),
    ("s","Sinistra","La mano que pisa","Independencia, legato, extensiones y cambios de posición, bends y vibrato, acordes y cejilla, apagado. También escalas, arpegios, enclosures y voicings."),
    ("a","Ambas","Las dos en sincronía","Mapas del mástil, enclosures y voicings con púa y dedo a la vez. Y Tabula, el reto de intervalos 11 × 11."),
  ],
  shared="Muchos ejercicios existen en las tres secciones con el mismo número: primero la derecha sola (D-1204), luego la izquierda sola (S-1204) y al final las dos juntas (A-1204). Misma música, cada mano a su tiempo.",
  sec_method="Un método, no una lista de ejercicios",
  sec_method_p="Practicar mucho no es lo mismo que practicar bien. La app decide el orden, el tiempo y el tempo para que tú solo tengas que tocar.",
  method=[
    ("Planes por ciclos","Cada semana entra un ejercicio núcleo y se queda tres: dos subiendo tempo y una de masterización al 90 % de tu récord, con un test el último día. Si lo superas, sale del plan; si no, se queda una semana más."),
    ("Las 4 reglas de una pasada limpia","Todo el ejercicio, de principio a fin. Completo, sin dejarse nada. Que suene bien. A tempo. Solo las pasadas limpias cuentan para tu récord."),
    ("El tempo se ajusta solo","Limpio: la próxima vez, 4 BPM más. Controlado: mantienes. Con tensión: bajas un 10 %. No tienes que adivinar a qué velocidad trabajar."),
    ("Tu tiempo real, no el ideal","Cada día del plan en versión completa o en un Snack corto. Lo que no termines se guarda y lo retomas otro día, en este dispositivo o en otro."),
  ],
  plans_t="Los planes",
  plans=[("Inicial","8 semanas · 25 min"),("Intermedio","10 semanas · 40 min"),("Avanzado","12 semanas · 60 min"),("Experto","12 semanas · 60 min")],
  plans_note="5 días por semana. Cada día trabaja las dos manos: el ejercicio de Dextra, su pareja de Sinistra y un bloque de Ambas al final. O crea tu plan personalizado: eliges días, minutos por sesión, semanas, nivel y qué quieres trabajar.",
  extras=[("Calentamiento","5 minutos antes de tocar en directo o 10 para empezar a estudiar."),("Reto de velocidad","Un ejercicio por semana: escalera de +3 % cada 4 compases, botón de tensión y ráfagas al +10 %."),("Formato profesional","La mitad de ejercicios y el doble de tiempo en cada uno.")],
  sec_how="Cómo funciona",
  sec_how_p="Cinco pantallas y ninguna configuración. Esto es un día normal con la app.",
  steps=[
    ("home","Abre Inicio y decide con un toque","Tu plan de hoy aparece arriba: elige la sesión completa o un Snack según el tiempo que tengas. Debajo, el calentamiento, el reto de la semana y la práctica libre con tu último ejercicio."),
    ("practice_voi","Toca con la tablatura delante","Tablatura, metrónomo y reloj en una sola pantalla, con una barra que recorre la tablatura mientras tocas. Mantén pulsado − o + para cambiar el tempo deprisa, pulsa Escuchar para oír el patrón y gira el móvil para verla en grande. En los voicings ves el acorde y sus trastes."),
    ("log","Di cómo ha salido","Cuando acaba el tiempo marcas Con tensión, Controlado o Limpio. Para que cuente como Limpio, las cuatro reglas. La app calcula el tempo de la próxima vez."),
    ("plan","Sigue el plan día a día","Cada día tiene su sesión. Al terminar el último ejercicio eliges seguir con el día siguiente o dejarlo por hoy, y puedes llevar varios planes a la vez."),
    ("progress","Mira cómo avanzas","Minutos por día y por mano, racha, pasadas limpias y el camino de cada ejercicio hacia su tempo objetivo. Y puedes compartir tu semana."),
  ],
  tabula_t="Tabula: 121 piezas de intervalos",
  tabula_p="Cada pieza combina un intervalo construido sobre la raíz con la distancia entre raíces, en 6 variantes: 726 ejercicios para las dos manos. Una pieza está completa cuando sus 6 variantes salen limpias a 100 BPM o más.",
  tabula_credit="Inspirado en la Interval Matrix de Jonathan Kreisberg.",
  install_t="Instálala como una app",
  install=[("iPhone y iPad","Ábrela en Safari, pulsa Compartir y después «Añadir a pantalla de inicio»."),("Android","En Chrome, menú ⋮ y «Instalar aplicación»."),("Ordenador","En Chrome o Edge, el icono de instalar de la barra de direcciones.")],
  install_note="Se abre a pantalla completa, como cualquier app, y funciona sin conexión.",
  sec_price="Precios",
  sec_price_p="Al abrir la app tienes 14 días de Plus completo. Cuando terminan, conservas los ejercicios gratis y todo tu progreso.",
  free=("Gratis","0 €","para siempre",["153 ejercicios: los 87 de nivel I de Dextra y Sinistra y la primera fila de Tabula","Tablatura, metrónomo, reloj y Escuchar","Registro, récords y progreso","Tus datos, siempre en tu dispositivo"],"Empezar gratis"),
  year=("Plus anual","19,99 €","al año",["Los 9.817 ejercicios, del nivel I al V","Ambas manos y Tabula completa","Los 4 planes guiados y tu plan personalizado","El año empieza cuando activas el código"],"Comprar Plus anual"),
  life=("Plus para siempre","49,99 €","un solo pago",["Todo lo de Plus anual","Sin renovaciones","Las novedades que lleguen, incluidas"],"Comprar para siempre"),
  best="Mejor valor",
  price_note="Pago seguro con Payhip. Recibes un código que activas en Ajustes → Plus; funciona también sin conexión y en todos tus dispositivos. Sin renovación automática. <a href=\"/legal#condiciones\">Condiciones de venta</a>.",
  sec_faq="Preguntas frecuentes",
  faq=[
    ("¿Necesito crear una cuenta?","No. No hay registro ni contraseña: abres la app y empiezas a tocar."),
    ("¿Funciona sin internet?","Sí. Después de abrirla una vez con conexión, funciona en modo avión o con una wifi que no responde."),
    ("¿Dónde se guarda mi práctica?","En tu dispositivo. Tu práctica no se envía a ningún servidor. Para pasarla a otro móvil, tablet u ordenador: Ajustes → Exportar copia, y en el otro, Importar."),
    ("¿Puedo usar Plus en varios dispositivos?","Sí. Activa el mismo código en tu móvil, tu tablet y tu ordenador."),
    ("¿Para qué guitarra y qué nivel?","Eléctrica o acústica, con púa, con dedos (p i m a) o en híbrido. Del nivel I, con los primeros cruces de cuerda, al V, con enclosures, voicings drop 2 y drop 3 y Tabula."),
    ("¿Cuánto tiempo necesito al día?","Los planes van de 25 a 60 minutos, 5 días por semana. Con un Snack bastan 10 o 20 minutos, y el plan personalizado empieza en 10."),
    ("¿Qué pasa si termina mi año de Plus?","Todo lo que registraste se queda. Vuelves a la versión gratuita hasta que renueves."),
    ("¿Hay versión en App Store o Google Play?","Es una app web instalable: se instala desde el navegador en unos segundos y no ocupa espacio de más."),
  ],
  faq_contact="¿Otra pregunta? Escribe a",
  final_t="Coge la guitarra. El plan de hoy ya está listo.",
  final_cta="Empezar gratis",
  foot_priv="Aviso legal y privacidad", legal="/legal", foot_rights="© 2026 Jacob Carrasco",
  guides=[("ejercicios-guitarra-mano-derecha","Ejercicios mano derecha"),("ejercicios-guitarra-mano-izquierda","Ejercicios mano izquierda"),("rutina-de-practica-de-guitarra","Rutina de práctica")],
  phone_alt={"home":"Pantalla de Inicio con el plan de hoy","practice_voi":"Pantalla de práctica con tablatura, acordes y metrónomo","log":"Registro de una pasada","plan":"Vista del plan","progress":"Progreso","tabula":"Tabula, el reto de intervalos"},
),
"en": dict(
  lang="en", other="es", other_href="/", other_label="Español", app="/app/en", img="en",
  title="Dextra Sinistra · guitar technique for both hands",
  desc="9,817 guitar exercises for the picking hand, the fretting hand and both together, with tab, metronome, timer, practice log and guided plans. No account, works offline.",
  nav=[("#exercises","Exercises"),("#method","Method"),("#how-it-works","How it works"),("#pricing","Pricing"),("#faq","FAQ")],
  open_app="Open the app",
  back_bar="Your practice is saved on this device.", back_cta="Continue in the app →",
  eyebrow="Technique app for guitarists",
  h1="Train each hand on its own.<br>Then put them together.",
  lead="Dextra Sinistra brings together 9,817 guitar exercises with tab, metronome, timer and a log of every run. Open the app and you know what to play today, for how long and at what tempo.",
  cta1="Start free", cta2="How it works",
  note="No account · works offline · 14 days of Plus included",
  stats=[("2,715","Dextra","picking hand"),("3,087","Sinistra","fretting hand"),("4,015","Both","hands together"),("4","guided plans","8 to 12 weeks")],
  sec_hands="Three sections, one guitar",
  sec_hands_p="Every exercise has its code, a level from I to V, a tempo range and a tip on why it is there.",
  hands=[
    ("d","Dextra","The hand that picks","Alternate, hybrid, sweep and economy, strumming and rhythm, scales and arpeggios, enclosures and voicings. With a pick, with fingers (p i m a) and hybrid."),
    ("s","Sinistra","The hand that frets","Independence, legato, stretches and position shifts, bends and vibrato, chords and barre, muting. Also scales, arpeggios, enclosures and voicings."),
    ("a","Both","The two in sync","Fretboard maps, enclosures and voicings with pick and fingers at once. Plus Tabula, the 11 × 11 interval challenge."),
  ],
  shared="Many exercises exist in all three sections under the same number: first the picking hand alone (D-1204), then the fretting hand alone (S-1204), and finally both together (A-1204). Same music, one hand at a time.",
  sec_method="A method, not a list of exercises",
  sec_method_p="Practicing a lot is not the same as practicing well. The app decides the order, the time and the tempo, so all you have to do is play.",
  method=[
    ("Cycle-based plans","Every week a core exercise comes in and stays for three: two weeks raising the tempo and one of mastery at 90 % of your record, with a test on the last day. Pass it and it leaves the plan; if not, it stays one more week."),
    ("The 4 rules of a clean run","The whole exercise, start to finish. Complete, nothing left out. It sounds good. In time. Only clean runs count toward your record."),
    ("The tempo adjusts itself","Clean: 4 BPM more next time. Controlled: you keep it. Tense: you drop 10 %. No guessing what speed to work at."),
    ("Your real time, not the ideal","Every plan day as a full session or a short Snack. Whatever you don't finish is saved and you pick it up another day, on this device or another."),
  ],
  plans_t="The plans",
  plans=[("Beginner","8 weeks · 25 min"),("Intermediate","10 weeks · 40 min"),("Advanced","12 weeks · 60 min"),("Expert","12 weeks · 60 min")],
  plans_note="5 days a week. Every day works both hands: the Dextra exercise, its Sinistra partner and a Both block at the end. Or build your own plan: choose days, minutes per session, weeks, level and what you want to work on.",
  extras=[("Warm-up","5 minutes before a gig or 10 to start a practice session."),("Speed challenge","One exercise a week: a ladder of +3 % every 4 bars, a tension button and bursts at +10 %."),("Professional format","Half the exercises and double the time on each.")],
  sec_how="How it works",
  sec_how_p="Five screens and nothing to set up. This is a normal day with the app.",
  steps=[
    ("home","Open Home and decide in one tap","Today's plan is at the top: choose the full session or a Snack depending on the time you have. Below, the warm-up, the weekly challenge and free practice with your last exercise."),
    ("practice_voi","Play with the tab in front of you","Tab, metronome and timer on one screen, with a bar that runs along the tab while you play. Hold − or + to change the tempo fast, tap Listen to hear the pattern and turn your phone to see it big. In voicings you see the chord and its frets."),
    ("log","Say how it went","When the time is up you mark Tense, Controlled or Clean. To count as Clean, all four rules. The app works out next time's tempo."),
    ("plan","Follow the plan day by day","Every day has its session. When you finish the last exercise you choose to go on to the next day or stop for today, and you can run several plans at once."),
    ("progress","See how you're doing","Minutes per day and per hand, streak, clean runs and each exercise's path to its goal tempo. And you can share your week."),
  ],
  tabula_t="Tabula: 121 interval pieces",
  tabula_p="Each piece combines an interval built on the root with the distance between roots, in 6 variants: 726 exercises for both hands. A piece is complete when its 6 variants are clean at 100 BPM or more.",
  tabula_credit="Inspired by Jonathan Kreisberg's Interval Matrix.",
  install_t="Install it like an app",
  install=[("iPhone and iPad","Open it in Safari, tap Share and then “Add to Home Screen”."),("Android","In Chrome, menu ⋮ and “Install app”."),("Computer","In Chrome or Edge, the install icon in the address bar.")],
  install_note="It opens full screen like any app and works offline.",
  sec_price="Pricing",
  sec_price_p="When you open the app you get 14 days of full Plus. When they end, you keep the free exercises and all your progress.",
  free=("Free","€0","forever",["153 exercises: the 87 level I exercises of Dextra and Sinistra and the first row of Tabula","Tab, metronome, timer and Listen","Practice log, records and progress","Your data, always on your device"],"Start free"),
  year=("Plus yearly","€19.99","a year",["All 9,817 exercises, levels I to V","Both hands and the full Tabula","The 4 guided plans and your custom plan","The year starts when you activate your code"],"Buy Plus yearly"),
  life=("Plus forever","€49.99","one payment",["Everything in Plus yearly","No renewals","Future additions included"],"Buy Plus forever"),
  best="Best value",
  price_note="Secure payment with Payhip. You get a code you activate in Settings → Plus; it also works offline and on all your devices. No automatic renewal. <a href=\"/legal-en#terms\">Terms of sale</a>.",
  sec_faq="FAQ",
  faq=[
    ("Do I need an account?","No. No sign-up and no password: open the app and start playing."),
    ("Does it work offline?","Yes. After opening it once with a connection, it works in airplane mode or on Wi-Fi that isn't responding."),
    ("Where is my practice saved?","On your device. Your practice is not sent to any server. To move it to another phone, tablet or computer: Settings → Export backup, and Import on the other one."),
    ("Can I use Plus on several devices?","Yes. Activate the same code on your phone, your tablet and your computer."),
    ("Which guitar and which level?","Electric or acoustic, with a pick, with fingers (p i m a) or hybrid. From level I, with the first string crossings, to level V, with enclosures, drop 2 and drop 3 voicings and Tabula."),
    ("How much time do I need a day?","The plans go from 25 to 60 minutes, 5 days a week. A Snack takes 10 or 20 minutes, and the custom plan starts at 10."),
    ("What happens when my Plus year ends?","Everything you logged stays. You go back to the free version until you renew."),
    ("Is it on the App Store or Google Play?","It's an installable web app: it installs from the browser in a few seconds and takes up no extra space."),
  ],
  faq_contact="Another question? Write to",
  final_t="Pick up the guitar. Today's plan is ready.",
  final_cta="Start free",
  foot_priv="Legal and privacy", legal="/legal-en", foot_rights="© 2026 Jacob Carrasco",
  guides=[("right-hand-guitar-exercises","Right-hand exercises"),("left-hand-guitar-exercises","Left-hand exercises"),("guitar-practice-routine","Practice routine")],
  phone_alt={"home":"Home screen with today's plan","practice_voi":"Practice screen with tab, chords and metronome","log":"Logging a run","plan":"Plan view","progress":"Progress","tabula":"Tabula, the interval challenge"},
),
}

CSS = r"""
:root{
  --bg:#ECEFF4; --surface:#E5E9F0; --raise:#F4F6F9; --card:#F7F8FA; --line:#D8DEE9; --line2:#C9D1DE;
  --fg:#2E3440; --muted:#4C566A; --faint:#7A8599;
  --acc-d:#5E81AC; --acc-s:#B4664D; --green:#7F9A6A;
  --hl-d:rgba(94,129,172,.12); --hl-s:rgba(180,102,77,.11);
  --bezel:#2E3440; --shadow:0 30px 60px -30px rgba(46,52,64,.45), 0 10px 24px -12px rgba(46,52,64,.25);
  --f-ui:"Instrument Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --f-mono:"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  color-scheme:light;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#2E3440; --surface:#3B4252; --raise:#353C4A; --card:#353C4A; --line:#434C5E; --line2:#4C566A;
  --fg:#ECEFF4; --muted:#D8DEE9; --faint:#9AA5B8; --acc-d:#88C0D0; --acc-s:#D08770; --green:#A3BE8C;
  --hl-d:rgba(136,192,208,.12); --hl-s:rgba(208,135,112,.14); --bezel:#1F242D;
  --shadow:0 30px 60px -30px rgba(0,0,0,.7), 0 10px 24px -12px rgba(0,0,0,.5); color-scheme:dark }}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 var(--f-ui);-webkit-font-smoothing:antialiased}
a{color:inherit}
img{max-width:100%;display:block}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.mono{font-family:var(--f-mono)}
h1,h2,h3{letter-spacing:-.02em;line-height:1.12;margin:0;font-weight:600}
h2{font-size:clamp(28px,4vw,40px)}
h3{font-size:19px;letter-spacing:-.01em}
p{margin:0}
.sec{padding:clamp(64px,9vw,112px) 0}
section[id]{scroll-margin-top:72px}
.sec-h{max-width:640px;margin-bottom:40px}
.sec-h p{color:var(--muted);margin-top:14px;font-size:18px}
.eyebrow{font:500 12px/1 var(--f-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}

/* barra de vuelta */
.back{display:none;background:var(--fg);color:var(--bg);font-size:14px}
.back.on{display:block}
.back .wrap{display:flex;gap:12px;align-items:center;justify-content:center;padding-top:9px;padding-bottom:9px;flex-wrap:wrap}
.back a{font-weight:600;text-decoration:none}

/* cabecera */
header.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:saturate(1.4) blur(12px);-webkit-backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid transparent;transition:border-color .2s}
header.top.sc{border-bottom-color:var(--line)}
.top .wrap{display:flex;align-items:center;gap:20px;height:64px}
.brand{white-space:nowrap;display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:600;font-size:17px;letter-spacing:-.01em;margin-right:auto}
.brand img{width:30px;height:30px;border-radius:8px}
.nav{display:flex;gap:22px;font-size:15px}
.nav a{text-decoration:none;color:var(--muted)}
.nav a:hover{color:var(--fg)}
.lang{font:500 13px var(--f-mono);text-decoration:none;color:var(--faint);border:1px solid var(--line2);border-radius:999px;padding:5px 10px}
.btn{white-space:nowrap;display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;padding:13px 22px;font:600 16px var(--f-ui);text-decoration:none;border:1px solid transparent;cursor:pointer;transition:transform .15s,background .15s}
.btn:active{transform:scale(.98)}
.btn.pri{background:var(--acc-d);color:#fff}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .btn.pri{color:#2E3440}}
.btn.pri:hover{filter:brightness(1.06)}
.btn.sec2{border-color:var(--line2);color:var(--fg);background:transparent}
.btn.sec2:hover{background:var(--raise)}
.btn.sm{padding:8px 15px;font-size:14px}
@media (max-width:860px){.nav{display:none}}
.lang .s{display:none}
@media (max-width:520px){.top .wrap{gap:10px}.brand{font-size:16px}.brand img{width:28px;height:28px}.lang .l{display:none}.lang .s{display:inline}.btn.sm{padding:8px 13px}.pl ul{grid-template-columns:1fr}}

/* portada */
.hero{padding:clamp(40px,7vw,88px) 0 clamp(56px,8vw,96px)}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center}
.hero h1{font-size:clamp(36px,4.6vw,56px);margin:18px 0 22px}
.hero h1 .d{color:var(--acc-d)} .hero h1 .s{color:var(--acc-s)}
.hero .lead{font-size:clamp(17px,2vw,20px);color:var(--muted);max-width:34em}
.hero .ctas{display:flex;gap:12px;flex-wrap:wrap;margin:30px 0 16px}
.hero .note{font-size:14px;color:var(--faint)}
.phones{position:relative;height:clamp(440px,52vw,600px)}
.phone{position:absolute;width:clamp(210px,24vw,280px);aspect-ratio:390/844;border-radius:38px;background:var(--bezel);padding:9px;box-shadow:var(--shadow)}
.phone img{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:30px;background:var(--raise)}
.phones .p1{left:2%;top:6%;transform:rotate(-4deg)}
.phones .p2{right:2%;top:0;transform:rotate(3deg);z-index:2}
@media (max-width:860px){
  .hero .wrap{grid-template-columns:1fr}
  .phones{height:auto;display:flex;justify-content:center;gap:14px;margin-top:8px}
  .phone{position:relative;width:min(44vw,240px);left:auto!important;right:auto!important;top:auto!important}
  .phones .p1{transform:rotate(-3deg) translateY(14px)} .phones .p2{transform:rotate(3deg)}
}

/* cifras */
.stats{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats .wrap{display:grid;grid-template-columns:repeat(4,1fr)}
.stat{padding:26px 18px;border-left:1px solid var(--line)}
.stat:first-child{border-left:0}
.stat b{display:block;font:500 clamp(28px,4vw,38px)/1 var(--f-mono);letter-spacing:-.03em}
.stat span{display:block;margin-top:10px;font-weight:600}
.stat small{color:var(--faint);font-size:14px}
.stat.d b{color:var(--acc-d)} .stat.s b{color:var(--acc-s)}
@media (max-width:700px){.stats .wrap{grid-template-columns:1fr 1fr}.stat:nth-child(3){border-left:0}.stat:nth-child(n+3){border-top:1px solid var(--line)}}

/* manos */
.hands{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.hand{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px}
.hand .dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px;vertical-align:1px}
.hand.d .dot{background:var(--acc-d)} .hand.s .dot{background:var(--acc-s)}
.hand.a .dot{background:linear-gradient(90deg,var(--acc-s) 0 50%,var(--acc-d) 50%)}
.hand .nm{font:500 13px var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--faint)}
.hand h3{margin:14px 0 10px}
.hand p{color:var(--muted);font-size:15.5px}
.shared{margin-top:18px;padding:20px 24px;border-radius:16px;background:linear-gradient(90deg,var(--hl-d),var(--hl-s));color:var(--muted);font-size:15.5px}
.shared .mono{color:var(--fg)}
@media (max-width:860px){.hands{grid-template-columns:1fr}}

/* método */
.method{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.mi{padding:26px;border-radius:18px;border:1px solid var(--line);background:var(--card)}
.mi .n{font:500 13px var(--f-mono);color:var(--acc-s)}
.mi h3{margin:10px 0 10px}
.mi p{color:var(--muted);font-size:15.5px}
.plans{margin-top:16px;display:grid;grid-template-columns:1.2fr 1fr;gap:16px}
.pl{padding:26px;border-radius:18px;background:var(--fg);color:var(--bg)}
.pl h3{margin-bottom:16px}
.pl ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pl li{border:1px solid color-mix(in srgb,var(--bg) 22%,transparent);border-radius:12px;padding:12px 14px}
.pl li b{display:block;font-weight:600}
.pl li span{font:13px var(--f-mono);opacity:.75}
.pl p{margin-top:16px;font-size:15px;opacity:.85}
.ex{display:grid;gap:10px}
.ex div{padding:18px 20px;border:1px solid var(--line);border-radius:16px;background:var(--card)}
.ex b{display:block;margin-bottom:4px}
.ex span{color:var(--muted);font-size:15px}
@media (max-width:860px){.method,.plans{grid-template-columns:1fr}.pl ul{grid-template-columns:1fr 1fr}}

/* cómo funciona */
.steps{display:grid;gap:clamp(48px,7vw,84px)}
.step{display:grid;grid-template-columns:auto 1fr;gap:clamp(28px,6vw,72px);align-items:center}
.step:nth-child(even){grid-template-columns:1fr auto}
.step:nth-child(even) .ph{order:2}
.step .ph .phone{position:relative;width:clamp(220px,26vw,270px)}
.step .num{font:500 14px var(--f-mono);color:var(--acc-d)}
.step h3{font-size:clamp(24px,3vw,30px);margin:10px 0 14px}
.step p{color:var(--muted);font-size:17px;max-width:30em}
@media (max-width:760px){.step,.step:nth-child(even){grid-template-columns:1fr;justify-items:center;text-align:left}.step:nth-child(even) .ph{order:0}.step .tx{justify-self:stretch}}
.tabula{margin-top:clamp(56px,8vw,96px);display:grid;grid-template-columns:1fr auto;gap:40px;align-items:center;padding:clamp(24px,4vw,44px);border-radius:24px;background:var(--card);border:1px solid var(--line)}
.tabula .phone{position:relative;width:clamp(200px,22vw,240px)}
.tabula p{color:var(--muted);margin-top:14px;font-size:17px;max-width:34em}
.tabula small{display:block;margin-top:14px;color:var(--faint)}
@media (max-width:760px){.tabula{grid-template-columns:1fr;justify-items:center}}
.install{margin-top:20px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.install div{padding:18px 20px;border-radius:16px;border:1px dashed var(--line2)}
.install b{display:block;margin-bottom:4px}
.install span{color:var(--muted);font-size:15px}
.inote{margin-top:12px;color:var(--faint);font-size:14px}
@media (max-width:760px){.install{grid-template-columns:1fr}}

/* precios */
.prices{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:stretch}
.pc{position:relative;display:flex;flex-direction:column;padding:28px;border-radius:20px;border:1px solid var(--line);background:var(--card)}
.pc.best{border-color:var(--acc-d);box-shadow:0 0 0 1px var(--acc-d)}
.pc .tag{position:absolute;top:-12px;left:24px;background:var(--acc-d);color:#fff;font:600 12px var(--f-ui);padding:4px 10px;border-radius:999px}
.pc h3{font-size:17px;color:var(--muted);font-weight:500}
.pc .pr{margin:14px 0 2px;font:500 40px/1 var(--f-mono);letter-spacing:-.03em}
.pc .per{color:var(--faint);font-size:14px}
.pc ul{list-style:none;padding:0;margin:22px 0 26px;display:grid;gap:10px;flex:1;align-content:start}
.pc li{padding-left:24px;position:relative;font-size:15px;color:var(--muted)}
.pc li::before{content:"";position:absolute;left:2px;top:.5em;width:10px;height:6px;border-left:2px solid var(--green);border-bottom:2px solid var(--green);transform:rotate(-45deg)}
.pnote{margin-top:16px;color:var(--faint);font-size:14px}
@media (max-width:860px){.prices{grid-template-columns:1fr}}

/* preguntas */
.faq{max-width:780px}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:20px 40px 20px 0;font-weight:600;font-size:17px;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:6px;top:16px;font:400 24px var(--f-mono);color:var(--faint);transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 20px;color:var(--muted);max-width:40em}
.contact{margin-top:22px;color:var(--muted)}

/* cierre y pie */
.final{text-align:center;padding:clamp(64px,9vw,104px) 0;border-top:1px solid var(--line)}
.final h2{max-width:16em;margin:0 auto 26px}
footer{border-top:1px solid var(--line);padding:28px 0;color:var(--faint);font-size:14px}
footer .wrap{display:flex;gap:18px;flex-wrap:wrap;align-items:center}
footer a{text-decoration:none}
footer a:hover{color:var(--fg)}
footer .sp{margin-left:auto}
:focus-visible{outline:2px solid var(--acc-d);outline-offset:3px;border-radius:6px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
"""

def esc(s): return html.escape(s, quote=True)

def phone(t, key, cls="", eager=False):
    return f'<div class="phone {cls}"><img src="/img/{t["img"]}_{key}.webp" width="390" height="844" alt="{esc(t["phone_alt"][key])}"{"" if eager else " loading=\"lazy\""} decoding="async"></div>'

def page(code):
    t = T[code]; o = T[t["other"]]
    ids = [h for h, _ in t["nav"]]
    canon = "https://dextrasinistra.com/" if code == "es" else "https://dextrasinistra.com/en"
    h1 = t["h1"]
    stats = "".join(f'<div class="stat {["d","s","",""][i]}"><b>{n}</b><span>{a}</span><small>{b}</small></div>' for i, (n, a, b) in enumerate(t["stats"]))
    hands = "".join(f'<article class="hand {k}"><div class="nm"><span class="dot"></span>{n}</div><h3>{h}</h3><p>{p}</p></article>' for k, n, h, p in t["hands"])
    shared = t["shared"]
    for c in ("D-1204", "S-1204", "A-1204"): shared = shared.replace(c, f'<span class="mono">{c}</span>')
    method = "".join(f'<div class="mi"><div class="n mono">0{i+1}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(t["method"]))
    plans = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in t["plans"])
    extras = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t["extras"])
    steps = "".join(f'<div class="step"><div class="ph">{phone(t, k)}</div><div class="tx"><div class="num">0{i+1}</div><h3>{a}</h3><p>{b}</p></div></div>' for i, (k, a, b) in enumerate(t["steps"]))
    install = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t["install"])
    def pc(d, href, best=False, ext=False):
        n, pr, per, items, cta = d
        lis = "".join(f"<li>{x}</li>" for x in items)
        tgt = ' target="_blank" rel="noopener"' if ext else ""
        return (f'<div class="pc{" best" if best else ""}">' + (f'<span class="tag">{t["best"]}</span>' if best else "") +
                f'<h3>{n}</h3><div class="pr">{pr}</div><div class="per">{per}</div><ul>{lis}</ul>'
                f'<a class="btn {"pri" if best else "sec2"}" href="{href}"{tgt}>{cta}</a></div>')
    prices = pc(t["free"], t["app"]) + pc(t["year"], PAY_YEAR, ext=True) + pc(t["life"], PAY_LIFE, best=True, ext=True)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"])
    ld = json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":"Dextra Sinistra","applicationCategory":"MusicApplication",
          "operatingSystem":"Web, iOS, Android, Windows, macOS","inLanguage":code,"url":canon,"description":t["desc"],
          "offers":[{"@type":"Offer","price":p,"priceCurrency":"EUR"} for p in ("0","19.99","49.99")]}, ensure_ascii=False)
    ld_faq = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":html.unescape(q),"acceptedAnswer":{"@type":"Answer","text":html.unescape(a)}} for q, a in t["faq"]]}, ensure_ascii=False)
    guides = "".join(f'<a href="/{s}">{n}</a>' for s, n in t["guides"])
    app_target = t["app"]
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>/* instalada como app: directo a la app */try{{if(matchMedia("(display-mode: standalone)").matches||navigator.standalone===true)location.replace("{app_target}");}}catch(e){{}}</script>
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="es" href="https://dextrasinistra.com/">
<link rel="alternate" hreflang="en" href="https://dextrasinistra.com/en">
<link rel="alternate" hreflang="x-default" href="https://dextrasinistra.com/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dextra Sinistra">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://dextrasinistra.com/img/og_{code}.jpg">
<meta property="og:locale" content="{"es_ES" if code == "es" else "en_US"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ECEFF4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#2E3440" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/icons/icon.svg" type="image/svg+xml">
<link rel="icon" href="/icons/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preload" href="/fonts/sans-400.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/fonts/sans-600.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" as="image" href="/img/{t["img"]}_practice_voi.webp">
<script type="application/ld+json">{ld}</script>
<script type="application/ld+json">{ld_faq}</script>
<style>{FONTS}{CSS}</style>
</head>
<body>
<div class="back" id="back"><div class="wrap"><span>{t["back_bar"]}</span><a href="{app_target}">{t["back_cta"]}</a></div></div>
<header class="top" id="top"><div class="wrap">
  <a class="brand" href="{"/" if code == "es" else "/en"}"><img src="/icons/icon.svg" alt="" width="30" height="30">Dextra Sinistra</a>
  <nav class="nav" aria-label="{"Secciones" if code == "es" else "Sections"}">{nav}</nav>
  <a class="lang" href="{t["other_href"]}" hreflang="{t["other"]}" lang="{t["other"]}" aria-label="{t["other_label"]}"><span class="l">{t["other_label"]}</span><span class="s">{t["other"].upper()}</span></a>
  <a class="btn pri sm" href="{app_target}">{t["open_app"]}</a>
</div></header>
<main>
<section class="hero"><div class="wrap">
  <div>
    <div class="eyebrow">{t["eyebrow"]}</div>
    <h1>{h1}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="ctas"><a class="btn pri" href="{app_target}">{t["cta1"]}</a><a class="btn sec2" href="{ids[2]}">{t["cta2"]}</a></div>
    <p class="note">{t["note"]}</p>
  </div>
  <div class="phones">{phone(t, "home", "p1", True)}{phone(t, "practice_voi", "p2", True)}</div>
</div></section>
<section class="stats" aria-label="{"Cifras" if code == "es" else "Numbers"}"><div class="wrap">{stats}</div></section>
<section class="sec" id="{ids[0][1:]}"><div class="wrap">
  <div class="sec-h"><h2>{t["sec_hands"]}</h2><p>{t["sec_hands_p"]}</p></div>
  <div class="hands">{hands}</div>
  <p class="shared">{shared}</p>
</div></section>
<section class="sec" id="{ids[1][1:]}" style="padding-top:0"><div class="wrap">
  <div class="sec-h"><h2>{t["sec_method"]}</h2><p>{t["sec_method_p"]}</p></div>
  <div class="method">{method}</div>
  <div class="plans"><div class="pl"><h3>{t["plans_t"]}</h3><ul>{plans}</ul><p>{t["plans_note"]}</p></div><div class="ex">{extras}</div></div>
</div></section>
<section class="sec" id="{ids[2][1:]}" style="padding-top:0"><div class="wrap">
  <div class="sec-h"><h2>{t["sec_how"]}</h2><p>{t["sec_how_p"]}</p></div>
  <div class="steps">{steps}</div>
  <div class="tabula"><div><h2>{t["tabula_t"]}</h2><p>{t["tabula_p"]}</p></div>{phone(t, "tabula")}</div>
  <h3 style="margin-top:56px">{t["install_t"]}</h3>
  <div class="install">{install}</div>
  <p class="inote">{t["install_note"]}</p>
</div></section>
<section class="sec" id="{ids[3][1:]}" style="padding-top:0"><div class="wrap">
  <div class="sec-h"><h2>{t["sec_price"]}</h2><p>{t["sec_price_p"]}</p></div>
  <div class="prices">{prices}</div>
  <p class="pnote">{t["price_note"]}</p>
</div></section>
<section class="sec" id="{ids[4][1:]}" style="padding-top:0"><div class="wrap">
  <div class="sec-h"><h2>{t["sec_faq"]}</h2></div>
  <div class="faq">{faq}</div>
  <p class="contact">{t["faq_contact"]} <a href="mailto:{MAIL}">{MAIL}</a></p>
</div></section>
<section class="final"><div class="wrap"><h2>{t["final_t"]}</h2><a class="btn pri" href="{app_target}">{t["final_cta"]}</a></div></section>
</main>
<footer><div class="wrap">
  <span>{t["foot_rights"]}</span>
  <a href="{t["legal"]}">{t["foot_priv"]}</a>
  {guides}
  <a href="{t["other_href"]}" hreflang="{t["other"]}" lang="{t["other"]}">{t["other_label"]}</a>
  <a class="sp" href="{app_target}">{t["open_app"]} →</a>
</div></footer>
<script>
/* quien ya practica en este navegador ve el acceso directo a su app */
try{{var lg=JSON.parse(localStorage.getItem("dys-log")||"[]");if(lg&&lg.length)document.getElementById("back").classList.add("on");}}catch(e){{}}
/* línea bajo la cabecera al bajar */
var tp=document.getElementById("top");addEventListener("scroll",function(){{tp.classList.toggle("sc",scrollY>8)}},{{passive:true}});
/* la portada también se guarda para abrirla sin conexión */
if("serviceWorker" in navigator)addEventListener("load",function(){{navigator.serviceWorker.register("/sw.js",{{updateViaCache:"none"}}).catch(function(){{}})}});
</script>
{COUNTER}
</body>
</html>
"""

for code, fn in (("es", "index.html"), ("en", "en.html")):
    open(f"{REPO}/{fn}", "w").write(page(code))
print("ok")
