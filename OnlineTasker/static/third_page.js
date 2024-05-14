let source = document.getElementById("source").value; // папка с картинками
let index = Number(document.getElementById("index").value); // индекс изначальной картинки
let popupImg = document.querySelector('.currentImage');
console.log(index)
console.log(source)


function hasNextImage(callback) {
    let img = new Image();
        img.onload = () => callback(true);
        img.onerror = () => callback(false);
        img.src = source + 'out' + (index + 1) + '.png';
}

document.querySelector('.prev').addEventListener('click', () => {
    if (index > 0) {
        index--;
        popupImg.src = source + 'out' + index + '.png';
        updateButtons();
    }
});
 document.querySelector('.next').addEventListener('click', () => {
     hasNextImage((exists) => {
         if (exists) {
             index++;
             popupImg.src = source + 'out' + index + '.png';
             updateButtons();
         }
     });
 });

 function updateButtons() {
     document.querySelector('.prev').style.display = index === 0 ? 'none' : '';
        hasNextImage((exists) => {
            document.querySelector('.next').style.display = exists ? '' : 'none';
        });
    }

updateButtons();