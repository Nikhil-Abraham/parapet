function validate(){

  var name = document.getElementById("name").value.trim();
  var email = document.getElementById("email").value.trim();
  var pass = document.getElementById("pass").value.trim();
  var pass2 = document.getElementById("pass2").value.trim();

  var regx_email = /^[a-zA-Z0-9.-]+@([a-zA-Z]+).([a-zA-Z]+)$/;
  var regx_name = /^[a-zA-Z]+$/;
  var flag1 = 0, flag2 = 0, flag3 = 0;
  


  if(regx_email.test(email)){
    document.getElementById("email").style.border="1px solid green";
    flag1 = 1;
  }
  else{
    document.getElementById("email").style.border="1px solid red";
    document.getElementById("email").placeholder="Invalid Email";
    flag1 = 0;
  }

  if(regx_name.test(name)){
    document.getElementById("name").style.border="1px solid green";
    flag2 = 1;
  }
  else{
    document.getElementById("name").style.border="1px solid red";
    document.getElementById("name").placeholder="Invalid Name";
    flag2 = 0;
  }

  console.log(pass.length)
  // && pass.length()>=8

  if(pass != pass2 || pass==""){
    document.getElementById("pass").style.border="1px solid red";
    document.getElementById("pass2").style.border="1px solid red";
    document.getElementById("pass").placeholder="Not Matching";
    document.getElementById("pass2").placeholder="Not Matching";
    flag3 = 0;
  }
  else{
    document.getElementById("pass").style.border="1px solid green";
    document.getElementById("pass2").style.border="1px solid green";
    flag3 = 1;
  }

  if(flag1+flag2+flag3==3){
    return true;
  }
  else{
    return false;
  }
}