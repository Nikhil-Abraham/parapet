const form = document.getElementById("form");

console.log("JS RUNNING");


function validate(){
  var email=document.getElementById("email").value.trim();
  var password=document.getElementById("password").value.trim();
  var flag1=0;
  var flag2=0;

  if(email.length<5){
    document.getElementById("email").style.border="1px solid red";
    document.getElementById("email").placeholder="invalid username";
    console.log("Email-Error!");
    flag1 = 0;
  }
  else{
    console.log("Email-Correct");
    document.getElementById("email").style.border="1px solid green";
    document.getElementById("email").placeholder="";
    flag1 = 1;
  }
  if(password.length <4){
    document.getElementById("password").style.border="1px solid red";
    document.getElementById("password").placeholder="invalid password";
    console.log("Pass-Error!")
    flag2 = 0;
  }
  else{
    document.getElementById("password").style.border="1px solid green";
    document.getElementById("password").placeholder="";
    console.log("Pass-Correct!");
    flag2 = 1;
  }

  if(flag1+flag2 == 2){
    return true;
  } 
  else{
    return false;
  }
}