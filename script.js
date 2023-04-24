const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://gk7g4wdbrmfz4ejltqrcmaff6m0ztqja.lambda-url.ap-southeast-1.on.aws/");
    let views = await response.json();
    counter.innerHTML = `<p style='font-size:10px;'>👀 : ${views} views</p>`;

}
updateCounter();