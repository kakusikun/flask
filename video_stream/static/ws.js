function websocket(ip, port){
    var url = `http://${ip}:${port}/stream`;
    var socket = io.connect(url);
    var stream;
    
    socket.on('response', function(msg){
        console.log(msg.data);
    });
    
    socket.on('stream', function(msg){
        $("#stream").attr("src", msg.data);
    });
    
    $("#play").click(function(){
        stream = setInterval(function(){ 
            socket.emit('stream', {data: 'stream'});
        }, 40);
    });
    
    $("#stop").click(function(){
        clearInterval(stream)
    });

    return socket;

}

export {websocket};