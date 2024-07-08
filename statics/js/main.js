// creating variables
const formModal = document.getElementById('form-modal')
const cancelbtn = document.getElementById('cancel-btn') 
const openModalBtn = document.getElementById('open-modal-btn')
const backdrop = document.getElementById('backdrop')


// printing the variables
console.log(formModal)
console.log(cancelbtn)
console.log(backdrop)



// functions
openModalBtn.addEventListener('click', ()=> {
    formModal.classList.remove('hidden')
})

cancelbtn.addEventListener('click' , ()=> {
    formModal.classList.add('hidden')
})

formModal.addEventListener('click',(e)=>{
    if (e.target !== backdrop) return;
    console.log(e.target)
    formModal.classList.add('hidden')
})


