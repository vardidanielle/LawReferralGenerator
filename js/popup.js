
document.addEventListener('DOMContentLoaded', function() {
    var ol = document.createElement("ol");
    var dict = spanNodeList;
    for (var key in dict) {
        var law = document.createElement('li');
        law.textContent = key;
        law.onclick = function() {
            dict[key].scrollIntoView();
        }
        ol.appendChild(law);
    }
    document.body.appendChild(ol)
}, false);


// console.log("here");

// chrome.tabs.query({
//     'active': true,
//     'currentWindow': true
// },
// function(tabs) {
//     if ('undefined' != typeof tabs[0].id && tabs[0].id) {
//     chrome.tabs.sendMessage(tabs[0].id, {
//         'message' : 'loadY',
//         'document': document
//     });
//     }
// });