btn=document.getElementById('submit-btn');
btn.addEventListener("click",function(e){
    e.preventDefault()
    cno=parseInt(document.getElementById('cno').value);
    cname=document.getElementById('cname').value;
    runs=parseInt(document.getElementById('runs').value);
    newcricketer={cno,cname,runs}
    console.log(newcricketer);
    fetch("http://127.0.0.1:5000/save_my_cricketer",{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(newcricketer)
    })
    .then(response=>{
        const status=response.status;
        return response.json().then(data=>{
            alert(`Status: ${status}\nMessage: ${data.message}`);
            // myp1=document.createElement('p')
            // myp1.innerHTML=`Status: ${status}\nMessage: ${data.message}`
            // myform[0].insertBefore(myp1, empbtn);
        })
    })
})