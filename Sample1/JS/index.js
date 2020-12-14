import highway from '@dogstudio/highway';
import Highway from '@dogstudio/highway';
import Fade from './transition';


const H = new Highway.Core({
  transitions: {
    default: Fade
  }
});




// const text = ['Nikhil\ Abraham','Neha\ Cathrin','Nishchal\ Nandagopal','Abhinav\ Atla'];
// let count = 0;
// let index = 0;
// let currentText = '';
// let letter = '';


// const run = () =>{
//   console.log("its rnning");
// };





// (function type(){
//   if(count === text.length){
//     count = 0;
//   }
//   currentText = text[count];
//   letter = currentText.slice(0,++index);

//   document.querySelector('.typing').textContent = letter;
//   if(letter.length === currentText.length){
//     count++;
//     index = 0;
//   }

//   setTimeout(type, 300);

// }())


// const glass = document.getElementById('glass');
// const tl = gsap.timeline({ defaults: { ease: "power2.inOut", duration: 2.5 } })

// tl.from('img', { x: '-10%', opacity: 0 })
//   .from('.container', { opacity: 0, delay: .5, duration: 1 }, "-=2.5")


