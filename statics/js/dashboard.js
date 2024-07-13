console.log('helllllooooo ali')

const dashboardBox = document.getElementById('dashboard-box')


$.ajax({
    type: 'GET',
    url: '/chart-data/',
    success: (resp) => {
        const { msg } = resp 
        console.log(msg)
        dashboardBox.innerHTML =`<b>${msg}</b>`
    },
    error: (err) => console.log(err)
})