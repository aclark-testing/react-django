var url = 'http://localhost:8000/comments/?format=json'
var x = new XMLHttpRequest()
x.open("GET", url, true)
x.onreadystatechange = function(){
  if (x.readyState == 4 && x.status == 200){
    console.log(x.response)
  }
}

x.setRequestHeader('Content-Type', 'application/json');
x.send()

/*
Exception: [Exception... "<no message>"  nsresult: "0x805e0006 (<unknown>)"  location: "JS frame :: Scratchpad/4 :: <TOP_LEVEL> :: line 11"  data: no]
*/