function getResponse(){
    alert("Get your Response via Cleopatra");
    const log=document.querySelector(".event-log-contents");
    const reload=document.querySelector("#reload");
    reload.addEventListener("click",()=>{
      log.textContent="";
      outputTextArea.value="";
      var client=new XMLHttpRequest();
      client.open("Get",'/get_response',true);
      client.onreadystatechange=() =>{
       if(client.readyState==3 && client.status==200){
          outputTextArea.value+=client.responseText;
          outputTextArea.scrollTop=outputTextArea.scrollHeight;
        }
      };
    client.send();
      setTimeout(()=>{
        window.location.reload(true);
      },200);
    });
    window.addEventListener("load",(Event)=>{
      log.textContent+="load\n";
    });
    document.addEventListener("readystatechange",(Event)=>{
      log.textContent+=`readystate :${document.readyState}\n`;
    });
    document.addEventListener("DOMContentLoaded",(Event)=>{
      log.textContent+="DOMContentLoaded\n";
    });
}
