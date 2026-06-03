import json, html, os
PDIR="/sessions/awesome-peaceful-babbage/mnt/kuzmenko/pages"
OUT="/sessions/awesome-peaceful-babbage/mnt/kuzmenko/index.html"
LIB=open("/sessions/awesome-peaceful-babbage/mnt/kuzmenko/build/page-flip.min.js",encoding="utf-8").read()
m=json.load(open(os.path.join(PDIR,"manifest.json")))
N=m["count"]; AR=m["ar"]
# BASE pinned to a commit after push to avoid stale jsDelivr cache; @main as fallback
BASE=os.environ.get("GK_BASE","https://cdn.jsdelivr.net/gh/amarshalkin/kuzmenko@main/pages/")
TITLE="Гастрокод — май 2026"
DLURL="https://disk.yandex.ru/i/EwZlR56RMYKx-w"

tpl=r'''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><title>__TITLE__</title>
<style>:root{color-scheme:light}*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:#e9e9ec;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;color:#1a1a1a;overflow:hidden;-webkit-user-select:none;user-select:none}
#loader{position:fixed;inset:0;z-index:60;background:#1b1613;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .6s ease}
#loader.hide{opacity:0;pointer-events:none}
.ldtop{position:absolute;top:24px;left:0;right:0;text-align:center;font-family:Georgia,serif;color:#c2a368;font-size:13px;letter-spacing:.42em;padding-left:.42em}
.ldmark{font-family:Georgia,serif;color:#f1e9da;font-size:clamp(24px,7vw,34px);letter-spacing:.30em;padding-left:.30em;margin-bottom:30px}
.ring{position:relative;width:188px;height:188px}.ring svg{display:block;transform:rotate(-90deg)}
.ringc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
#count{font-family:Georgia,serif;color:#f1e9da;font-size:46px;line-height:1}
.ringc .of{color:#9a8f7e;font-size:13px;margin-top:6px;letter-spacing:.04em}
.ldbarw{width:230px;height:1px;background:#3a322a;margin:30px 0 14px;position:relative}
#ldbar{position:absolute;left:0;top:0;height:1px;width:0;background:#c2a368;transition:width .2s linear}
#pct{color:#c2a368;font-size:13px;letter-spacing:.18em;margin-bottom:4px}
.ldbot{position:absolute;bottom:28px;left:0;right:0;text-align:center;padding:0 22px}
#cap{color:#cdbfa8;font-size:13px;letter-spacing:.03em}
#sub{color:#6f665a;font-size:11px;margin-top:5px;letter-spacing:.06em;min-height:13px}
#wrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#e9e9ec;touch-action:none}
#flip{box-shadow:0 14px 40px rgba(0,0,0,.22)}
#flip .stf__item img,#flip img{display:block;width:100%;height:100%}
.pg{background:#fff;overflow:hidden}.pg img{width:100%;height:100%;display:block}
#pagepill{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);background:rgba(27,22,19,.78);color:#f1e9da;font-size:12px;letter-spacing:.06em;padding:6px 14px;border-radius:999px;z-index:25;font-variant-numeric:tabular-nums}
#dl{position:fixed;bottom:14px;right:14px;z-index:25;display:inline-flex;align-items:center;gap:7px;text-decoration:none;background:rgba(27,22,19,.82);color:#f1e9da;font-size:13px;letter-spacing:.04em;padding:9px 15px;border-radius:999px;border:1px solid rgba(194,169,104,.5)}
#dl:hover{background:#c2a368;color:#1b1613}#dl svg{width:16px;height:16px;display:block}
#hint{position:fixed;bottom:46px;left:50%;transform:translateX(-50%);font-size:11px;color:#8a8a8a;z-index:24;letter-spacing:.03em}
@media(max-width:600px){#dl span{display:none}#dl{padding:10px}#hint{display:none}}
</style></head>
<body>
<div id="wrap"><div id="flip"></div></div>
<div id="pagepill">1 / __N__</div>
<div id="hint">Колесо · стрелки · тяни угол страницы</div>
<a id="dl" href="__DLURL__" target="_blank" rel="noopener noreferrer" title="Скачать PDF на Яндекс.Диске">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg><span>Скачать</span></a>

<div id="loader">
  <div class="ldtop">МАЙ 2026</div>
  <div class="ldmark">ГАСТРОКОД</div>
  <div class="ring"><svg viewBox="0 0 188 188" width="188" height="188">
    <circle cx="94" cy="94" r="86" fill="none" stroke="#3a322a" stroke-width="3"></circle>
    <circle id="ring" cx="94" cy="94" r="86" fill="none" stroke="#c2a368" stroke-width="3" stroke-linecap="round" stroke-dasharray="540.4" stroke-dashoffset="540.4"></circle>
  </svg><div class="ringc"><div id="count">0</div><div class="of">из __N__ страниц</div></div></div>
  <div class="ldbarw"><div id="ldbar"></div></div>
  <div id="pct">0%</div>
  <div class="ldbot"><div id="cap">Подготовка журнала…</div><div id="sub">&nbsp;</div></div>
</div>

<script>/* === StPageFlip (inlined, page-flip@2.0.7) === */
__LIB__
</script>
<script>(function(){
var BASE="__BASE__", N=__N__, AR=__AR__, C=540.4;
var GATE=Math.min(20,N), DUR=4200, CONC=6;
function pad(n){n=String(n);return n.length>=3?n:('000'+n).slice(-3);}
var IMGS=[]; for(var i=1;i<=N;i++) IMGS.push(BASE+'page-'+pad(i)+'.webp');
var loader=document.getElementById('loader'),ring=document.getElementById('ring'),ldbar=document.getElementById('ldbar');
var count=document.getElementById('count'),pct=document.getElementById('pct'),cap=document.getElementById('cap'),sub=document.getElementById('sub');
var wrap=document.getElementById('wrap'),flipEl=document.getElementById('flip'),pill=document.getElementById('pagepill');
var touch=(('ontouchstart' in window)||navigator.maxTouchPoints>0)&&window.innerWidth<900;
var pf=null, idx=0, pageImgs=[];

function section(p){
  if(p<=4) return 'ОБЛОЖКА';
  if(p<=22) return 'СЕРВИС И УПРАВЛЕНИЕ';
  if(p<=42) return 'ЛОКАЛЬНЫЕ ПРОИЗВОДИТЕЛИ';
  if(p<=62) return 'МОДНЫЙ КОД';
  if(p<=82) return 'ТУРИЗМ';
  if(p<=100) return 'ПАРТНЁРЫ';
  return 'ЗАВЕРШЕНИЕ';
}
// ---- gate preload: first GATE pages (warms cache) ----
var realLoaded=0, started=0;
function loadGate(i){ var im=new Image(); im.onload=im.onerror=function(){ realLoaded++; pumpGate(); }; im.src=IMGS[i]; }
function pumpGate(){ while(started<GATE && (started-realLoaded)<CONC){ loadGate(started++); } }
// ---- showcase loader: counter sweeps 0..N over DUR, reveal needs GATE ready ----
var t0=performance.now();
function ease(x){ return x<0.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2; }
function renderLoader(disp){
  var p=disp/N;
  ring.setAttribute('stroke-dashoffset',(C*(1-p)).toFixed(1));
  ldbar.style.width=(p*230).toFixed(1)+'px';
  count.textContent=disp; pct.textContent=Math.round(p*100)+'%';
  if(disp<N){ var cur=Math.min(disp+1,N); cap.textContent='Загрузка страницы '+cur; sub.textContent=section(cur); }
  else { cap.textContent='Журнал готов'; sub.textContent='ОТКРЫВАЕМ…'; }
}
function loop(now){
  var e=Math.min((now-t0)/DUR,1);
  renderLoader(Math.round(ease(e)*N));
  if(e>=1 && realLoaded>=GATE){ boot(); return; }
  requestAnimationFrame(loop);
}
// ---- build pages: first GATE get src now, rest lazy (background) ----
function buildPages(){
  flipEl.innerHTML=''; pageImgs=[];
  for(var i=0;i<N;i++){
    var pg=document.createElement('div'); pg.className='pg'; pg.setAttribute('data-density','soft');
    var im=document.createElement('img'); im.alt='Страница '+(i+1); im.draggable=false;
    if(i<GATE) im.src=IMGS[i]; else im.setAttribute('data-src',IMGS[i]);
    pg.appendChild(im); flipEl.appendChild(pg); pageImgs.push(im);
  }
}
function ensureSrc(i){ var im=pageImgs[i]; if(im && !im.getAttribute('src')){ var d=im.getAttribute('data-src'); if(d){ im.src=d; } } }
// ---- background loader (no UI) ----
var bgIdx=GATE, bgInflight=0;
function bgNext(){
  while(bgInflight<CONC && bgIdx<N){
    var im=pageImgs[bgIdx++];
    if(im.getAttribute('src')){ continue; }
    bgInflight++;
    (function(im){ im.onload=im.onerror=function(){ bgInflight--; bgNext(); }; im.src=im.getAttribute('data-src'); })(im);
  }
}
function dims(){
  var availH=window.innerHeight-24, availW=window.innerWidth-(touch?16:40);
  var w=availH/AR; if(w>availW)w=availW; var h=w*AR;
  return {w:Math.round(w), h:Math.round(h)};
}
function makePF(d){
  buildPages();
  var p=new St.PageFlip(flipEl,{
    width:d.w, height:d.h, size:'fixed',
    minWidth:120, maxWidth:3000, minHeight:160, maxHeight:4200,
    maxShadowOpacity:0.5, showCover:false, usePortrait:true, autoSize:false,
    mobileScrollSupport:false, drawShadow:true, flippingTime:800, swipeDistance:28,
    useMouseEvents:true, clickEventForward:true
  });
  p.loadFromHTML(flipEl.querySelectorAll('.pg'));
  p.on('flip', function(e){ idx=e.data; ensureSrc(idx); ensureSrc(idx+1); ensureSrc(idx-1); pill.textContent=(idx+1)+' / '+N; });
  return p;
}
function boot(){
  var d=dims();
  flipEl.style.width=d.w+'px'; flipEl.style.height=d.h+'px';
  pf=makePF(d);
  loader.classList.add('hide'); setTimeout(function(){loader.style.display='none';},650);
  bgNext(); // докачиваем остальное фоном, без лоадера
  var wlock=false, acc=0;
  wrap.addEventListener('wheel', function(e){
    e.preventDefault(); if(wlock) return; acc+=e.deltaY;
    if(acc>40){ acc=0; wlock=true; ensureSrc(idx+1); pf.flipNext(); setTimeout(function(){wlock=false;},820); }
    else if(acc<-40){ acc=0; wlock=true; ensureSrc(idx-1); pf.flipPrev(); setTimeout(function(){wlock=false;},820); }
  }, {passive:false});
  document.addEventListener('keydown', function(e){
    if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key==='PageDown'){ ensureSrc(idx+1); pf.flipNext(); e.preventDefault(); }
    else if(e.key==='ArrowLeft'||e.key==='ArrowUp'||e.key==='PageUp'){ ensureSrc(idx-1); pf.flipPrev(); e.preventDefault(); }
  });
  var rt; window.addEventListener('resize', function(){ clearTimeout(rt); rt=setTimeout(relayout, 220); });
}
function relayout(){
  if(!pf) return;
  var cur=0; try{ cur=pf.getCurrentPageIndex(); }catch(e){}
  try{ pf.destroy(); }catch(e){}
  var d=dims(); flipEl.style.width=d.w+'px'; flipEl.style.height=d.h+'px';
  buildPages();
  // keep already-loaded ones loaded
  for(var i=0;i<N;i++){ if(i<GATE || i<=bgIdx){ ensureSrc(i); } }
  pf=new St.PageFlip(flipEl,{
    width:d.w, height:d.h, size:'fixed', minWidth:120, maxWidth:3000, minHeight:160, maxHeight:4200,
    maxShadowOpacity:0.5, showCover:false, usePortrait:true, autoSize:false,
    mobileScrollSupport:false, drawShadow:true, flippingTime:800, swipeDistance:28, useMouseEvents:true, clickEventForward:true
  });
  pf.loadFromHTML(flipEl.querySelectorAll('.pg'));
  pf.on('flip', function(e){ idx=e.data; ensureSrc(idx); ensureSrc(idx+1); ensureSrc(idx-1); pill.textContent=(idx+1)+' / '+N; });
  if(cur>0){ setTimeout(function(){ try{ pf.turnToPage(cur); }catch(e){} }, 60); }
}
renderLoader(0); pumpGate(); requestAnimationFrame(loop);
})();</script>
</body></html>'''
out=(tpl.replace("__TITLE__",html.escape(TITLE)).replace("__DLURL__",DLURL)
        .replace("__BASE__",BASE).replace("__N__",str(N)).replace("__AR__",repr(AR))
        .replace("__LIB__",LIB))
open(OUT,"w",encoding="utf-8").write(out)
print("index.html",round(os.path.getsize(OUT)/1024,1),"KB  BASE=",BASE)
