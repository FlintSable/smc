function openimage(imgs) {

  // Get the expanded image
  var dubImg = document.getElementById('double');
  var x = imgs.parentElement.href;
  var imgText = document.getElementById('imgText');
  console.log(imgText)
  console.log(imgs.alt)
  imgText.innerHTML = imgs.alt;
  dubImg.src = imgs.src;
  dubImg.parentElement.href = x
  dubImg.parentElement.style.display = "block";
}