const closeIcon = document.querySelector('.cancel-message');
const searchBtn = document.querySelector('.search-btn');
const allTasks = document.querySelectorAll('.task');
document.body.addEventListener('click',closeFlashMessage);
document.body.addEventListener('click', searchTask);


function closeFlashMessage(e){
   let x = e.target;

  if (x.classList.contains('cancel-message')){
    x.parentElement.style.display = "none";
  }
}



function searchTask(e){
  
  if(e.target == searchBtn){
    
    allTasks.forEach((task)=>{
      console.log(task.firstChild);
    });
    
  }
  
}