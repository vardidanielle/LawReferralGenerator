const { spanNodeList } = require("./content");

document.addEventListener('DOMContentLoaded', function() {
    var ol = document.createElement("ol");
    var dict = getSpanNodeList();
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