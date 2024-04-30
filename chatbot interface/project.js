document.addEventListener("DOMContentLoaded",()=>{
   const reload=document.getElementById("reload");
   reload.addEventListener('click',function(){
    fetch('/getResponse',{
        method:'POST',
        headers:{
            "Content-type":'application/x-www-form-urlencoded'
        },
        body:'input'
    })
    .then(Response=>Response.json)
    .then(data =>{
        const responseid=document.getElementById('Response');
        responseid.value=data.Response;
    })
    .catch(error =>{
        console.error("error",error);
    });
   });
});
