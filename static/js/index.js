const closeIcon = document.querySelector('.cancel-message');
const searchBtn = document.querySelector('.search-btn');
const message = document.querySelectorAll('.message');
const allTasks = document.querySelectorAll('.task');
document.body.addEventListener('click',closeFlashMessage);
// document.body.addEventListener('click', searchTask);
setTimeout(()=>{
  if (message){
  message.forEach(msg =>{
    msg.style.display = "none";
  })
}
},2000);

function closeFlashMessage(e){
   let x = e.target;

  if (x.classList.contains('cancel-message')){
    x.parentElement.style.display = "none";
  }
  
}



// function searchTask(e){
  
//   if(e.target == searchBtn){
    
//     allTasks.forEach((task)=>{
//       console.log(task.firstChild);
//     });
    
//   }
  
// }