const toggleBtn = document.getElementById('navbarAddBtn');
const toggleIcon = document.getElementById('addIcon');

toggleBtn.addEventListener('click', () => {
    toggleIcon.classList.toggle('fa-bars');
    toggleIcon.classList.toggle('fa-x');
});
