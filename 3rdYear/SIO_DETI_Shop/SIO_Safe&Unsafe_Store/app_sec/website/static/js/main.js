/*==================== SHOW MENU ====================*/
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)

    // Validate that variables exist
    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            // We add the show-menu class to the div tag with the nav__menu class
            nav.classList.toggle('show-menu')
        })
    }
}
showMenu('nav-toggle', 'nav-menu')

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

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
/*==================== CHANGE BACKGROUND HEADER ====================*/
function scrollHeader() {
    const nav = document.getElementById('header')
    // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
    if (this.scrollY >= 200) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/*==================== SHOW SCROLL TOP ====================*/
function scrollTop() {
    const scrollTop = document.getElementById('scroll-top');
    // When the scroll is higher than 560 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if (this.scrollY >= 560) scrollTop.classList.add('show-scroll'); else scrollTop.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollTop)

/*==================== DARK LIGHT THEME ====================*/
const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'bx-sun'
const themeButtonlogo = document.getElementById('detishoplogo');
const lightLogoPath = '../static/img/detishoplogo.png';
const darkLogoPath = '../static/img/detishoplogodarker.png';

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx-moon' : 'bx-sun'

// Function to change the logo based on the theme
const changeLogoBasedOnTheme = () => {
    const currentTheme = getCurrentTheme();
    if (currentTheme === 'dark') {
        themeButtonlogo.src = darkLogoPath;
    } else {
        themeButtonlogo.src = lightLogoPath;
    }
};
// We validate if the user previously chose a topic
if (selectedTheme) {
    // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
    themeButton.classList[selectedIcon === 'bx-moon' ? 'add' : 'remove'](iconTheme)
    // Change logo on page load based on the selected theme
    changeLogoBasedOnTheme();
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
    // Add or remove the dark / icon theme
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)
    // Change logo based on the selected theme
    changeLogoBasedOnTheme();
    // We save the theme and the current icon that the user chose
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})

/*==================== SCROLL REVEAL ANIMATION ====================*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '30px',
    duration: 200,
    reset: true
});

sr.reveal(`.home__data, .home__img,
            .about__data, .about__img,
            .services__content, .menu__content,
            .app__data, .app__img,
            .contact__data, .contact__button,
            .footer__content`, {
    interval: 200
})

/*==================== Download Results ====================*/
function checkCode() {
    var codeInput = document.getElementById("code").value;
    var downloadBtnContainer = document.getElementById("download-btn-container");

    if (codeInput === "your_correct_code") {
        downloadBtnContainer.style.display = "block";
    } else {
        downloadBtnContainer.style.display = "none";
    }
}

/*==================== PRODUCT LIST SEARCHBAR ====================*/

function searchbar() {
    // Declare variables
    var input, filter, ul, div, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    div = ul.getElementsByTagName('div');

    // Loop through all div items, and hide those who don't match the search query
    for (i = 0; i < div.length; i++) {
        h3 = div[i].getElementsByTagName("h3")[0];
        txtValue = h3.textContent || h3.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "";
        } else {
            div[i].style.display = "none";
        }
    }
}

/*==================== PRODUCT LIST FILTER ====================*/
// Initialize the page with "all" category selected
filterSelection("all");

function filterSelection(category) {
    var filterDivs = document.getElementsByClassName("filterDiv");

    for (var i = 0; i < filterDivs.length; i++) {
        var filterDiv = filterDivs[i];
        var categories = filterDiv.classList; // Get all classes of the current element

        if (category === "all" || categories.contains(category)) {
            filterDiv.style.display = "block";
        } else {
            filterDiv.style.display = "none";
        }
    }

    // Add the "active" class to the clicked button
    var buttons = document.getElementsByClassName("btn");
    for (var j = 0; j < buttons.length; j++) {
        buttons[j].classList.remove("active");
    }
    document.querySelector('[data-category="' + category + '"]').classList.add("active");
}

/*==================== CHECKOUT ====================*/
// Show error message if wrong information is entered
var isCheckoutVisible = false;

function toggleCheckout() {
    var invalidCCPopup = document.getElementById("invalid-cc-popup");
    var requiredInfoPopup = document.getElementById("required-info-popup");

    var ccnum = document.getElementById("ccnum").value;
    var cvv = document.getElementById("cvv").value;
    var cname = document.getElementById("cname").value;
    var expyear = document.getElementById("expyear").value;


    // Check if the information is valid


    // Hide the popup if the info validates
    if (isValidCreditCardNumber(ccnum) && cvv.length === 3 && cname.trim() !== "" && expyear !== "" && expyear >= 2023) {
        invalidCCPopup.style.display = "none";
    } else {
        invalidCCPopup.style.display = "block";
    }

    if (requiredFields()) {
        requiredInfoPopup.style.display = "none";
    } else {
        requiredInfoPopup.style.display = "block";
    }
    //Print the receipt if all the info is correct
    if (isValidCreditCardNumber(ccnum) && cvv.length === 3 && cname.trim() !== "" && expyear !== "" && expyear >= 2023 && requiredFields()) {
        openReceiptPopup();
    }
    isCheckoutVisible = !isCheckoutVisible;
}

// Function to check if the credit card number is in the correct format.
function isValidCreditCardNumber(ccnum) {

    var regex = /^(?:\d{4}-){3}\d{4}$/;

    return regex.test(ccnum);
}

//Function to check if the required fields are filled

function requiredFields() {
    var name = document.getElementById("fname").value;
    var email = document.getElementById("email").value;

    // Check if name and email are empty or contain only whitespace
    if (name.trim() === "") {
        return false;
    }
    // Check if there are numbers in the full name
    if (/\d/.test(name)) {
        return false;
    }
    // Check if the email ends with @gmail.com or @hotmail.com
    if (!/(@gmail\.com|@hotmail\.com|@asd\.com|@ua\.pt)$/.test(email)) {
        return false;
    }

    return true;
}
// Format the credit card number as the user types it.
function formatCreditCard() {
    const creditCardInput = document.getElementById('ccnum');
    let value = creditCardInput.value.replace(/\s|-/g, ''); // Remove existing spaces and hyphens
    let formattedValue = '';

    for (let i = 0; i < value.length; i++) {
        if (i > 0 && i % 4 === 0) {
            formattedValue += '-';
        }
        formattedValue += value[i];
    }

    creditCardInput.value = formattedValue;
}

// Function to format the credit card number from the database
function formatCreditCardFromDatabase() {
    const formattedCreditCardInput = document.getElementById('formatted_ccnum');
    // Use the formatCreditCard function to format the credit card number
    formattedCreditCardInput.value = formatCreditCard(formattedCreditCardInput.value);
}
// Function to open the popup and display the receipt
function openReceiptPopup() {
    const popup = document.getElementById('popup-container');
    popup.style.display = 'block';
    displayReceipt();
}

// Function to close the popup
function closeReceiptPopup() {
    const popup = document.getElementById('popup-container');
    popup.style.display = 'none';

    // Redirect to the orders page
    window.location.href = "/orders";
}

// Function to display the receipt
function displayReceipt() {
    openReceiptPopup();
}