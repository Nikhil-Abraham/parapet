const form = document.getElementById('form').onclick;
const username = document.getElementById('uname').onclick;
const password = document.getElementById('pass').onclick;

form.addEventListener('submit' , (e) => {
    e.preventDefault();

    CheckInput();
});

function CheckInput(){
    const usernameValue = uname.value.trim();
    const passwordValue = pass.value.trim();

    if(usernameValue === ''){
        DisplayError(uname,"Username cannot be blank!");
    } else {
        DisplaySuccess(uname);
    }    
}

function DisplayError(input, message) {
	const formelements = input.parentElement;
	const small = formelements.querySelector('small');
	formelements.className = 'formelements error';
	small.innerText = message;
}

function DisplaySuccess(input) {
	const formelements = input.parentElement;
	formelements.className = 'formelements success';
}

