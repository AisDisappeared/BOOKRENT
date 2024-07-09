const head = document.getElementById('head');

if (head) {
    const backBtn = document.getElementById('go-back-btn')
    backBtn?.addEventListener('click' , ()=> history.back())
}


const copyBtnBox = document.getElementById('copy-box-btn')
const bookIDforCopy = document.getElementById('book-copy-box')

copyBtnBox.addEventListener('click', ()=>{
    const bookID = bookIDforCopy.textContent; 
    navigator.clipboard.writeText(bookID).then(()=> {
        copyBtnBox.innerHTML = "<p>copied!</p>"
    })
})