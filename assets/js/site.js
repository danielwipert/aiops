/* ============================================================
   AI Operations Management — interaction layer
   Progressive enhancement: the essay, diagram fallback, and
   functions are fully readable without this file. Everything
   here is the enhancement layer only.
   ============================================================ */
(function(){
'use strict';

/* ---------- sticky nav ---------- */
var nav = document.getElementById('nav');
addEventListener('scroll', function(){ nav.classList.toggle('stuck', scrollY > 40); }, {passive:true});

/* ---------- mobile menu ---------- */
var menuBtn = document.getElementById('menuBtn'), navLinks = document.getElementById('navLinks');
menuBtn.addEventListener('click', function(){
  var open = navLinks.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
});
navLinks.querySelectorAll('a').forEach(function(a){
  a.addEventListener('click', function(){
    navLinks.classList.remove('open');
    menuBtn.setAttribute('aria-expanded','false');
  });
});

/* ---------- reveal on scroll (single fade-up, unobserve after) ---------- */
var io = new IntersectionObserver(function(es){
  es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
}, {threshold:0.12});
document.querySelectorAll('.rv').forEach(function(el){ io.observe(el); });

/* ---------- arm the triple-flow diagram on view ---------- */
var diagram = document.getElementById('diagram');
if(diagram){
  var dio = new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ diagram.classList.add('armed'); dio.unobserve(diagram); } });
  }, {threshold:0.35});
  dio.observe(diagram);
}

/* ---------- function cards highlight diagram segments ---------- */
var cards = document.querySelectorAll('.func-card');
var stages = document.querySelectorAll('.stage');
function setHot(segs){ stages.forEach(function(s){ s.classList.toggle('hot', segs.indexOf(s.dataset.seg) !== -1); }); }
cards.forEach(function(card){
  card.addEventListener('click', function(){
    var already = card.classList.contains('active');
    cards.forEach(function(c){ c.classList.remove('active'); });
    if(already){ setHot([]); return; }
    card.classList.add('active');
    setHot(card.dataset.hot.split(','));
  });
});

/* ---------- Monday Test ---------- */
var answers = [null,null,null,null,null];
var results = [
  {min:0,   max:1.5, t:'You are running the flow in the dark.',
   b:'Cost is accumulating by default across every workflow AI touches, and your records cannot reconstruct where it went or what it returned. The first move is not a strategy. It is a meter.'},
  {min:2,   max:3,   t:'Partial visibility, not yet a discipline.',
   b:'Some of the flow is visible, but visibility without ownership is a dashboard, not a discipline. Use the five functions to decide what needs an owner next.'},
  {min:3.5, max:4.5, t:'Emerging AI Operations Management.',
   b:'The functions are forming. What remains is making them recurring, owned, and measured. That is the difference between practicing a discipline and being lucky.'},
  {min:5,   max:5,   t:'A disciplined AI Operations foundation.',
   b:'You are practicing AI Operations Management, whatever your organization calls it. The next frontier is the value boundary: somewhere specific, someone accountable, netting captured value against fully loaded cost.'}
];
document.querySelectorAll('.q-item').forEach(function(item){
  var qi = +item.dataset.q;
  item.querySelectorAll('.q-opt').forEach(function(btn){
    btn.addEventListener('click', function(){
      item.querySelectorAll('.q-opt').forEach(function(b){ b.classList.remove('sel'); });
      btn.classList.add('sel');
      answers[qi] = +btn.dataset.v;
      score();
    });
  });
});
function score(){
  if(answers.some(function(a){ return a === null; })) return;
  var s = answers.reduce(function(a,b){ return a+b; }, 0);
  var r = results.find(function(r){ return s >= r.min && s <= r.max; }) || results[0];
  document.getElementById('resTitle').textContent = r.t;
  document.getElementById('resBody').textContent = r.b;
  document.getElementById('scoreCap').textContent = 'Score: ' + s + ' of 5';
  var res = document.getElementById('quizResult');
  res.classList.add('show');
  requestAnimationFrame(function(){ document.getElementById('scoreFill').style.width = (s/5*100) + '%'; });
  res.scrollIntoView({behavior:'smooth', block:'nearest'});
}

/* ============================================================
   SESSION METER — the signature. All state in-memory only.
   No localStorage, no analytics, nothing leaves this page.
   ============================================================ */
var M = {events:0, cost:0, value:0, captured:false, t0:Date.now()};
var $ = function(id){ return document.getElementById(id); };
var mEvents=$('mEvents'), mEventsWord=$('mEventsWord'), mCost=$('mCost'), pEvents=$('pEvents'), pCost=$('pCost'),
    pValue=$('pValue'), mLedger=$('mLedger'), mThesis=$('mThesis'), valueRow=$('valueRow'),
    meterPill=$('meterPill'), meterPanel=$('meterPanel');
var reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

function fmt(n){ return n.toFixed(4); }
function elapsed(){
  var s = Math.floor((Date.now() - M.t0) / 1000);
  return String(Math.floor(s/60)).padStart(2,'0') + ':' + String(s%60).padStart(2,'0');
}
function render(){
  mEvents.textContent = M.events; mCost.textContent = fmt(M.cost);
  mEventsWord.textContent = M.events === 1 ? 'event' : 'events';
  pEvents.textContent = M.events; pCost.textContent = fmt(M.cost);
  pValue.textContent = fmt(M.value);
}
function ledgerAdd(label, cost, cls){
  var row = document.createElement('div');
  row.className = 'm-entry' + (cls ? ' ' + cls : '');
  row.innerHTML = '<span class="m-t">' + elapsed() + '</span><span>' + label +
    '</span><span class="m-c">' + (cls === 'm-capture' ? '+' : '') + '<span class="cur">¤</span>' + fmt(cost) + '</span>';
  mLedger.prepend(row);
  while(mLedger.children.length > 30) mLedger.removeChild(mLedger.lastChild);
}
/* Passive cost registers immediately (<400ms): metering must feel live and causal. */
function consume(label, cost){
  M.events++; M.cost += cost;
  ledgerAdd(label, cost);
  render();
}

meterPill.addEventListener('click', function(){
  var open = meterPanel.hidden;
  meterPanel.hidden = !open;
  meterPill.setAttribute('aria-expanded', open);
});

/* --- event sources --- */
consume('page loaded', 0.0006);
setInterval(function(){ if(!document.hidden) consume('idle · time on page', 0.0002); }, 10000);

var seenSections = new Set();
var sio = new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(e.isIntersecting && !seenSections.has(e.target.id)){
      seenSections.add(e.target.id);
      var name = e.target.querySelector('.sec-title, h1');
      consume('section entered: ' + (name ? name.textContent.trim().replace(/\.$/,'').slice(0,34) : e.target.id), 0.0006);
    }
  });
}, {threshold:0.25});
document.querySelectorAll('section[id]').forEach(function(s){ sio.observe(s); });

var milestones = [25,50,75,100], hit = new Set();
addEventListener('scroll', function(){
  var d = Math.round((scrollY + innerHeight) / document.body.scrollHeight * 100);
  milestones.forEach(function(m){ if(d >= m && !hit.has(m)){ hit.add(m); consume('scroll depth: ' + m + '%', 0.0004); } });
}, {passive:true});

document.addEventListener('click', function(e){
  var card = e.target.closest('.func-card');
  if(card){ consume('function inspected: ' + card.querySelector('h3').textContent.trim().toLowerCase(), 0.0008); return; }
  var opt = e.target.closest('.q-opt');
  if(opt){
    var q = opt.closest('.q-item').querySelector('.q-num').textContent.trim().toLowerCase();
    consume('diagnostic answered: ' + q.replace(/ ·.*/,''), 0.0008);
  }
});

/* --- VALUE CAPTURE: the peak. Deliberately NOT instant (the second clock):
   the one deliberate act carries a weighted beat so it feels earned. --- */
var CAPTURE = 0.06; // notional captured-value amount (design spec §4 calibration knob)
function captureValue(){
  if(M.captured) return;
  M.captured = true;
  M.events++;
  ledgerAdd('VALUE BOUNDARY DRAWN · Monday Test completed', CAPTURE, 'm-capture');
  mThesis.textContent = 'Value accrues by design.';
  mThesis.classList.add('captured');
  valueRow.classList.add('captured');
  meterPill.classList.add('flash');
  var strong = valueRow.querySelector('strong');
  strong.classList.remove('m-val-pulse'); void strong.offsetWidth; strong.classList.add('m-val-pulse');

  var target = CAPTURE;
  if(reduceMotion){ M.value = target; render(); return; }
  var start = null, dur = 800;
  function step(ts){
    if(start === null) start = ts;
    var t = Math.min((ts - start) / dur, 1);
    var eased = 1 - Math.pow(1 - t, 3); /* easeOutCubic: a settling beat, not a jump */
    M.value = target * eased;
    render();
    if(t < 1) requestAnimationFrame(step);
    else { M.value = target; render(); }
  }
  requestAnimationFrame(step);
}
var resNode = document.getElementById('quizResult');
var mo = new MutationObserver(function(){ if(resNode.classList.contains('show')) captureValue(); });
mo.observe(resNode, {attributes:true, attributeFilter:['class']});

render();
})();
