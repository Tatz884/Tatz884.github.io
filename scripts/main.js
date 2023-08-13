const header = document.querySelector('[aria-controls]');
const navButton = document.querySelector('.menu-button');
const nav = document.querySelector('nav')

function toggleNav() {
  const expanded = header.getAttribute('aria-expanded') === 'true' || false;
  header.setAttribute('aria-expanded', !expanded);
  if (!nav.classList.contains('active')) {
    setTimeout(() => nav.classList.add('active'), 200)
  } else {
    nav.classList.remove('active')
  }
}

navButton.addEventListener('click', toggleNav);