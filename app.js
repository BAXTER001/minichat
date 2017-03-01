

var postCycle = function(){
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           console.log(req.responseText);
        }
    };
    req.open("GET", "/messages", true);
    req.send();
    setTimeout(postCycle,500);
}
postCycle();

