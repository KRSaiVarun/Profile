/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')
function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*==================== SMOOTH SCROLL ====================*/
navLink.forEach(link => {
    link.addEventListener("click", e => {
        e.preventDefault();
        document.querySelector(link.getAttribute("href"))
          .scrollIntoView({ behavior: "smooth" });
    });
});

/*==================== ACTIVE LINK ON SCROLL ====================*/
const sections = document.querySelectorAll("section[id]");
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        // quote the attribute value to make a valid selector and guard if no matching nav item
        const navItem = document.querySelector(`.nav__menu a[href*="${entry.target.id}"]`);
        if (!navItem) return;
        if(entry.isIntersecting){
            navItem.classList.add("active");
        } else {
            navItem.classList.remove("active");
        }
    });
}, { threshold: 0.6 });

sections.forEach(sec => observer.observe(sec));

/*===== THEME: DARK MODE + COLOR PALETTE =====*/
const navEl = document.querySelector('.nav');
const palettePanel = document.createElement('div');
palettePanel.className = 'theme-panel';
palettePanel.setAttribute('aria-hidden', 'true');
// no static label — keep the panel empty and append controls below
palettePanel.innerHTML = '';
navEl.appendChild(palettePanel);

// --- Hue slider for continuous selection ---
const hueWrapper = document.createElement('div');
hueWrapper.className = 'theme-hue-wrapper';
// compute initial hue from CSS variable, fall back to 220
let initialHue = getComputedStyle(document.documentElement).getPropertyValue('--hue-color').trim();
initialHue = initialHue ? Number(initialHue) : 220;
if (Number.isNaN(initialHue)) initialHue = 220;
hueWrapper.innerHTML = `
    <input type="range" min="0" max="360" value="${initialHue}" class="theme-hue-slider" aria-label="Primary color hue">
`;
palettePanel.appendChild(hueWrapper);

// Update swatch preview function
function updateSwatch(hue){
    const swatch = document.querySelector('.color-swatch');
    if(swatch) swatch.style.background = `hsl(${hue}, 89%, 60%)`;
}

const hueSlider = hueWrapper.querySelector('.theme-hue-slider');
// apply hue live
hueSlider.addEventListener('input', (e) => {
    const hue = e.target.value;
    setHue(hue);
    localStorage.setItem('selected-hue', String(hue));
    updateSwatch(hue);
    debouncedHueToast(hue);
});

const colorPresets = [
    { name: 'Blue', hue: 224 },
    { name: 'Purple', hue: 260 },
    { name: 'Red', hue: 355 },
    { name: 'Green', hue: 140 },
    { name: 'Orange', hue: 30 }
];

colorPresets.forEach(p => {
    const btn = document.createElement('button');
    btn.className = 'theme-color-btn';
    btn.title = p.name;
    btn.dataset.hue = p.hue;
    btn.style.background = `hsl(${p.hue}, 89%, 60%)`;
    palettePanel.appendChild(btn);
    btn.addEventListener('click', () => {
        setHue(p.hue);
        localStorage.setItem('selected-hue', String(p.hue));
        // close panel after select
        togglePalette(false);
        updateSwatch(p.hue);
        showToast('Theme color saved');
    });
});

// helper to set CSS variable for hue
function setHue(hue) {
    document.documentElement.style.setProperty('--hue-color', hue);
}

// Toast helper utilities
function ensureToastContainer(){
    let container = document.querySelector('.toast-container');
    if(!container){
        container = document.createElement('div');
        container.className = 'toast-container';
        document.body.appendChild(container);
    }
    return container;
}

function showToast(message){
    const container = ensureToastContainer();
    const t = document.createElement('div');
    t.className = 'toast';
    t.textContent = message;
    container.appendChild(t);
    setTimeout(()=>{
        t.style.opacity = '0';
        t.style.transform = 'translateY(6px) scale(.98)';
        setTimeout(()=> t.remove(), 300);
    }, 3000);
}

function debounce(fn, wait){
    let h;
    return function(...args){
        clearTimeout(h);
        h = setTimeout(()=> fn.apply(this,args), wait);
    }
}

// toggle palette visibility
function togglePalette(show) {
    const isShow = typeof show === 'boolean' ? show : palettePanel.classList.toggle('open') && true;
    if(isShow) {
        palettePanel.classList.add('open');
        palettePanel.setAttribute('aria-hidden', 'false');
        const openBtn = document.getElementById('palette-open');
        if(openBtn){ openBtn.setAttribute('aria-expanded','true'); }
    } else {
        palettePanel.classList.remove('open');
        palettePanel.setAttribute('aria-hidden', 'true');
        const openBtn = document.getElementById('palette-open');
        if(openBtn){ openBtn.setAttribute('aria-expanded','false'); }
    }
}

// close palette when clicking outside (click outside panel closes it)
document.addEventListener('click', (e) => {
    if(!palettePanel.contains(e.target)){
        togglePalette(false);
    }
});

// Open palette when palette-open button clicked
const paletteOpenBtn = document.getElementById('palette-open');
if(paletteOpenBtn){
    paletteOpenBtn.addEventListener('click', (e)=>{
        e.stopPropagation();
        togglePalette();
        // focus the first control inside the panel
        const firstControl = palettePanel.querySelector('button, input');
        if(firstControl) firstControl.focus();
    });
}

// Keyboard shortcuts: T toggles theme, Escape closes palette
document.addEventListener('keydown', (e)=>{
    if(e.key === 'T' || e.key === 't'){
        document.body.classList.toggle(darkTheme);
        const accessibleBtn = document.getElementById('theme-accessible');
        if(accessibleBtn) accessibleBtn.setAttribute('aria-pressed', document.body.classList.contains(darkTheme) ? 'true' : 'false');
        localStorage.setItem('selected-theme', document.body.classList.contains(darkTheme) ? 'dark' : 'light');
        showToast(document.body.classList.contains(darkTheme) ? 'Dark theme enabled' : 'Light theme enabled');
    }
    if(e.key === 'Escape'){
        togglePalette(false);
        paletteOpenBtn && paletteOpenBtn.focus();
    }
});

const darkTheme = 'dark-theme';
const iconSun = 'bx-sun';

// Load saved theme & hue
const savedTheme = localStorage.getItem('selected-theme');
const savedHue = localStorage.getItem('selected-hue');
if(savedHue){
    setHue(savedHue);
    // update slider if present
    if(hueSlider) hueSlider.value = savedHue;
    updateSwatch(savedHue);
}

// prepare debounced toast for hue slider
const debouncedHueToast = debounce((hue)=> showToast('Theme color saved'), 600);
if(savedTheme === 'dark'){
    document.body.classList.add(darkTheme);
}

// Accessible visible toggle
const accessibleBtn = document.getElementById('theme-accessible');
if(accessibleBtn){
    accessibleBtn.addEventListener('click', () => {
        document.body.classList.toggle(darkTheme);
        const isDark = document.body.classList.contains(darkTheme);
        localStorage.setItem('selected-theme', isDark ? 'dark' : 'light');
        accessibleBtn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
        showToast(isDark ? 'Dark theme enabled' : 'Light theme enabled');
    });
    // initialize aria state
    accessibleBtn.setAttribute('aria-pressed', document.body.classList.contains(darkTheme) ? 'true' : 'false');
}

// Make palette appear inside mobile menu when menu opens (for small screens)
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');
if(navToggle && navMenu){
    // move palette into nav menu for small screens
    window.addEventListener('resize', placePalette);
    placePalette();

    function placePalette(){
        if(window.innerWidth <= 767){
            // append to nav-menu and show inline
            if(!navMenu.contains(palettePanel)) navMenu.appendChild(palettePanel);
        } else {
            if(!navEl.contains(palettePanel)) navEl.appendChild(palettePanel);
        }
    }
}

/*===== CONTACT FORM VALIDATION =====*/
// In the EmailJS init:
emailjs.init("YOUR_PUBLIC_KEY_HERE");

// In the sendForm function:
const contactForm = document.querySelector(".contact__form");
if(contactForm){
    contactForm.addEventListener("submit", function(e) {
        e.preventDefault();
        emailjs.sendForm(
          'YOUR_SERVICE_ID',     // Your EmailJS Service ID
          'YOUR_TEMPLATE_ID',    // Your EmailJS Template ID
          this
        ).then(function() {
            showToast('Message sent successfully!');
            contactForm.reset();
        }, function(error) {
            showToast('Message failed to send. Please try again.');
        });
    });
}

/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2000,
    delay: 200,
});
sr.reveal('.home__data, .about__img, .skills__subtitle, .skills__text',{}); 
sr.reveal('.home__img, .about__subtitle, .about__text, .skills__img',{delay: 400}); 
sr.reveal('.home__social-icon',{ interval: 200}); 
sr.reveal('.skills__data, .work__item, .contact__input',{interval: 200}); 
