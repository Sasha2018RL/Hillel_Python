window.onload = ()=>{
    const clock = document.getElementById('live_clock')
    if(clock){
        const diff = Math.round(new Date().getTime()/1000) - Math.round(new Date(clock.innerText, ).getTime()/1000)
        console.log(diff)
        setInterval(()=>{
            clock.innerText = moment(new Date().getTime() + diff).format('YYYY/MM/DD HH:mm:ss')
        }, 1000)
    }
}
