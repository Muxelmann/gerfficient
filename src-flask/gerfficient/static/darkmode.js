let colorSchemeStored = localStorage.getItem('color-scheme');
let colorSchemeCurrent = document.querySelector('meta[name="color-scheme"]');
let colorSchemeToggle = document.querySelector('#dark-mode-toggle');

switch (colorSchemeStored) {
    case 'dark':
        colorSchemeCurrent.setAttribute('content', 'dark');
        document.body.classList.add('dark')
        break;
    default:
        colorSchemeCurrent.setAttribute('content', 'light');
        document.body.classList.add('light')
        break;
}

function toggleColorScheme() {
    if (document.body.classList.toggle('dark')) {
        localStorage.setItem('color-scheme', 'dark');
        colorSchemeCurrent.setAttribute('content', 'dark');
    } else {
        localStorage.setItem('color-scheme', 'light');
        colorSchemeCurrent.setAttribute('content', 'light');
    }
}

colorSchemeToggle.addEventListener('click', toggleColorScheme);