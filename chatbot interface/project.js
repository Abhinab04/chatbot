function getResponse(){
    alert("Get your Response via Cleopatra");
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
}
