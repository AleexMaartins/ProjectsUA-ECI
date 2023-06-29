/*==================== SHOW MENU ====================*/
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if (navToggle) {
  navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu');
  });
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if (navClose) {
  navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu');
  });
}

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link');

function linkAction() {
  const navMenu = document.getElementById('nav-menu');
  // When we click on each nav__link, we remove the show-menu class
  navMenu.classList.remove('show-menu');
}
navLink.forEach(n => n.addEventListener('click', linkAction));

/*==================== CHANGE BACKGROUND HEADER ====================*/
function scrollHeader() {
  const header = document.getElementById('header');
  // When the scroll is greater than 100 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 100) {
    header.classList.add('scroll-header');
  } else {
    header.classList.remove('scroll-header');
  }
}
window.addEventListener('scroll', scrollHeader);

/*==================== SWIPER DISCOVER ====================*/
let swiper = new Swiper(".discover__container", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  loop: true,
  spaceBetween: 32,
  coverflowEffect: {
    rotate: 0,
  },
});

/*==================== VIDEO ====================*/
const videoFile = document.getElementById('video-file');
const videoButton = document.getElementById('video-button');
const videoIcon = document.getElementById('video-icon');

function playPause() {
  if (videoFile.paused) {
    // Play video
    videoFile.play();
    // We change the icon
    videoIcon.classList.add('ri-pause-line');
    videoIcon.classList.remove('ri-play-line');
  } else {
    // Pause video
    videoFile.pause();
    // We change the icon
    videoIcon.classList.remove('ri-pause-line');
    videoIcon.classList.add('ri-play-line');
  }
}
videoButton.addEventListener('click', playPause);

function finalVideo() {
  // Video ends, icon change
  videoIcon.classList.remove('ri-pause-line');
  videoIcon.classList.add('ri-play-line');
}
// ended, when the video ends
videoFile.addEventListener('ended', finalVideo);

/*==================== SHOW SCROLL UP ====================*/
function scrollUp() {
  const scrollUp = document.getElementById('scroll-up');
  // When the scroll is higher than 200 viewport height, add the show-scroll class to the a tag with the scroll-top class
  if (this.scrollY >= 200) {
    scrollUp.classList.add('show-scroll');
  } else {
    scrollUp.classList.remove('show-scroll');
  }
}
window.addEventListener('scroll', scrollUp);

/*==================== SCROLL SECTIONS ACTIVE LINK ====================*/
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__menu a');

function scrollActive() {
  const scrollY = window.pageYOffset;

  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 50;
    sectionId = current.getAttribute('id');

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      navLinks.forEach(link => {
        link.classList.remove('active-link');
        if (link.getAttribute('href') === '#' + sectionId) {
          link.classList.add('active-link');
        }
      });
    } else {
      navLinks.forEach(link => {
        if (link.getAttribute('href') === '#' + sectionId) {
          link.classList.remove('active-link');
        }
      });
    }
  });
}
window.addEventListener('scroll', scrollActive);

/*==================== SCROLL REVEAL ANIMATION ====================*/
const sr = ScrollReveal({
  distance: '60px',
  duration: 600,
  // reset: true,
});

sr.reveal(`.home__data, .home__social-link, .home__info,
           .discover__container,
           .experience__data, .experience__overlay,
           .place__card,
           .sponsor__content,
           .footer__data, .footer__rights`, {
  origin: 'top',
  interval: 100,
});

sr.reveal(`.about__data, 
           .video__description,
           .subscribe__description`, {
  origin: 'left',
});

sr.reveal(`.about__img-overlay, 
           .video__content,
           .subscribe__form`, {
  origin: 'right',
  interval: 100,
});

/*==================== DARK LIGHT THEME ====================*/
const themeButton = document.getElementById('theme-button');
const darkTheme = 'dark-theme';
const iconTheme = 'ri-sun-line';

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem('selected-theme');
const selectedIcon = localStorage.getItem('selected-icon');

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'ri-moon-line' : 'ri-sun-line';

// We validate if the user previously chose a topic
if (selectedTheme) {
  // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
  themeButton.classList[selectedIcon === 'ri-moon-line' ? 'add' : 'remove'](iconTheme);
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
  // Add or remove the dark / icon theme
  document.body.classList.toggle(darkTheme);
  themeButton.classList.toggle(iconTheme);
  // We save the theme and the current icon that the user chose
  localStorage.setItem('selected-theme', getCurrentTheme());
  localStorage.setItem('selected-icon', getCurrentIcon());
});

/*==================== voo/hotel menu ====================*/
function showSection(sectionId) {
  // Oculta todas as seções
  var sections = document.querySelectorAll('section[id^="section-"]');
  for (var i = 0; i < sections.length; i++) {
    sections[i].style.display = 'none';
  }

  // Exibe a seção selecionada
  var section = document.getElementById('section-' + sectionId);
  section.style.display = 'block';
}





//----------------------------------------------------------







// Função para exibir/ocultar o calendário
function toggleCalendar(inputId) {
  var input = document.getElementById(inputId);
  var dropdown = input.nextElementSibling;

  if (dropdown.style.display === "block") {
    dropdown.style.display = "none";
  } else {
    dropdown.style.display = "block";
  }
}

// Função para definir a data selecionada no campo de partida/chegada
function selectDate(inputId, day, month, year) {
  var input = document.getElementById(inputId);
  var formattedDate = `${day}/${month}/${year}`;
  input.value = formattedDate;

  // Oculta o calendário após a seleção da data
  toggleCalendar(inputId);
}

// Evento de clique no campo de partida para exibir/ocultar o calendário
document.getElementById("partida").addEventListener("click", function () {
  toggleCalendar("partida");
});

// Evento de clique no campo de chegada para exibir/ocultar o calendário
document.getElementById("chegada").addEventListener("click", function () {
  toggleCalendar("chegada");
});

document.getElementById("checkin").addEventListener("click", function () {
  toggleCalendar("checkin");
});

// Evento de clique no campo de chegada para exibir/ocultar o calendário
document.getElementById("checkout").addEventListener("click", function () {
  toggleCalendar("checkout");
});

document.getElementById("voohotelpartida").addEventListener("click", function () {
  toggleCalendar("voohotelpartida");
});

// Evento de clique no campo de chegada para exibir/ocultar o calendário
document.getElementById("voohotelchegada").addEventListener("click", function () {
  toggleCalendar("voohotelchegada");
});

document.getElementById("voohotelcheckin").addEventListener("click", function () {
  toggleCalendar("voohotelcheckin");
});

// Evento de clique no campo de chegada para exibir/ocultar o calendário
document.getElementById("voohotelcheckout").addEventListener("click", function () {
  toggleCalendar("voohotelcheckout");
});






// Evento de clique fora do calendário para ocultá-lo
document.addEventListener("click", function (event) {
  var dropdowns = document.getElementsByClassName("dropdown-calendar");
  var partidaInput = document.getElementById("partida");
  var chegadaInput = document.getElementById("chegada");
  var checkinInput = document.getElementById("checkin");
  var checkoutInput = document.getElementById("checkout");
  var voohotelpartidaInput = document.getElementById("voohotelpartida");
  var voohotelchegadaInput = document.getElementById("voohotelchegada");
  var voohotelcheckinInput = document.getElementById("voohotelcheckin");
  var voohotelcheckoutInput = document.getElementById("voohotelcheckout");

  for (var i = 0; i < dropdowns.length; i++) {
    var dropdown = dropdowns[i];
    if (!dropdown.contains(event.target) && event.target !== partidaInput && event.target !== chegadaInput && event.target !== checkinInput && event.target !== checkoutInput && event.target !== voohotelpartidaInput && event.target !== voohotelchegadaInput && event.target !== voohotelcheckinInput && event.target !== voohotelcheckoutInput) {
      dropdown.style.display = "none";
    }
  }
});

// Gera o calendário
function generateCalendar(calendarId, inputId) {
  var calendar = document.getElementById(calendarId);
  var currentDate = new Date();
  var currentMonth = currentDate.getMonth();
  var currentYear = currentDate.getFullYear();

  var months = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
  ];

  // Cabeçalho do calendário (mês e ano)
  var header = document.createElement("div");
  header.className = "calendar-header";
  header.innerHTML = `
    <button class="prev-btn" onclick="prevMonth('${calendarId}')">&lt;</button>
    <span class="month">${months[currentMonth]}</span>
    <span class="year">${currentYear}</span>
    <button class="next-btn" onclick="nextMonth('${calendarId}')">&gt;</button>
  `;
  calendar.appendChild(header);

  // Dias da semana
  var weekdays = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"];
  var weekdaysRow = document.createElement("div");
  weekdaysRow.className = "weekdays";
  weekdays.forEach(function (weekday) {
    var weekdayCell = document.createElement("div");
    weekdayCell.textContent = weekday;
    weekdaysRow.appendChild(weekdayCell);
  });
  calendar.appendChild(weekdaysRow);

  // Dias do mês
  var daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
  var firstDayOfWeek = new Date(currentYear, currentMonth, 1).getDay();
  var daysRow = document.createElement("div");
  daysRow.className = "days";

  // Células vazias para o início do mês
  for (var i = 0; i < firstDayOfWeek; i++) {
    var emptyCell = document.createElement("div");
    daysRow.appendChild(emptyCell);
  }

  // Células com os dias do mês
  for (var day = 1; day <= daysInMonth; day++) {
    var dayCell = document.createElement("div");
    dayCell.textContent = day;
    dayCell.addEventListener("click", selectDate.bind(null, inputId, day, currentMonth + 1, currentYear));
    daysRow.appendChild(dayCell);
  }

  calendar.appendChild(daysRow);
}

// Inicializa os calendários
generateCalendar("partida-calendar", "partida");
generateCalendar("chegada-calendar", "chegada");
generateCalendar("checkin-calendar", "checkin");
generateCalendar("checkout-calendar", "checkout");
generateCalendar("voohotelpartida-calendar", "voohotelpartida");
generateCalendar("voohotelchegada-calendar", "voohotelchegada");
generateCalendar("voohotelcheckin-calendar", "voohotelcheckin");
generateCalendar("voohotelcheckout-calendar", "voohotelcheckout");

