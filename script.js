//Nav-Fixed
    window.onscroll = function () {
        const header = document.querySelector('header');
        const  fixedNav = header.offsetTop;

        if(window.pageYOffset > fixedNav) {
            header.classList.add('navbar-fixed');
        } else {
            header.classList.remove('navbar-fixed');
        }
    };
//Hamburger
const hamburger = document.querySelector('#hamburger');
const navdropdown = document.querySelector('#nav-dropdown');

hamburger.addEventListener('click', function () {
    hamburger.classList.toggle('ham-active');
    navdropdown.classList.toggle('hidden');
});