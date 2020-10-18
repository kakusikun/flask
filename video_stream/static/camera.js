import { connectCamera } from "./ws.js"

$(document).ready(function () {
    connectCamera(ip, port, 1, dummyImgSrc);
    connectCamera(ip, port, 2, dummyImgSrc);
    
});