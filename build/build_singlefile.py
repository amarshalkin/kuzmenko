import fitz, io, base64, os, html, json, time
from PIL import Image
SRC="/sessions/awesome-peaceful-babbage/mnt/uploads/e5e8a41e-79c6-4b79-a721-b59d2b631ba9-1780477733806_1клик — light.pdf"
OUT="/sessions/awesome-peaceful-babbage/mnt/outputs/gastrokod-flipbook-full.html"
TITLE="Гастрокод — май 2026"
DLURL="https://disk.yandex.ru/i/EwZlR56RMYKx-w"
W=1400; Q=72
doc=fitz.open(SRC); N=doc.page_count
imgs=[]; ar=None
t0=time.time()
for i in range(N):
    p=doc[i]; r=p.rect; zoom=W/r.width
    pix=p.get_pixmap(matrix=fitz.Matrix(zoom,zoom),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    buf=io.BytesIO(); im.save(buf,'WEBP',quality=Q,method=5)
    imgs.append("data:image/webp;base64,"+base64.b64encode(buf.getvalue()).decode())
    if ar is None: ar=pix.height/pix.width
print("rendered",N,"in",round(time.time()-t0,1),"s")
imgs_js=json.dumps(imgs)

tpl=r'''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><title>__TITLE__</title>
<style>:root{color-scheme:light}*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:#e9e9ec;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;color:#1a1a1a;overflow:hidden;-webkit-user-select:none;user-select:none}
/* loader */
#loader{position:fixed;inset:0;z-index:60;background:#1b1613;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .6s ease}
#loader.hide{opacity:0;pointer-events:none}
.ldtop{position:absolute;top:24px;left:0;right:0;text-align:center;font-family:Georgia,"Times New Roman",serif;color:#c2a368;font-size:13px;letter-spacing:.42em;padding-left:.42em}
.ldmark{font-family:Georgia,"Times New Roman",serif;color:#f1e9da;font-size:clamp(24px,7vw,34px);letter-spacing:.30em;padding-left:.30em;margin-bottom:30px}
.ring{position:relative;width:188px;height:188px}
.ring svg{display:block;transform:rotate(-90deg)}
.ringc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
#count{font-family:Georgia,"Times New Roman",serif;color:#f1e9da;font-size:46px;line-height:1}
.ringc .of{color:#9a8f7e;font-size:13px;margin-top:6px;letter-spacing:.04em}
.ldbarw{width:230px;height:1px;background:#3a322a;margin:30px 0 14px;position:relative}
#ldbar{position:absolute;left:0;top:0;height:1px;width:0;background:#c2a368}
#pct{color:#c2a368;font-size:13px;letter-spacing:.18em;margin-bottom:4px}
.ldbot{position:absolute;bottom:28px;left:0;right:0;text-align:center;padding:0 22px}
#cap{color:#cdbfa8;font-size:13px;letter-spacing:.03em}
#sub{color:#6f665a;font-size:11px;margin-top:5px;letter-spacing:.06em;min-height:13px}
#enter{margin-top:18px;display:none;border:1px solid #c2a368;color:#f1e9da;background:transparent;border-radius:999px;padding:10px 26px;font-size:13px;letter-spacing:.12em;cursor:pointer;font-family:Georgia,serif}
#enter:hover{background:#c2a368;color:#1b1613}
/* viewer */
#stage{position:absolute;top:0;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:center;overflow:hidden;perspective:2400px;touch-action:none;background:#e9e9ec}
#book{position:relative}
.layer{position:absolute;inset:0;background:#fff;overflow:hidden}
.layer img,.face img{width:100%;height:100%;display:block;pointer-events:none}
.leaf{position:absolute;inset:0;transform-style:preserve-3d;transform-origin:left center;will-change:transform;z-index:5}
.face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden;background:#fff}
.face.back{transform:rotateY(180deg);background:#efeeec}
#shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.28),rgba(0,0,0,0) 55%);opacity:0;z-index:6;pointer-events:none}
.zone{position:absolute;top:0;bottom:0;width:30%;z-index:20}
.zone.l{left:0}.zone.r{right:0}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:46px;height:66px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:30px;color:rgba(0,0,0,.34);background:rgba(255,255,255,.6);z-index:24;cursor:pointer;transition:opacity .2s}
.nav:hover{color:rgba(0,0,0,.62);background:rgba(255,255,255,.85)}
.nav.l{left:8px}.nav.r{right:8px}
.nav.off{opacity:0;pointer-events:none}
#pagepill{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);background:rgba(27,22,19,.78);color:#f1e9da;font-size:12px;letter-spacing:.06em;padding:6px 14px;border-radius:999px;z-index:25;font-variant-numeric:tabular-nums}
#dl{position:fixed;bottom:14px;right:14px;z-index:25;display:inline-flex;align-items:center;gap:7px;text-decoration:none;background:rgba(27,22,19,.82);color:#f1e9da;font-size:13px;letter-spacing:.04em;padding:9px 15px;border-radius:999px;border:1px solid rgba(194,169,104,.5)}
#dl:hover{background:#c2a368;color:#1b1613}
#dl svg{width:16px;height:16px;display:block}
@media(max-width:600px){.nav{width:40px;height:58px;font-size:26px;background:rgba(255,255,255,.42)}.nav.l{left:2px}.nav.r{right:2px}#dl span{display:none}#dl{padding:10px}}
</style></head>
<body>
<div id="stage">
  <div id="book">
    <div class="layer" id="base"><img id="baseImg" alt="Страница журнала"></div>
    <div id="shade"></div>
  </div>
  <div class="zone l" id="zl"></div><div class="zone r" id="zr"></div>
  <div class="nav l off" id="navL">‹</div><div class="nav r" id="navR">›</div>
</div>
<div id="pagepill">1 / __N__</div>
<a id="dl" href="__DLURL__" target="_blank" rel="noopener noreferrer" title="Скачать PDF на Яндекс.Диске">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
  <span>Скачать</span></a>

<div id="loader">
  <div class="ldtop">МАЙ 2026</div>
  <div class="ldmark">ГАСТРОКОД</div>
  <div class="ring">
    <svg viewBox="0 0 188 188" width="188" height="188">
      <circle cx="94" cy="94" r="86" fill="none" stroke="#3a322a" stroke-width="3"></circle>
      <circle id="ring" cx="94" cy="94" r="86" fill="none" stroke="#c2a368" stroke-width="3" stroke-linecap="round" stroke-dasharray="540.4" stroke-dashoffset="540.4"></circle>
    </svg>
    <div class="ringc"><div id="count">0</div><div class="of">из __N__ страниц</div></div>
  </div>
  <div class="ldbarw"><div id="ldbar"></div></div>
  <div id="pct">0%</div>
  <div class="ldbot">
    <div id="cap">Подготовка журнала…</div>
    <div id="sub">&nbsp;</div>
  </div>
  <button id="enter">Листать журнал</button>
</div>

<script>(function(){
var IMGS=__IMGS__, AR=__AR__, TOTAL=IMGS.length, C=540.4;
var idx=0, animating=false;
// elements
var loader=document.getElementById('loader'),ring=document.getElementById('ring'),ldbar=document.getElementById('ldbar');
var count=document.getElementById('count'),pct=document.getElementById('pct'),cap=document.getElementById('cap'),sub=document.getElementById('sub'),enter=document.getElementById('enter');
var stage=document.getElementById('stage'),book=document.getElementById('book'),baseImg=document.getElementById('baseImg'),shade=document.getElementById('shade');
var navL=document.getElementById('navL'),navR=document.getElementById('navR'),pill=document.getElementById('pagepill');
var touch=(('ontouchstart' in window)||navigator.maxTouchPoints>0)&&window.innerWidth<900;

function section(p){
  if(p<=4) return 'ОБЛОЖКА';
  if(p<=22) return 'СЕРВИС И УПРАВЛЕНИЕ';
  if(p<=42) return 'ЛОКАЛЬНЫЕ ПРОИЗВОДИТЕЛИ';
  if(p<=62) return 'МОДНЫЙ КОД';
  if(p<=82) return 'ТУРИЗМ';
  if(p<=100) return 'ПАРТНЁРЫ';
  return 'ЗАВЕРШЕНИЕ';
}
// ---- loader: real decode + smooth display tween ----
var realLoaded=0, shown=0, decodeIdx=0, revealed=false;
function decodeNext(){
  if(decodeIdx>=TOTAL) return;
  var i=decodeIdx++;
  var im=new Image();
  im.onload=im.onerror=function(){ realLoaded++; decodeNext(); };
  im.src=IMGS[i];
  if(decodeIdx<6) decodeNext(); // kick a few in parallel at start
}
function renderLoader(){
  var p=shown/TOTAL;
  ring.setAttribute('stroke-dashoffset',(C*(1-p)).toFixed(1));
  ldbar.style.width=(p*230).toFixed(1)+'px';
  count.textContent=shown;
  pct.textContent=Math.round(p*100)+'%';
  if(shown<TOTAL){ cap.textContent='Загрузка страницы '+shown; sub.textContent=section(shown); }
  else { cap.textContent='Журнал готов'; sub.textContent='МОЖНО ЛИСТАТЬ'; }
}
var lastTick=0, MIN_MS=20; // не быстрее ~2.2с на всё
function loop(ts){
  if(!lastTick) lastTick=ts;
  if(ts-lastTick>=MIN_MS){
    lastTick=ts;
    if(shown<realLoaded && shown<TOTAL){ shown++; renderLoader(); }
  }
  if(shown>=TOTAL){ onReady(); return; }
  requestAnimationFrame(loop);
}
function onReady(){
  renderLoader();
  enter.style.display='inline-block';
  setTimeout(reveal, 650); // авто-вход, плюс кнопка
}
function reveal(){
  if(revealed) return; revealed=true;
  loader.classList.add('hide');
  setTimeout(function(){ loader.style.display='none'; }, 650);
}
enter.onclick=reveal;

// ---- flipbook ----
function fit(){
  var availH=stage.clientHeight-24, availW=stage.clientWidth-(touch?10:120);
  var h=availH, w=h/AR;
  if(w>availW){ w=availW; h=w*AR; }
  book.style.width=Math.floor(w)+'px'; book.style.height=Math.floor(h)+'px';
}
function show(){ baseImg.src=IMGS[idx]; pill.textContent=(idx+1)+' / '+TOTAL; updNav(); }
function updNav(){ navL.classList.toggle('off',idx<=0); navR.classList.toggle('off',idx>=TOTAL-1); }
function flip(dir){
  if(animating)return; var target=idx+dir;
  if(target<0||target>=TOTAL)return; animating=true;
  var leaf=document.createElement('div');leaf.className='leaf';
  var front=document.createElement('div');front.className='face front';
  var back=document.createElement('div');back.className='face back';
  var fimg=document.createElement('img'),bimg=document.createElement('img');
  front.appendChild(fimg);back.appendChild(bimg);leaf.appendChild(front);leaf.appendChild(back);
  book.insertBefore(leaf,shade);
  var from,to;
  if(dir>0){ fimg.src=IMGS[idx]; baseImg.src=IMGS[target]; from=0; to=-180; }
  else { fimg.src=IMGS[target]; from=-180; to=0; }
  leaf.style.transform='rotateY('+from+'deg)';
  shade.animate([{opacity:0},{opacity:.32},{opacity:0}],{duration:660,easing:'ease-in-out'});
  leaf.animate([{transform:'rotateY('+from+'deg)'},{transform:'rotateY('+to+'deg)'}],{duration:660,easing:'cubic-bezier(.3,.1,.3,1)'}).onfinish=function(){
    idx=target; show(); leaf.remove(); animating=false;
  };
}
navR.onclick=function(){flip(1)};navL.onclick=function(){flip(-1)};
document.getElementById('zr').onclick=function(){flip(1)};
document.getElementById('zl').onclick=function(){flip(-1)};
document.addEventListener('keydown',function(e){
  if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key==='PageDown'){flip(1);e.preventDefault()}
  else if(e.key==='ArrowLeft'||e.key==='ArrowUp'||e.key==='PageUp'){flip(-1);e.preventDefault()}
});
var acc=0,lock=false;
stage.addEventListener('wheel',function(e){
  e.preventDefault(); if(animating)return; acc+=e.deltaY; if(lock)return;
  if(acc>60){lock=true;acc=0;flip(1);setTimeout(function(){lock=false},120);}
  else if(acc<-60){lock=true;acc=0;flip(-1);setTimeout(function(){lock=false},120);}
},{passive:false});
var tsx=null,tsy=null;
stage.addEventListener('touchstart',function(e){var t=e.changedTouches[0];tsx=t.clientX;tsy=t.clientY;},{passive:true});
stage.addEventListener('touchend',function(e){
  if(tsx===null)return; var t=e.changedTouches[0]; var dx=t.clientX-tsx,dy=t.clientY-tsy;
  if(Math.abs(dx)>42 && Math.abs(dx)>Math.abs(dy)){ flip(dx<0?1:-1); } tsx=null;
},{passive:true});
var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(fit,200)});

fit(); show();
decodeNext(); requestAnimationFrame(loop);
})();</script></body></html>'''
out=(tpl.replace("__TITLE__",html.escape(TITLE)).replace("__DLURL__",DLURL)
        .replace("__N__",str(N)).replace("__IMGS__",imgs_js).replace("__AR__",repr(ar)))
open(OUT,"w",encoding="utf-8").write(out)
print("written",OUT,"size MiB",round(os.path.getsize(OUT)/1048576,2))
