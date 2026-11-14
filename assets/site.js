(function(){
  var root=document.documentElement;
  var header=document.querySelector('.site-header');
  var onScroll=function(){header.classList.toggle('scrolled',window.scrollY>8)};
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  // Menu
  var btn=document.getElementById('menu-btn'),links=document.getElementById('nav-links');
  function setMenu(open){links.classList.toggle('open',open);btn.setAttribute('aria-expanded',open?'true':'false');btn.setAttribute('aria-label',open?'Close menu':'Open menu')}
  btn.addEventListener('click',function(){setMenu(!links.classList.contains('open'))});
  links.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&links.classList.contains('open')){setMenu(false);btn.focus()}});
  document.addEventListener('click',function(e){if(links.classList.contains('open')&&!e.target.closest('.nav'))setMenu(false)});

  var yr=document.getElementById('year');if(yr)yr.textContent=new Date().getFullYear();

  // Scroll reveal, staggered within each group. Everything is visible if this never runs.
  var els=[].slice.call(document.querySelectorAll('.reveal'));
  if('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches){
    root.classList.add('js');
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(!en.isIntersecting)return;
        var el=en.target,sib=[].slice.call(el.parentNode.children).filter(function(n){return n.classList.contains('reveal')});
        el.style.transitionDelay=Math.min(sib.indexOf(el),7)*60+'ms';
        el.classList.add('in');io.unobserve(el);
      });
    },{rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){io.observe(el)});
    setTimeout(function(){els.forEach(function(el){el.classList.add('in')})},4000);
  }

  // Product filter
  var filters=[].slice.call(document.querySelectorAll('.filter'));
  var cards=[].slice.call(document.querySelectorAll('[data-c]'));
  var featured=document.querySelector('.featured');
  filters.forEach(function(f){
    f.addEventListener('click',function(){
      var c=f.dataset.f;
      filters.forEach(function(x){x.setAttribute('aria-pressed',x===f?'true':'false')});
      cards.forEach(function(card){
        var show=c==='all'||card.dataset.c===c;
        card.classList.toggle('hide',!show);
        if(show&&card.animate&&!matchMedia('(prefers-reduced-motion: reduce)').matches){card.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:280,easing:'ease-out'})}
      });
      if(featured)featured.hidden=!featured.querySelector('.card:not(.hide)');
    });
  });

  // Contact form
  var form=document.getElementById('contact-form');if(!form)return;var status=document.getElementById('cf-status'),submit=document.getElementById('cf-submit');
  function show(msg,ok){status.setAttribute('role',ok?'status':'alert');status.textContent=msg;status.className='form-status'+(ok?' ok':'');status.hidden=false}
  form.addEventListener('input',function(e){e.target.removeAttribute('aria-invalid')});
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var names={'cf-name':'your name','cf-email':'your work email','cf-msg':'a short message'};
    var missing=[].slice.call(form.querySelectorAll('[required]')).filter(function(el){return !el.value.trim()});
    missing.forEach(function(el){el.setAttribute('aria-invalid','true')});
    if(missing.length){var n=missing.map(function(el){return names[el.id]});show('Please add '+(n.length>1?n.slice(0,-1).join(', ')+' and '+n[n.length-1]:n[0])+'.');missing[0].focus();return}
    var email=document.getElementById('cf-email');
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())){email.setAttribute('aria-invalid','true');show('Please enter a valid email address.');email.focus();return}
    var data={};new FormData(form).forEach(function(v,k){data[k]=String(v).trim()});
    submit.disabled=true;submit.textContent='Sending…';
    fetch('/submit-contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.ok?r.json():Promise.reject(r.status)})
      .then(function(){form.reset();show('Thank you. Your message has reached us, and we will reply within one working day.',true)})
      .catch(function(){show('Your message could not be sent from this page. Please email info@liwalabs.com or call +92 326 2263160.')})
      .finally(function(){submit.disabled=false;submit.textContent='Send message'});
  });
})();
