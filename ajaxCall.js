var url = 
    'http://localhost:8000/api/v1/sections/path/part-summaries/list.json/?inline_all=True'
var x = new XMLHttpRequest()
x.open("GET", url, true)
x.onreadystatechange = function(){
  if (x.readyState == 4 && x.status == 200){
    console.log(x.response)
  }
}

x.setRequestHeader('Content-Type', 'application/json');
x.send()
