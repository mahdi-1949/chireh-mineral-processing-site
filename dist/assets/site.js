
document.documentElement.classList.add("js-ready");
document.body.classList.add("has-motion");

(function(){
  var toggle=document.querySelector(".menu-toggle");
  var nav=document.querySelector(".primary-nav");
  if(toggle&&nav){
    toggle.addEventListener("click",function(){
      var open=toggle.getAttribute("aria-expanded")==="true";
      toggle.setAttribute("aria-expanded",String(!open));
      nav.classList.toggle("is-open",!open);
      toggle.setAttribute("aria-label",open?"بازکردن فهرست":"بستن فهرست");
    });
    nav.querySelectorAll("a").forEach(function(link){
      link.addEventListener("click",function(){
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded","false");
        toggle.setAttribute("aria-label","بازکردن فهرست");
      });
    });
    document.addEventListener("keydown",function(event){
      if(event.key==="Escape"){
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded","false");
        document.querySelectorAll(".nav-products[open]").forEach(function(el){el.removeAttribute("open");});
      }
    });
  }

  var path=window.location.pathname;
  var navSection=path.indexOf("/products")===0?"products":
    path.indexOf("/services")===0?"services":
    path.indexOf("/articles")===0?"articles":
    path.indexOf("/about")===0?"about":
    path.indexOf("/contact")===0?"contact":
    path.indexOf("/faq")===0?"faq":"home";
  var activeLink=document.querySelector('[data-nav="'+navSection+'"]');
  if(activeLink&&activeLink.tagName==="A"){activeLink.setAttribute("aria-current","page");}
  if(navSection==="products"){
    var productSummary=document.querySelector(".nav-products>summary");
    if(productSummary){productSummary.setAttribute("aria-current","page");}
  }

  var search=document.getElementById("product-search");
  var cards=Array.prototype.slice.call(document.querySelectorAll("[data-product-card]"));
  var chips=Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
  var count=document.getElementById("catalog-count");
  var empty=document.getElementById("empty-products");
  var activeCategory="all";
  var params=new URLSearchParams(window.location.search);
  if(search&&cards.length){
    var initialQuery=params.get("q")||"";
    var initialCategory=params.get("category")||"all";
    search.value=initialQuery;
    if(chips.some(function(chip){return chip.dataset.filter===initialCategory;})){activeCategory=initialCategory;}
    function filterCards(){
      var query=search.value.trim().toLocaleLowerCase("fa-IR");
      var visible=0;
      cards.forEach(function(card){
        var matchesText=card.textContent.toLocaleLowerCase("fa-IR").indexOf(query)!==-1;
        var matchesCategory=activeCategory==="all"||card.dataset.category===activeCategory;
        var show=matchesText&&matchesCategory;
        card.hidden=!show;
        if(show){visible+=1;}
      });
      if(count){count.textContent=visible.toLocaleString("fa-IR")+" تجهیز نمایش داده می‌شود";}
      if(empty){empty.hidden=visible!==0;}
      chips.forEach(function(chip){
        var active=chip.dataset.filter===activeCategory;
        chip.classList.toggle("is-active",active);
        chip.setAttribute("aria-pressed",String(active));
      });
    }
    chips.forEach(function(chip){
      chip.addEventListener("click",function(){
        activeCategory=chip.dataset.filter;
        filterCards();
      });
    });
    search.addEventListener("input",filterCards);
    filterCards();
  }

  var productInput=document.getElementById("contact-product");
  var productParam=params.get("product");
  if(productInput&&productParam){productInput.value=productParam;}
  var subjectParam=params.get("subject");
  var subjectSelect=document.getElementById("contact-subject");
  if(subjectSelect&&subjectParam){
    Array.prototype.slice.call(subjectSelect.options).forEach(function(option){
      if(option.textContent.indexOf(subjectParam)!==-1){subjectSelect.value=option.value;}
    });
  }

  var form=document.getElementById("contact-form");
  if(form){
    form.addEventListener("submit",function(event){
      event.preventDefault();
      if(!form.reportValidity()){return;}
      var data=new FormData(form);
      var subject=String(data.get("subject")||"درخواست از وب‌سایت");
      var body=[
        "نام: "+String(data.get("name")||""),
        "شماره تماس: "+String(data.get("phone")||""),
        "ایمیل: "+String(data.get("email")||""),
        "محصول: "+String(data.get("product")||""),
        "",
        "پیام:",
        String(data.get("message")||"")
      ].join("\n");
      var link="mailto:sales@chirehfg.com?subject="+encodeURIComponent(subject)+"&body="+encodeURIComponent(body);
      var status=document.getElementById("form-status");
      if(status){status.textContent="پیام آماده شد. برای ارسال، نرم‌افزار ایمیل خود را تأیید کنید.";}
      window.location.href=link;
    });
  }

  var year=document.getElementById("current-year");
  if(year){year.textContent=new Date().getFullYear().toLocaleString("fa-IR");}

  if("IntersectionObserver" in window&&!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){entry.target.classList.add("is-visible");observer.unobserve(entry.target);}
      });
    },{threshold:.12});
    document.querySelectorAll(".section-heading,.product-card,.article-card,.service-card,.showcase-step,[data-reveal]").forEach(function(el){
      el.setAttribute("data-reveal","");
      observer.observe(el);
    });
  }else{
    document.querySelectorAll("[data-reveal]").forEach(function(el){el.classList.add("is-visible");});
  }
})();
