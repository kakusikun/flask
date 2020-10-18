function connectCamera(ip, port, index, dummyImgSrc){
    $('.main').prepend(
        `<div class="col-6">
            <div class="row no-gutters">
                <div class="col text-center border">
                    <div class="video-container">
                        <img id="stream${index}" src=${dummyImgSrc} class="img-fluid img-responsive video" data-switch="open">
                        <svg id="wait${index}" viewBox="0 0 16 16" class="bi bi-play-fill wait" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path d="M11.596 8.697l-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
                            </svg>
                    </div>
                </div>
            </div>
        </div>`
    );
    var url = `http://${ip}:${port}/stream`;
    var socket = io.connect(url);
    var stream;
    var streamId = `#stream${index}`;
    var waitId = `#wait${index}`;
    
    socket.on('response', function(msg){
        console.log(msg.data);
    });
    
    socket.on('stream', function(msg){
        $(streamId).attr("src", msg.data);
    });
    
    $(streamId).click(function(){
        clearInterval(stream);
        $(waitId).slideDown();
    });

    $(waitId).click(function(){
        stream = setInterval(function(){ 
            socket.emit('stream', {data: 'stream'});
        }, 40);
        $(this).slideUp();
    });

    return socket;

}

export { connectCamera };