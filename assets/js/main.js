(function(){
  'use strict';
  function onReady(fn){ if(document.readyState!=='loading'){fn();} else {document.addEventListener('DOMContentLoaded',fn);} }
  onReady(function(){
    // Sticky header shadow
    var header=document.querySelector('[data-header]');
    var onScroll=function(){ if(header){ header.classList.toggle('is-scrolled', window.scrollY>8); } };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

    // Mobile nav
    var toggle=document.querySelector('[data-nav-toggle]');
    var nav=document.querySelector('[data-nav]');
    if(toggle&&nav){
      toggle.addEventListener('click',function(){
        var open=nav.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open?'true':'false');
        toggle.setAttribute('aria-label', open?'Close navigation':'Open navigation');
      });
      nav.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ nav.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); }); });
    }

    // Reveal on scroll
    var reveals=document.querySelectorAll('.reveal');
    if('IntersectionObserver' in window && reveals.length){
      var io=new IntersectionObserver(function(entries){
        entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
      },{threshold:.12,rootMargin:'0px 0px -40px 0px'});
      reveals.forEach(function(el){ io.observe(el); });
    } else { reveals.forEach(function(el){ el.classList.add('in'); }); }

    // Tabs / category filter
    document.querySelectorAll('[data-tabs]').forEach(function(group){
      var btns=group.querySelectorAll('[data-filter]');
      var panels=group.querySelectorAll('[data-panel]');
      btns.forEach(function(btn){
        btn.addEventListener('click',function(){
          var f=btn.getAttribute('data-filter');
          btns.forEach(function(b){ b.classList.toggle('is-active', b===btn); });
          panels.forEach(function(p){
            var match=(f==='all'||p.getAttribute('data-panel')===f);
            p.classList.toggle('is-active', match);
          });
        });
      });
    });

    // Filter inside a single grid (all .p-item cards)
    document.querySelectorAll('[data-filter-grid]').forEach(function(wrap){
      var btns=wrap.querySelectorAll('.tab-btn');
      var items=wrap.querySelectorAll('.p-item');
      var empty=wrap.querySelector('.empty-state');
      btns.forEach(function(btn){
        btn.addEventListener('click',function(){
          var f=btn.getAttribute('data-filter');
          btns.forEach(function(b){ b.classList.toggle('is-active', b===btn); });
          var shown=0;
          items.forEach(function(card){
            var show=(f==='all'||card.getAttribute('data-cat').split(' ').indexOf(f)>-1);
            card.style.display=show?'':'none';
            if(show) shown++;
          });
          if(empty) empty.classList.toggle('show', shown===0);
        });
      });
    });

    // FAQ accordion
    document.querySelectorAll('.faq-item').forEach(function(item){
      var q=item.querySelector('.faq-q');
      if(!q) return;
      q.addEventListener('click',function(){
        var open=item.classList.toggle('is-open');
        q.setAttribute('aria-expanded', open?'true':'false');
      });
    });

    // Material swatch highlight
    document.querySelectorAll('[data-swatches]').forEach(function(group){
      var swatches=group.querySelectorAll('.swatch');
      var label=group.querySelector('[data-swatch-name]');
      var current=null;
      swatches.forEach(function(s){
        s.addEventListener('click',function(){
          swatches.forEach(function(x){ x.style.outline=''; x.style.boxShadow='0 0 0 1px var(--line)'; });
          this.style.boxShadow='0 0 0 2px var(--camel-500)';
          if(label) label.textContent='Selected: '+this.getAttribute('aria-label');
        });
      });
    });

    // Inquiry forms -> mailto with prefilled body
    document.querySelectorAll('form[data-mailto]').forEach(function(form){
      form.addEventListener('submit',function(ev){
        ev.preventDefault();
        var email=form.getAttribute('data-mailto');
        var subject=form.getAttribute('data-subject')||'RFQ from website';
        var lines=[];
        var skip=['_subject','_next'];
        form.querySelectorAll('[name]').forEach(function(f){
          if(skip.indexOf(f.name)>-1) return;
          var v=f.value.trim();
          if(!v) return;
          var labelEl=form.querySelector('label[for="'+f.id+'"]');
          var label=labelEl?labelEl.textContent.trim():f.name;
          lines.push(label+': '+v);
        });
        var body=lines.join('\n')+'\n\nSent from '+location.href;
        window.location.href='mailto:'+email+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
      });
    });

    // Prefill inquiry product from URL param or data attributes
    var urlParams=new URLSearchParams(location.search);
    var wanted=(urlParams.get('product')||'').trim();
    var productSel=document.getElementById('product');
    if(wanted&&productSel){
      var wl=wanted.toLowerCase(),matched=false;
      productSel.querySelectorAll('option').forEach(function(opt){
        var txt=(opt.textContent||'').trim().toLowerCase();
        if(!matched&&(opt.value.toLowerCase()===wl||txt.indexOf(wl)>-1)){ productSel.value=opt.value; matched=true; }
      });
      if(!matched){ var o=document.createElement('option'); o.value=wanted; o.textContent=wanted; productSel.appendChild(o); productSel.value=wanted; }
    }
    document.querySelectorAll('[data-product-name]').forEach(function(el){
      if(productSel) productSel.value=el.getAttribute('data-product-name');
    });

    // Year in footer
    document.querySelectorAll('[data-year]').forEach(function(el){ el.textContent=new Date().getFullYear(); });
  });
})();
