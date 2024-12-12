// Home_page.js


const banners = [
    "/static/images/Navratri_Banner.jpg",
    "/static/images/355167888_753795866749007_8134489539911786255_n.jpg",
    "/static/images/Ganesh_Chaturti_Banner.jpg",
    "/static/images/VC_Banner12.jpg"
];

const imagePath = "static/images/";

const bannerContainer = document.getElementById("banner-container");

let currentIndex = 0;

function showBanner(index) {
    const banner = document.getElementById('banner');
    banner.src = banners[index];
}

function nextBanner() {
    currentIndex = (currentIndex + 1) % banners.length;
    showBanner(currentIndex);
}

function prevBanner() {
    currentIndex = (currentIndex - 1 + banners.length) % banners.length;
    showBanner(currentIndex);
}

// Automatic banner swap every 5 seconds
setInterval(nextBanner, 5000);

// Initial banner display
showBanner(currentIndex);


let currentIndex2 = 0;
const totalImages = document.querySelectorAll('.image-frame img').length;
const imagePerFrame = 4;
const frame = document.querySelector('.image-frame');
const totalFrames = Math.ceil(totalImages / imagePerFrame);

function updateFramePosition(){
    frame.style.transform = `translateX(${-currentIndex2 * 100}%)`;
}

function nextImage(){
    currentIndex2 = (currentIndex2 + 1) % totalFrames;
    updateFramePosition();
}

function prevImage(){
    currentIndex2 = (currentIndex2 - 1 + totalFrames) % totalFrames;
    updateFramePosition();
}

let autoSwap = setInterval(nextImage, 5000);

document.querySelector('.prev').addEventListener('click', function(){
    clearInterval(autoSwap);
    autoSwap = setInterval(nextImage, 5000);
});
document.querySelector('next').addEventListener('click', function(){
    clearInterval(autoSwap);
    autoSwap = setInterval(nextImage, 5000);
});
class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();