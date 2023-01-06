// DOM elements

const time= document.getElementById('time')
const greeting=document.getElementById('greeting')
const name=document.getElementById('name')
const focus=document.getElementById('focus')


// function to show the time

function showTime(){
    let today=new Date()
    let hour=today.getHours()
    hour+1;
    let min=today.getMinutes()


// set AM or PM
const amPm=hour>=12 ? 'PM' : 'AM';



// time output
time.innerHTML=`${hour}<span>:</span>${addZero(min)}`;

setTimeout(showTime, 1000);
}

// add zero
function addZero(n){
    return(parseInt(n,10) < 10 ? '0' : '')+n;
}






// setting the background and greeting
function BgGreet(){
    let today=new Date();
    let hour =today.getHours();


if( hour<12){
    // its morning
    document.body.style.backgroundImage= "url('../img/morning.jpeg')";
    greeting.textContent="Good Morning"
}
else if(hour<19){
    // afternoon
    document.body.style.backgroundImage= "url('../img/afternoon.jpeg')";
    greeting.textContent="Good afternoon"

}
else{
// it's night
document.body.style.backgroundImage= "url('../img/night.jpeg')";
    greeting.textContent="Good night"
}

}

//  running the function
showTime()
BgGreet()