function validate(){
  var email=document.getElementById("email").value;
  var password=document.getElementById("password").value;
  var email_error=document.getElementById("email_error");
  var password_error=document.getElementById("password_error");

  if(email.length<9){
    email.style.border="1px solid red";
    email_error.style.display="block";
    email.focus();
    alert("invalid email");
  }
  else{
    email.style.border="1px solid grey";
    email_error.style.display="none";
    email.focus();

  }
  if(password.value.length <6){
    password.style.border="1px solid red";
    password_error.style.display="block";
    password.focus();
    alert("invalid password");
    
  }
  else
  {
  password.style.border="1px solid grey";
  password_error.style.display="none";
  password.focus();

  
  }
}