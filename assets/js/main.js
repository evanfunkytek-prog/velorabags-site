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

    // Inquiry forms: POST to a real endpoint; fall back to email so no lead is lost
    var SKIP_FIELDS=['_gotcha','_subject','_next'];
    function fieldLines(form){
      var lines=[];
      form.querySelectorAll('[name]').forEach(function(f){
        if(SKIP_FIELDS.indexOf(f.name)>-1) return;
        var v=(f.value||'').trim();
        if(!v) return;
        var labelEl=f.id?form.querySelector('label[for="'+f.id+'"]'):null;
        lines.push((labelEl?labelEl.textContent.trim():f.name)+': '+v);
      });
      return lines;
    }
    function setStatus(form,kind,html){
      var box=form.querySelector('.form-status');
      if(!box) return;
      box.className='form-status'+(kind?' is-'+kind:'');
      box.innerHTML=html;
      box.hidden=false;
    }
    function mailtoFallback(form,note){
      var email=form.getAttribute('data-mailto');
      var subject=form.getAttribute('data-subject')||'RFQ from website';
      var lines=fieldLines(form);
      if(!lines.length) return;
      var body=lines.join('\n')+'\n\nSent from '+location.href;
      window.location.href='mailto:'+email+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
      setStatus(form,'error',note+' You can also email <a href="mailto:'+email+'">'+email+'</a> directly.');
    }
    document.querySelectorAll('form[data-mailto]').forEach(function(form){
      form.addEventListener('submit',function(ev){
        ev.preventDefault();
        var trap=form.querySelector('[name="_gotcha"]');
        if(trap&&trap.value) return;
        var lines=fieldLines(form);
        if(!lines.length){ setStatus(form,'error','Please fill in the required fields before sending.'); return; }
        var btn=form.querySelector('button[type=submit]');
        var btnText=btn?btn.textContent:'';
        var endpoint=form.getAttribute('data-endpoint');
        if(!endpoint){
          mailtoFallback(form,'Your email app should now open with the request ready to send.');
          return;
        }
        var payload={subject:form.getAttribute('data-subject')||'RFQ from website',
                     fields:{}, message:lines.join('\n'), page:location.href,
                     referrer:document.referrer||'', sentAt:new Date().toISOString()};
        form.querySelectorAll('[name]').forEach(function(f){
          if(SKIP_FIELDS.indexOf(f.name)>-1) return;
          if((f.value||'').trim()) payload.fields[f.name]=f.value.trim();
        });
        setStatus(form,'','Sending…');
        if(btn){ btn.disabled=true; btn.textContent='Sending…'; }
        form.classList.add('is-sending');
        var done=function(ok,note){
          form.classList.remove('is-sending');
          if(btn){ btn.disabled=false; btn.textContent=btnText; }
          if(ok){
            form.reset();
            setStatus(form,'ok',note);
          } else {
            mailtoFallback(form,note);
          }
        };
        fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/json'},
                        body:JSON.stringify(payload)})
          .then(function(r){ return r.ok?r.json().catch(function(){return {}}):Promise.reject(new Error('HTTP '+r.status)); })
          .then(function(){ done(true,'Thanks — your request is in. We reply within one business day, usually with a few questions that sharpen the quote.'); })
          .catch(function(){ done(false,'We could not send that automatically.'); });
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
