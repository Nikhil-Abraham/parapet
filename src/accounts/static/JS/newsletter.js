function newsletter() {
  var email = document.getElementById("email").value.trim();

  var regx_email = /^[a-zA-Z0-9.-]+@([a-zA-Z]+).([a-zA-Z]+)$/;

  if(regx_email.test(email)){
    document.getElementById("email").style.border="1px solid green";
    return true;
  }
  else{
    document.getElementById("email").style.border="1px solid red";
    document.getElementById("email").placeholder="Invalid Email";
    return false;
  }

}