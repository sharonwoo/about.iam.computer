const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://vryowpy57u7p7j7of27pp4penm0jvipw.lambda-url.ap-southeast-1.on.aws/");
    let views = await response.json();
    counter.innerHTML = `<p style='font-size:10px;'>👀 : ${views} views</p>`;

}
updateCounter();