const closeIcon = document.querySelector('.cancel-message');

document.body.addEventListener('click',closeFlashMessage);


function closeFlashMessage(e){
   let x = e.target;

  if (x === closeIcon) x.parentElement.style.display = "none";
  
}