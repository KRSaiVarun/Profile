/* Updated main.js — cleaned, resilient to missing elements, and dark theme friendly.
   Replaces your previous main.js file. */

// ============ SHOW MENU (Mobile) ============ //
const navMenu = document.getElementById("nav-menu"),
      navToggle = document.getElementById("nav-toggle"),
      navClose = document.getElementById("nav-close");

if(navToggle){
  navToggle.addEventListener("click", ()=>{
    navMenu?.classList.add("show");
  });
}

if(navClose){
  navClose.addEventListener("click", ()=>{
    navMenu?.classList.remove("show");
  });
}

// ============ REMOVE MENU MOBILE ============ //
const navLinks = document.querySelectorAll(".nav__link");

navLinks.forEach(n => n.addEventListener("click", ()=>{
  navMenu?.classList.remove("show");
}));

// ============ SCROLL SECTIONS ACTIVE LINK ============ //
const sections = document.querySelectorAll("section[id]");

function scrollActive(){
  const scrollY = window.pageYOffset;
  sections.forEach(current =>{
    const sectionHeight = current.offsetHeight,
          sectionTop = current.offsetTop - 50,
          sectionId = current.getAttribute("id"),
          link = document.querySelector('.nav__menu a[href*=' + sectionId + ']');
    if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
      link?.classList.add("active");
    }else{
      link?.classList.remove("active");
    }
  });
}
window.addEventListener("scroll", scrollActive);

// ============ CHANGE BACKGROUND HEADER ON SCROLL ============ //
function scrollHeader(){
  const header = document.getElementById("header");
  if(window.scrollY >= 80) header?.classList.add("scroll-header");
  else header?.classList.remove("scroll-header");
}
window.addEventListener("scroll", scrollHeader);

// ============ SHOW SCROLL TOP BUTTON ============ //
function scrollTop(){
  const scrollTop = document.getElementById("scroll-top");
  if(window.scrollY >= 560) scrollTop?.classList.add("show-scroll");
  else scrollTop?.classList.remove("show-scroll");
}
window.addEventListener("scroll", scrollTop);

// ============ THEME / PALETTE HANDLING ============ //
const palettePanel = document.getElementById("palette-panel");
const paletteOpen = document.getElementById("palette-open");
const paletteClose = document.getElementById("palette-close");
const colorSwatches = document.querySelectorAll(".color-swatch");

// open/close panel if elements exist
paletteOpen?.addEventListener("click", ()=>{
  palettePanel?.classList.add("open");
});
paletteClose?.addEventListener("click", ()=>{
  palettePanel?.classList.remove("open");
});

// set hue color when swatch clicked
colorSwatches.forEach(swatch =>{
  swatch.addEventListener("click", ()=>{
    const hue = swatch.dataset.hue;
    if(hue){
      document.documentElement.style.setProperty("--hue-color", hue);
      localStorage.setItem("selected-hue", hue);
    }
  });
});

// restore saved hue
const savedHue = localStorage.getItem("selected-hue");
if(savedHue){
  document.documentElement.style.setProperty("--hue-color", savedHue);
}

// ============ SCROLL REVEAL (optional, check availability) ============ //
if(typeof ScrollReveal !== "undefined"){
  const sr = ScrollReveal({origin:"top",distance:"40px",duration:800,delay:200});
  sr.reveal(".home__data, .about__img, .skills__data, .work__item, .contact__form",{interval:150});
}

// ============ Typing effect (optional if Typed.js loaded) ============ //
if(typeof Typed !== "undefined"){
  const typedElement = document.getElementById("typed-text");
  if(typedElement){
    new Typed("#typed-text", {
      strings: ["Developer", "Designer", "Freelancer"],
      typeSpeed: 80,
      backSpeed: 50,
      backDelay: 2000,
      loop: true,
    });
  }
}
