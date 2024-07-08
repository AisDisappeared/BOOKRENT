const head = document.getElementById('head');

if (head) {
    const backBtn = document.getElementById('go-back-btn')
    backBtn?.addEventListener('click' , ()=> history.back())
}
