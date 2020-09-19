import { add } from "./math.js"
// window.onload = function() {
//     // console.log("window loaded")
// };

var btn = document.getElementById("btn");
btn.addEventListener("click", Add);

function Add(){
    var result = document.getElementById("result");
    var a = document.getElementById("a");
    var b = document.getElementById("b");
    console.log(a.value);
    console.log(b.value);
    // c = a.value + b.value
    result.innerHTML = add(a.value, b.value);
}
