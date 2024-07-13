const btndropdown = document.getElementById('btn-dropdown')
const dropdownbox = document.getElementById('dropdown-box')
const dropdown = document.getElementById('dropdown')


btndropdown.addEventListener('click', ()=> {
    dropdown.classList.toggle('hidden')
    dropdown.classList.contains('hidden') ? 
        btndropdown.innerHTML = 'menu &nbsp; <i class="fa-solid fa-caret-down"></i>'
    :
        btndropdown.innerHTML = 'menu &nbsp; <i class="fa-solid fa-xmark"></i>'


})

dropdownbox.addEventListener('mouseleave',()=> {
    dropdown.classList.add('hidden')
    btndropdown.innerHTML = 'menu &nbsp; <i class="fa-solid fa-caret-down"></i>'

})