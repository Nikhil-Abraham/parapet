const form = document.getElementById("form");

console.log("JS RUNNING");



// form.addEventListener('submit', (e) => {
//   e.preventDefault();
//   validate();
// })


function validate(){
  var email=document.getElementById("email").value.trim();
  var password=document.getElementById("password").value.trim();
  var email_error=document.getElementById("email_error");
  var password_error=document.getElementById("password_error");
  var flag=0;
  console.log("Flag3");

  if(email.length<9){
    email_error.style.display="block";
    console.log("Email-Error!");
    flag = 0;
  }
  else{
    email_error.style.display="none";
    console.log("Email-Correct");
    flag = 1;
  }
  if(password.length <6){
    password_error.style.display="block";
    console.log("Pass-Error!")
    flag = 0;
  }
  else{
    password_error.style.display="none";
    console.log("Pass-Correct!");
    flag = 1;
  }

  if(flag){
    return true;
  } 
  else{
    return false;
  }
}