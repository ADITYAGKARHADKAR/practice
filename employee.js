empbtn=document.getElementById("submit-emp")
myform = document.getElementsByClassName('frm')
srcbtn=document.getElementById("search-btn")



empbtn.addEventListener("click",function(e){
    e.preventDefault();
    empno=document.getElementById("empno").value;
    ename=document.getElementById("ename").value;
    salary=document.getElementById("sal").value;
    empno=parseInt(empno);
    salary=parseFloat(salary);
    newemployee={empno,ename,salary}
    console.log(`empno=${empno},ename=${ename},salary=${salary}`)
    fetch("http://127.0.0.1:5000/save_my_employee",{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(newemployee)
    })
    .then(response => {
  // Store the status code
  const status = response.status;
  // Parse JSON body
  return response.json().then(data => {
    alert(`Status: ${status}\nMessage: ${data.message}`);
    myp1=document.createElement('p')
    myp1.innerHTML=`Status: ${status}\nMessage: ${data.message}`
    myform[0].insertBefore(myp1, empbtn);
    
  });
})
    .catch(err=> alert('Error:'+ err));

})


srcbtn.addEventListener("click",function(e){
  e.preventDefault();
  empno=document.getElementById("empno").value
  fetch(`http://localhost:5000/search_employee?empno=${empno}`,{
    method:'GET',
    headers:{
      'Content-Type': 'application/json'
    }

  })
  .then(response=>{
    const statusCode = response.status;
    return response.json().then(data=>{
                empno.value=data.empno;
                empname.value=data.empname;
                salary.value=data.salary;
                 alert(`Status ${statusCode}: Employee found successfully!`);
    })
  })
  .catch(error => {
  alert("Network or server error: " + error.message);
});
})
