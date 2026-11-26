#!/usr/bin/env python3
"""Genera las guías de dextrasinistra.com (páginas pensadas para buscadores), en español e inglés.
Uso: python3 guias.py <carpeta del repositorio>"""
import sys, html, json

REPO = sys.argv[1]
FONTS = open(REPO + "/tools/fontface.css").read()
COUNTER = open(REPO + "/tools/counter.html").read()
BASE = "https://dextrasinistra.com/"
DATE = "2026-11-26"

CSS = """
:root{--bg:#ECEFF4;--surface:#E5E9F0;--card:#F7F8FA;--line:#D8DEE9;--fg:#2E3440;--muted:#4C566A;--faint:#7A8599;
--acc-d:#5E81AC;--acc-s:#B4664D;--green:#7F9A6A;--shadow:0 30px 60px -30px rgba(46,52,64,.45),0 10px 24px -12px rgba(46,52,64,.25);
--f-ui:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--f-mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme: dark){:root{--bg:#2E3440;--surface:#3B4252;--card:#353C4A;--line:#434C5E;--fg:#ECEFF4;--muted:#D8DEE9;--faint:#9AA5B8;
--acc-d:#88C0D0;--acc-s:#D08770;--green:#A3BE8C;--shadow:0 30px 60px -30px rgba(0,0,0,.7),0 10px 24px -12px rgba(0,0,0,.5);color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 var(--f-ui);-webkit-font-smoothing:antialiased;padding-bottom:84px}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:16px;height:60px}
.brand{font-weight:600;text-decoration:none;letter-spacing:-.01em;display:flex;align-items:center;gap:9px}.brand img{width:26px;height:26px;border-radius:7px}
.btn{display:inline-block;text-decoration:none;font-weight:600;border-radius:999px;padding:13px 22px;background:var(--fg);color:var(--bg);font-size:16px;line-height:1.2}
.btn.sm{padding:9px 16px;font-size:15px;margin-left:auto}
article{padding:36px 0 20px}
.eyebrow{font:500 12px/1 var(--f-mono);letter-spacing:.12em;text-transform:uppercase;color:var(--faint);margin:0 0 14px}
h1{font-size:clamp(32px,6.5vw,46px);line-height:1.1;letter-spacing:-.025em;margin:0 0 16px;font-weight:600}
h2{font-size:clamp(24px,4.2vw,30px);line-height:1.2;letter-spacing:-.02em;margin:44px 0 12px;font-weight:600}
h3{font-size:19px;margin:26px 0 6px;font-weight:600}
.lead{font-size:20px;color:var(--muted);margin:0 0 22px}
.hands{display:flex;gap:6px;margin:22px 0 8px}.hands i{flex:1;height:8px;border-radius:4px;background:var(--acc-d)}.hands i:nth-child(2){background:var(--acc-s)}.hands i:nth-child(3){background:var(--green)}
ul,ol{padding-left:22px}li{margin:6px 0}
ol.steps{list-style:none;counter-reset:s;padding:0}ol.steps li{counter-increment:s;position:relative;padding:0 0 14px 52px}
ol.steps li::before{content:counter(s,decimal-leading-zero);position:absolute;left:0;top:2px;font:500 14px var(--f-mono);color:var(--faint);border:1px solid var(--line);border-radius:8px;padding:3px 7px;background:var(--card)}
ol.steps b{display:block}
pre.tab{font:13.5px/1.45 var(--f-mono);background:var(--card);border:1px solid var(--line);border-left:5px solid var(--c,var(--acc-d));border-radius:12px;padding:14px 16px;overflow-x:auto;margin:14px 0 6px}
.cap{font-size:14px;color:var(--faint);margin:0 0 18px}
.box{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:18px 0}
.box b{display:block;margin-bottom:4px}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:26px 0 10px}
.shots img{border-radius:20px;box-shadow:var(--shadow);border:6px solid #2E3440;background:#2E3440}
.shots figure{margin:0}.shots figcaption{font-size:13.5px;color:var(--faint);text-align:center;margin-top:8px}
.mid{text-align:center;margin:12px 0 30px}
.cta{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:28px 24px;margin:46px 0 10px;text-align:center}
.cta h2{margin:0 0 8px}.cta p{color:var(--muted);margin:0 0 18px}
details{border-bottom:1px solid var(--line);padding:14px 0}details summary{font-weight:600;cursor:pointer}details p{margin:8px 0 0;color:var(--muted)}
.more{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}.more a{text-decoration:none;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:8px 16px;font-size:15px}
footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--faint);font-size:14px}footer .wrap{display:flex;gap:16px;flex-wrap:wrap}footer a{text-decoration:none}
.stick{position:fixed;left:0;right:0;bottom:0;z-index:9;padding:12px 16px calc(12px + env(safe-area-inset-bottom));background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid var(--line);display:flex;align-items:center;gap:12px;transform:translateY(110%);transition:transform .3s ease}
.stick.on{transform:none}.stick span{flex:1;font-size:14px;line-height:1.3;color:var(--muted)}.stick span b{display:block;color:var(--fg);font-size:15.5px}.stick .btn{flex:none;padding:10px 18px;font-size:15px}
@media(max-width:560px){.shots{grid-template-columns:1fr 1fr}.shots figure:nth-child(3){display:none}}
"""

L = {
"es": dict(app="/app/", home="/", open="Empezar gratis", other="English", priv="Aviso legal y privacidad", legal="/legal", rights="© 2026 Jacob Carrasco",
  stick_t="Técnica de guitarra para las dos manos", stick_s="Gratis · sin cuenta · funciona sin conexión",
  faq_t="Preguntas frecuentes", more_t="Sigue leyendo", eyebrow="Guía · Dextra Sinistra",
  caps=["Tablatura, metrónomo y reloj","Tu plan día a día","Cómo avanzas"]),
"en": dict(app="/app/en", home="/en", open="Start for free", other="Español", priv="Legal and privacy", legal="/legal-en", rights="© 2026 Jacob Carrasco",
  stick_t="Guitar technique for both hands", stick_s="Free · no account · works offline",
  faq_t="Frequently asked questions", more_t="Keep reading", eyebrow="Guide · Dextra Sinistra",
  caps=["Tab, metronome and timer","Your plan, day by day","See your progress"]),
}

TAB_RH = """D|---------0-0-0-0-|
A|-0-0-0-0---------|
   ↓ ↑ ↓ ↑ ↓ ↑ ↓ ↑"""
TAB_SPIDER = """G|-------------------------1-2-3-4-|
D|-----------------1-2-3-4---------|
A|---------1-2-3-4-----------------|
E|-1-2-3-4-------------------------|"""
TAB_LEGATO = """G|-5h7p5-----5h7p5-----|
D|-------7h9p7-----7h9-|"""
TAB_PIMA = """e|-------0-------0-|
B|-----0-------0---|
G|---0-------0-----|
E|-0-------0-------|
   p i m a p i m a"""

def P(*a): return "".join(f"<p>{x}</p>" for x in a)

G = [
# ---------------- MANO DERECHA ----------------
dict(lang="es", slug="ejercicios-guitarra-mano-derecha", pair="right-hand-guitar-exercises",
 title="Ejercicios de guitarra para la mano derecha: púa, dedos e híbrido · Dextra Sinistra",
 desc="Ejercicios para la mano derecha en guitarra: púa alterna, cruces de cuerda, economy, híbrido y dedos (p i m a). Con tablatura, metrónomo y cómo subir el tempo sin tensión.",
 h1="Ejercicios de guitarra para la mano derecha",
 lead="La mano derecha marca el ritmo, el ataque y la limpieza de todo lo que tocas. Se entrena igual que la izquierda: con ejercicios cortos, metrónomo y un tempo que sube solo cuando la pasada sale limpia.",
 body=f"""<h2>Por qué entrenar la mano derecha por separado</h2>
{P("Casi todos los errores que parecen de la mano izquierda nacen en la derecha: una púa que no cae a tiempo, un cruce de cuerda que se adelanta o una nota que suena más fuerte que las demás.",
   "Si tocas la mano derecha sola, sobre cuerdas al aire, la izquierda deja de tapar esos fallos y los oyes enseguida.")}
<h2>Las técnicas que hay que trabajar</h2>
<ul>
<li><b>Púa alterna (alternate picking):</b> abajo y arriba, siempre alternando, también al cambiar de cuerda.</li>
<li><b>Cruces de cuerda:</b> pasar de una cuerda a otra sin perder el pulso. Es donde más se nota la falta de control.</li>
<li><b>Economy y sweep:</b> aprovechar el movimiento de la púa al cambiar de cuerda en la misma dirección.</li>
<li><b>Híbrido:</b> púa y dedos medio y anular a la vez, para saltos de cuerda y acordes abiertos.</li>
<li><b>Dedos (p i m a):</b> pulgar, índice, medio y anular, para arpegios y fingerstyle.</li>
<li><b>Rasgado y rítmica:</b> el brazo como un péndulo constante aunque no toques todas las cuerdas.</li>
</ul>
<h2>Un ejercicio para empezar hoy</h2>
{P("Cruce de cuerda con púa alterna, solo cuerdas al aire. Pon el metrónomo a 60 BPM y toca corcheas: cuatro notas en la quinta cuerda y cuatro en la cuarta, sin parar.")}
<pre class="tab" style="--c:var(--acc-d)">{html.escape(TAB_RH)}</pre>
<p class="cap">↓ púa hacia abajo · ↑ púa hacia arriba. La púa sigue alternando al cambiar de cuerda.</p>
{P("Cuando salga limpio cuatro veces seguidas, sube 4 BPM. Si notas el brazo o la mano tensos, baja un 10 % y vuelve a subir otro día.")}
<h3>Y con dedos</h3>
{P("El mismo trabajo para fingerstyle: un arpegio sobre cuerdas al aire con p i m a, cada dedo en su cuerda.")}
<pre class="tab" style="--c:var(--acc-d)">{html.escape(TAB_PIMA)}</pre>
<p class="cap">p pulgar · i índice · m medio · a anular.</p>
<h2>Cómo subir el tempo sin tensión</h2>
<ol class="steps">
<li><b>Empieza donde salga limpio.</b> Todo el ejercicio, completo, que suene bien y a tempo.</li>
<li><b>Limpio: +4 BPM la próxima vez.</b> Subir poco y a menudo funciona mejor que grandes saltos.</li>
<li><b>Controlado: mantén el tempo.</b> Ya casi está: repítelo otro día.</li>
<li><b>Con tensión: baja un 10 %.</b> La tensión se graba igual que el movimiento; mejor no practicarla.</li>
</ol>
[[SHOTS]]
<h2>Cómo lo organiza Dextra Sinistra</h2>
{P("La sección Dextra tiene 2.715 ejercicios para la mano derecha, del nivel I al V: púa alterna, híbrido, sweep y economy, rasgado, escalas, arpegios, enclosures y voicings. Cada uno trae tablatura, metrónomo, reloj y su rango de tempo.",
   "Al acabar marcas cómo ha salido (con tensión, controlado o limpio) y la app calcula el tempo de la próxima vez. Muchos ejercicios tienen pareja en la mano izquierda con el mismo número, para trabajar después las dos juntas.")}""",
 faq=[("¿Cuánto tiempo al día para la mano derecha?","Con 10 o 15 minutos diarios se nota en pocas semanas, si son constantes y con metrónomo. Es mejor poco cada día que mucho un solo día."),
      ("¿Púa alterna o economy?","Las dos. La púa alterna da un pulso muy regular; el economy ahorra movimiento al cambiar de cuerda. Conviene dominar la alterna primero."),
      ("¿Sirve para guitarra clásica o acústica?","Sí. Los ejercicios con dedos (p i m a) son para cualquier guitarra, y los de púa valen para eléctrica y acústica."),
      ("¿Necesito saber leer partitura?","No. Todos los ejercicios vienen en tablatura.")]),
dict(lang="en", slug="right-hand-guitar-exercises", pair="ejercicios-guitarra-mano-derecha",
 title="Right-hand guitar exercises: picking, fingers and hybrid · Dextra Sinistra",
 desc="Right-hand guitar exercises: alternate picking, string crossing, economy, hybrid and fingerstyle (p i m a). With tab, metronome and how to raise the tempo without tension.",
 h1="Right-hand guitar exercises",
 lead="Your picking hand sets the rhythm, the attack and how clean everything sounds. Train it like the fretting hand: short exercises, a metronome, and a tempo that only goes up when the take is clean.",
 body=f"""<h2>Why train the picking hand on its own</h2>
{P("Many mistakes that seem to come from the fretting hand start in the picking hand: a pick stroke that lands late, a string crossing that rushes, or one note louder than the rest.",
   "Play the right hand alone, on open strings, and the left hand can no longer hide those mistakes. You hear them straight away.")}
<h2>The techniques to work on</h2>
<ul>
<li><b>Alternate picking:</b> down and up, always alternating, even when you change strings.</li>
<li><b>String crossing:</b> moving between strings without losing the pulse. This is where lack of control shows most.</li>
<li><b>Economy and sweep:</b> using the pick's motion when you change strings in the same direction.</li>
<li><b>Hybrid picking:</b> pick plus middle and ring fingers, for string skips and open voicings.</li>
<li><b>Fingerstyle (p i m a):</b> thumb, index, middle and ring, for arpeggios and fingerpicking.</li>
<li><b>Strumming and rhythm:</b> the arm moving like a steady pendulum, even when you don't hit every string.</li>
</ul>
<h2>One exercise to start today</h2>
{P("String crossing with alternate picking, open strings only. Set the metronome to 60 BPM and play eighth notes: four on the A string, four on the D string, without stopping.")}
<pre class="tab" style="--c:var(--acc-d)">{html.escape(TAB_RH)}</pre>
<p class="cap">↓ downstroke · ↑ upstroke. Keep alternating when you change strings.</p>
{P("When it comes out clean four times in a row, add 4 BPM. If your arm or hand feels tense, drop 10% and build back up another day.")}
<h3>And with fingers</h3>
{P("The same work for fingerstyle: an arpeggio on open strings with p i m a, each finger on its own string.")}
<pre class="tab" style="--c:var(--acc-d)">{html.escape(TAB_PIMA)}</pre>
<p class="cap">p thumb · i index · m middle · a ring.</p>
<h2>How to raise the tempo without tension</h2>
<ol class="steps">
<li><b>Start where it's clean.</b> The whole exercise, complete, sounding good and in time.</li>
<li><b>Clean: +4 BPM next time.</b> Small, frequent steps beat big jumps.</li>
<li><b>Controlled: keep the tempo.</b> You're nearly there: repeat it another day.</li>
<li><b>Tense: drop 10%.</b> Tension gets learned just like the movement, so don't practise it.</li>
</ol>
[[SHOTS]]
<h2>How Dextra Sinistra organises it</h2>
{P("The Dextra section has 2,715 right-hand exercises, from level I to V: alternate, hybrid, sweep and economy picking, strumming, scales, arpeggios, enclosures and voicings. Each one comes with tab, metronome, timer and its tempo range.",
   "When you finish, you mark how it went (tense, controlled or clean) and the app works out your next tempo. Many exercises have a left-hand twin with the same number, so you can later play both hands together.")}""",
 faq=[("How long should I practise the right hand each day?","10 to 15 minutes a day shows results within a few weeks, as long as it's regular and with a metronome. A little every day beats a lot on one day."),
      ("Alternate or economy picking?","Both. Alternate picking gives a very even pulse; economy saves motion when changing strings. It's worth mastering alternate picking first."),
      ("Does it work for classical or acoustic guitar?","Yes. The fingerstyle exercises (p i m a) work on any guitar, and the pick exercises suit electric and acoustic."),
      ("Do I need to read standard notation?","No. Every exercise comes in tab.")]),
# ---------------- MANO IZQUIERDA ----------------
dict(lang="es", slug="ejercicios-guitarra-mano-izquierda", pair="left-hand-guitar-exercises",
 title="Ejercicios de guitarra para la mano izquierda: independencia de dedos y legato · Dextra Sinistra",
 desc="Ejercicios para la mano izquierda en guitarra: independencia de dedos, el ejercicio de la araña, legato, extensiones, cambios de posición, bends y cejilla. Con tablatura y metrónomo.",
 h1="Ejercicios de guitarra para la mano izquierda",
 lead="La mano izquierda necesita fuerza justa, dedos independientes y movimientos pequeños. Estos ejercicios la entrenan poco a poco, sin forzar y con el metrónomo como referencia.",
 body=f"""<h2>Qué trabaja la mano izquierda</h2>
<ul>
<li><b>Independencia de dedos:</b> que cada dedo se mueva sin arrastrar a los demás, sobre todo el anular y el meñique.</li>
<li><b>Legato:</b> ligados ascendentes (hammer-on) y descendentes (pull-off), para que las notas suenen sin púa.</li>
<li><b>Extensiones y cambios de posición:</b> abrir la mano y desplazarla por el mástil sin cortar el sonido.</li>
<li><b>Bends y vibrato:</b> llegar a la nota exacta y moverla con control.</li>
<li><b>Acordes y cejilla:</b> pisar con la presión justa para que suenen todas las cuerdas.</li>
<li><b>Apagado:</b> silenciar las cuerdas que no tocan con los dedos que sobran.</li>
</ul>
<h2>El ejercicio de la araña (1-2-3-4)</h2>
{P("Es el clásico para la independencia de dedos: un dedo por traste, del índice al meñique, en cada cuerda. Empieza a 60 BPM, en corcheas, con la mano relajada.")}
<pre class="tab" style="--c:var(--acc-s)">{html.escape(TAB_SPIDER)}</pre>
<p class="cap">1 índice · 2 medio · 3 anular · 4 meñique. Sigue igual en la segunda y la primera cuerda, y luego baja.</p>
{P("Variaciones cuando salga limpio: 1-3-2-4, 1-4-2-3, o en el traste 5 y luego en el 1, donde los trastes son más anchos.")}
<h2>Legato: hammer-on y pull-off</h2>
{P("Toca solo la primera nota de cada grupo con la púa y saca las otras con los dedos. Las tres notas deben sonar igual de fuertes.")}
<pre class="tab" style="--c:var(--acc-s)">{html.escape(TAB_LEGATO)}</pre>
<p class="cap">h ligado ascendente (hammer-on) · p ligado descendente (pull-off).</p>
<h2>Tres reglas para no lesionarse</h2>
<ol class="steps">
<li><b>Presión justa.</b> Aprieta solo hasta que la nota suene limpia; más no ayuda.</li>
<li><b>Dedos cerca de las cuerdas.</b> Cuanto menos se levantan, más rápido y limpio tocas.</li>
<li><b>Si duele, para.</b> La tensión en la mano o el antebrazo es la señal para bajar un 10 % el tempo.</li>
</ol>
[[SHOTS]]
<h2>Cómo lo organiza Dextra Sinistra</h2>
{P("La sección Sinistra tiene 3.087 ejercicios para la mano izquierda, del nivel I al V: independencia, legato, extensiones y cambios de posición, bends y vibrato, acordes y cejilla, apagado, escalas, arpegios, enclosures y voicings.",
   "Cada ejercicio trae tablatura, metrónomo y reloj, y la app ajusta el tempo según cómo te salga. Muchos tienen pareja en la mano derecha con el mismo número, y al final se tocan las dos juntas.")}""",
 faq=[("¿Cuánto tarda en notarse la independencia de dedos?","Con 10 minutos diarios, la mayoría de la gente nota el anular y el meñique más sueltos en tres o cuatro semanas."),
      ("¿Los ejercicios cromáticos son música?","No mucho, pero son el gimnasio de la mano. Combínalos con escalas y arpegios, que trabajan lo mismo y además suenan."),
      ("¿Me duelen los dedos al principio, es normal?","Las yemas sensibles al principio, sí. Dolor en la muñeca o el antebrazo, no: para, relaja la mano y baja el tempo."),
      ("¿Sirve para zurdos?","Sí. Si tocas con la guitarra al revés, la mano que pisa es la derecha: los ejercicios son los mismos.")]),
dict(lang="en", slug="left-hand-guitar-exercises", pair="ejercicios-guitarra-mano-izquierda",
 title="Left-hand guitar exercises: finger independence and legato · Dextra Sinistra",
 desc="Fretting-hand guitar exercises: finger independence, the spider exercise, legato, stretches, position shifts, bends and barre chords. With tab and metronome.",
 h1="Left-hand guitar exercises",
 lead="Your fretting hand needs just enough pressure, independent fingers and small movements. These exercises train it step by step, without forcing, with the metronome as your guide.",
 body=f"""<h2>What the fretting hand works on</h2>
<ul>
<li><b>Finger independence:</b> each finger moving without dragging the others, especially the ring and little fingers.</li>
<li><b>Legato:</b> hammer-ons and pull-offs, so notes sound without picking.</li>
<li><b>Stretches and position shifts:</b> opening the hand and moving along the neck without cutting the sound.</li>
<li><b>Bends and vibrato:</b> hitting the exact pitch and moving it with control.</li>
<li><b>Chords and barre:</b> just enough pressure for every string to ring.</li>
<li><b>Muting:</b> silencing the strings you're not playing with your spare fingers.</li>
</ul>
<h2>The spider exercise (1-2-3-4)</h2>
{P("The classic for finger independence: one finger per fret, index to little finger, on every string. Start at 60 BPM, in eighth notes, with a relaxed hand.")}
<pre class="tab" style="--c:var(--acc-s)">{html.escape(TAB_SPIDER)}</pre>
<p class="cap">1 index · 2 middle · 3 ring · 4 little finger. Carry on the same way on the B and high E strings, then come back down.</p>
{P("Variations once it's clean: 1-3-2-4, 1-4-2-3, or start at the 5th fret and then move to the 1st, where the frets are wider.")}
<h2>Legato: hammer-ons and pull-offs</h2>
{P("Pick only the first note of each group and sound the others with your fingers. All three notes should be equally loud.")}
<pre class="tab" style="--c:var(--acc-s)">{html.escape(TAB_LEGATO)}</pre>
<p class="cap">h hammer-on · p pull-off.</p>
<h2>Three rules to avoid injury</h2>
<ol class="steps">
<li><b>Just enough pressure.</b> Press only until the note sounds clean; more doesn't help.</li>
<li><b>Fingers close to the strings.</b> The less they lift, the faster and cleaner you play.</li>
<li><b>If it hurts, stop.</b> Tension in the hand or forearm is the signal to drop the tempo by 10%.</li>
</ol>
[[SHOTS]]
<h2>How Dextra Sinistra organises it</h2>
{P("The Sinistra section has 3,087 fretting-hand exercises, from level I to V: independence, legato, stretches and position shifts, bends and vibrato, chords and barre, muting, scales, arpeggios, enclosures and voicings.",
   "Each exercise comes with tab, metronome and timer, and the app adjusts the tempo based on how it went. Many have a picking-hand twin with the same number, and in the end you play both hands together.")}""",
 faq=[("How long until finger independence improves?","With 10 minutes a day, most people feel their ring and little fingers loosen up within three or four weeks."),
      ("Are chromatic exercises music?","Not really, but they're the gym for your hand. Mix them with scales and arpeggios, which train the same and also sound good."),
      ("My fingertips hurt at first. Is that normal?","Sore fingertips at first, yes. Pain in the wrist or forearm, no: stop, relax your hand and lower the tempo."),
      ("Does it work for left-handed players?","Yes. If you play with the guitar flipped, your fretting hand is the right one: the exercises are the same.")]),
# ---------------- RUTINA ----------------
dict(lang="es", slug="rutina-de-practica-de-guitarra", pair="guitar-practice-routine",
 title="Rutina de práctica de guitarra: 25, 40 o 60 minutos al día · Dextra Sinistra",
 desc="Cómo organizar una rutina de práctica de guitarra: cuánto tiempo, en qué orden, cuántos días a la semana y cómo subir el tempo. Con planes de 25, 40 y 60 minutos.",
 h1="Una rutina de práctica de guitarra que sí se cumple",
 lead="Practicar mucho no es lo mismo que practicar bien. Una buena rutina decide por ti qué tocar, cuánto tiempo y a qué tempo, para que solo tengas que coger la guitarra.",
 body=f"""<h2>Las cuatro reglas de una buena rutina</h2>
<ol class="steps">
<li><b>Poco y a menudo.</b> Cinco días de 25 minutos valen más que un domingo de tres horas.</li>
<li><b>Las dos manos, cada día.</b> Un ejercicio para la mano que pulsa, otro para la que pisa y un bloque con las dos juntas.</li>
<li><b>Siempre con metrónomo.</b> Es la única forma de saber si avanzas.</li>
<li><b>Apunta cómo ha salido.</b> Con tensión, controlado o limpio: así sabes a qué tempo empezar mañana.</li>
</ol>
<h2>Tres rutinas según tu tiempo</h2>
<div class="box"><b>25 minutos · nivel inicial</b>5 min de calentamiento · 8 min de mano derecha · 8 min de mano izquierda · 4 min con las dos manos.</div>
<div class="box"><b>40 minutos · nivel intermedio</b>5 min de calentamiento · 12 min de mano derecha · 12 min de mano izquierda · 11 min con las dos manos o repertorio.</div>
<div class="box"><b>60 minutos · nivel avanzado</b>10 min de calentamiento · 15 min de mano derecha · 15 min de mano izquierda · 20 min con las dos manos: escalas, arpegios, voicings.</div>
{P("Cinco días a la semana y dos de descanso. Los días que vayas justo, haz una versión corta de 10 o 20 minutos: mantener la racha cuenta más que la duración.")}
<h2>Cuándo cambiar de ejercicio</h2>
{P("Un ejercicio se queda en tu rutina unas tres semanas: dos subiendo el tempo poco a poco y una tocándolo cómodo, por debajo de tu récord, para afianzarlo. Si al final sale limpio al tempo objetivo, entra otro; si no, se queda una semana más.")}
<h2>Cómo subir el tempo</h2>
<ul>
<li><b>Limpio:</b> la próxima vez, 4 BPM más.</li>
<li><b>Controlado:</b> mismo tempo.</li>
<li><b>Con tensión:</b> baja un 10 %.</li>
</ul>
[[SHOTS]]
<h2>Cómo lo hace Dextra Sinistra</h2>
{P("La app trae cuatro planes guiados (Inicial de 8 semanas y 25 minutos, Intermedio de 10 semanas y 40, Avanzado y Experto de 12 semanas y 60), cinco días por semana, o tu plan personalizado desde 10 minutos.",
   "Cada día trabaja las dos manos y, al acabar cada ejercicio, la app calcula tu próximo tempo. Si un día no terminas, lo retomas otro.")}""",
 faq=[("¿Cuánto hay que practicar guitarra al día?","Entre 20 y 60 minutos, cinco días por semana, es una buena base. Lo importante es la constancia y practicar con metrónomo."),
      ("¿Calentar antes de tocar es necesario?","Sí. Cinco minutos de ejercicios suaves preparan la mano y evitan tensiones, sobre todo antes de tocar rápido."),
      ("¿Qué hago si me salto un día?","Nada grave. Retoma el plan donde lo dejaste; lo que cuenta es la semana, no un día suelto."),
      ("¿Vale para cualquier estilo?","Sí. La técnica de las dos manos es la base del rock, el jazz, el pop, el flamenco o la clásica.")]),
dict(lang="en", slug="guitar-practice-routine", pair="rutina-de-practica-de-guitarra",
 title="Guitar practice routine: 25, 40 or 60 minutes a day · Dextra Sinistra",
 desc="How to build a guitar practice routine: how long, in what order, how many days a week and how to raise the tempo. With 25, 40 and 60-minute plans.",
 h1="A guitar practice routine you'll actually keep",
 lead="Practising a lot isn't the same as practising well. A good routine decides what to play, for how long and at what tempo, so all you have to do is pick up the guitar.",
 body=f"""<h2>Four rules of a good routine</h2>
<ol class="steps">
<li><b>Little and often.</b> Five days of 25 minutes beat one three-hour Sunday.</li>
<li><b>Both hands, every day.</b> One exercise for the picking hand, one for the fretting hand and a block with both together.</li>
<li><b>Always with a metronome.</b> It's the only way to know you're improving.</li>
<li><b>Note how it went.</b> Tense, controlled or clean: that tells you where to start tomorrow.</li>
</ol>
<h2>Three routines for the time you have</h2>
<div class="box"><b>25 minutes · beginner</b>5 min warm-up · 8 min picking hand · 8 min fretting hand · 4 min both hands.</div>
<div class="box"><b>40 minutes · intermediate</b>5 min warm-up · 12 min picking hand · 12 min fretting hand · 11 min both hands or repertoire.</div>
<div class="box"><b>60 minutes · advanced</b>10 min warm-up · 15 min picking hand · 15 min fretting hand · 20 min both hands: scales, arpeggios, voicings.</div>
{P("Five days a week, two days off. On busy days, do a short 10 or 20-minute version: keeping the streak matters more than the length.")}
<h2>When to change exercises</h2>
{P("An exercise stays in your routine for about three weeks: two raising the tempo little by little and one playing it comfortably, below your record, to lock it in. If it ends up clean at the target tempo, a new one comes in; if not, it stays one more week.")}
<h2>How to raise the tempo</h2>
<ul>
<li><b>Clean:</b> next time, 4 BPM faster.</li>
<li><b>Controlled:</b> same tempo.</li>
<li><b>Tense:</b> drop 10%.</li>
</ul>
[[SHOTS]]
<h2>How Dextra Sinistra does it</h2>
{P("The app has four guided plans (Beginner, 8 weeks at 25 minutes; Intermediate, 10 weeks at 40; Advanced and Expert, 12 weeks at 60), five days a week, or your own custom plan from 10 minutes.",
   "Every day works both hands and, after each exercise, the app works out your next tempo. If you don't finish a day, you pick it up another time.")}""",
 faq=[("How long should I practise guitar each day?","Between 20 and 60 minutes, five days a week, is a solid base. What matters is consistency and practising with a metronome."),
      ("Do I need to warm up before playing?","Yes. Five minutes of gentle exercises prepare your hand and prevent tension, especially before playing fast."),
      ("What if I skip a day?","Nothing serious. Pick the plan up where you left it; the week counts, not a single day."),
      ("Does it work for any style?","Yes. Two-hand technique is the base of rock, jazz, pop, flamenco and classical.")]),
]

NAV = {
 "es": [("ejercicios-guitarra-mano-derecha","Mano derecha"),("ejercicios-guitarra-mano-izquierda","Mano izquierda"),("rutina-de-practica-de-guitarra","Rutina de práctica"),("right-hand-guitar-exercises","In English")],
 "en": [("right-hand-guitar-exercises","Picking hand"),("left-hand-guitar-exercises","Fretting hand"),("guitar-practice-routine","Practice routine"),("ejercicios-guitarra-mano-derecha","En español")],
}

def page(g):
    l = L[g["lang"]]; lang = g["lang"]; url = BASE + g["slug"]
    alt_lang = "en" if lang == "es" else "es"
    es_slug = g["slug"] if lang == "es" else g["pair"]; en_slug = g["pair"] if lang == "es" else g["slug"]
    shots_k = ["practice_voi", "plan", "progress"]
    shots = '<div class="shots">' + "".join(f'<figure><img src="/img/{lang}_{k}.webp" width="390" height="844" loading="lazy" decoding="async" alt="{html.escape(c)}"><figcaption>{html.escape(c)}</figcaption></figure>' for k, c in zip(shots_k, l["caps"])) + '</div>'
    shots += f'<p class="mid"><a class="btn" href="{l["app"]}">{l["open"]} →</a></p>'
    body = g["body"].replace("[[SHOTS]]", shots)
    faqh = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in g["faq"])
    ld = [{"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["desc"],"inLanguage":lang,"url":url,
           "image":BASE+f"img/og_{lang}.jpg","author":{"@type":"Person","name":"Jacob Carrasco"},
           "publisher":{"@type":"Organization","name":"Dextra Sinistra","logo":{"@type":"ImageObject","url":BASE+"icons/icon-512.png"}},
           "datePublished":DATE,"dateModified":DATE},
          {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in g["faq"]]}]
    more = "".join(f'<a href="/{s}" hreflang="{"en" if s in [x for x,_ in NAV["en"][:3]] else "es"}">{html.escape(n)}</a>' for s, n in NAV[lang] if s != g["slug"])
    cta_t = {"es":"Coge la guitarra. El plan de hoy ya está listo.","en":"Pick up the guitar. Today's plan is ready."}[lang]
    cta_p = {"es":"9.817 ejercicios con tablatura, metrónomo y planes guiados. Gratis, sin cuenta y sin conexión.","en":"9,817 exercises with tab, metronome and guided plans. Free, no account, works offline."}[lang]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(g["title"])}</title>
<meta name="description" content="{html.escape(g["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{BASE}{es_slug}">
<link rel="alternate" hreflang="en" href="{BASE}{en_slug}">
<link rel="alternate" hreflang="x-default" href="{BASE}{es_slug}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Dextra Sinistra">
<meta property="og:title" content="{html.escape(g["title"])}">
<meta property="og:description" content="{html.escape(g["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/og_{lang}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ECEFF4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#2E3440" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/icons/icon.svg" type="image/svg+xml">
<link rel="icon" href="/icons/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="preload" href="/fonts/sans-400.woff" as="font" type="font/woff" crossorigin>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{FONTS}{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="{l["home"]}"><img src="/icons/icon.svg" alt="" width="26" height="26">Dextra Sinistra</a><a class="btn sm" href="{l["app"]}">{l["open"]}</a></div></header>
<main class="wrap"><article>
<p class="eyebrow">{l["eyebrow"]}</p>
<h1>{html.escape(g["h1"])}</h1>
<p class="lead">{html.escape(g["lead"])}</p>
<div class="hands" aria-hidden="true"><i></i><i></i><i></i></div>
{body}
<section class="cta"><h2>{cta_t}</h2><p>{cta_p}</p><a class="btn" href="{l["app"]}">{l["open"]}</a></section>
<h2>{l["faq_t"]}</h2>{faqh}
<h2>{l["more_t"]}</h2><div class="more">{more}</div>
</article></main>
<footer><div class="wrap"><span>{l["rights"]}</span><a href="{l["home"]}">Dextra Sinistra</a><a href="{l["legal"]}">{l["priv"]}</a><a href="/{g["pair"]}" hreflang="{alt_lang}" lang="{alt_lang}">{l["other"]}</a></div></footer>
<div class="stick" id="stick"><span><b>{l["stick_t"]}</b>{l["stick_s"]}</span><a class="btn" href="{l["app"]}">{l["open"]}</a></div>
<script>(function(){{var s=document.getElementById('stick');function f(){{s.classList.toggle('on',scrollY>420)}}addEventListener('scroll',f,{{passive:true}});f()}})()</script>
{COUNTER}
</body>
</html>
"""

for g in G:
    open(f"{REPO}/{g['slug']}.html", "w").write(page(g))
print("ok", len(G))
