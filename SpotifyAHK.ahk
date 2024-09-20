; Numpad9 to play/pause song
Numpad9::{
    HttpObj := ComObject("WinHttp.WinHttpRequest.5.1")
    HttpObj.Open("POST", "http://127.0.0.1:5000/playback/play", false)
    HttpObj.Send()
}
; Numpad8 to play next song
Numpad8::{
    HttpObj := ComObject("WinHttp.WinHttpRequest.5.1")
    HttpObj.Open("POST", "http://127.0.0.1:5000/playback/next", false)
    HttpObj.Send()
}
; Numpad7 to play previous song
Numpad7::{
    HttpObj := ComObject("WinHttp.WinHttpRequest.5.1")
    HttpObj.Open("POST", "http://127.0.0.1:5000/playback/previous", false)
    HttpObj.Send()
}