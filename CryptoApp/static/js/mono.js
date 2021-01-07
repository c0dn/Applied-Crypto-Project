function getRandomInt(n) {
  return Math.floor(Math.random() * n);
}
function shuffle(s) {
  const arr = s.split("");
  const n = arr.length;

  for(let i=0 ; i<n-1 ; ++i) {
    const j = getRandomInt(n);
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  s = arr.join("");
  return s
}

$(document).ready(function(){
  const sample_alpha = shuffle("abcdefghijklmnopqrstuvwxyz");
  $("input[name='text-setting-cipher']").val(sample_alpha);
  $(".action-encode").click(function () {
    $(".action-encode").toggleClass("mid-box-action-active");
    $(".action-decode").toggleClass("mid-box-action-active");
    $(".process-btn").text("Encrypt");
    $("#plaintext-area").val("");
    $("#ciphertext-area").val("");
    $(".box-title-right").text("Ciphertext");
    $(".box-title-left").text("Plaintext");
  });
  $(".action-decode").click(function () {
    $(".action-decode").toggleClass("mid-box-action-active");
    $(".action-encode").toggleClass("mid-box-action-active");
    $(".process-btn").text("Decrypt");
    $("#plaintext-area").val("");
    $("#ciphertext-area").val("");
    $(".box-title-right").text("Plaintext");
    $(".box-title-left").text("Ciphertext");
  });
  $(".process-btn").click(function () {
    const sub = $("input[name='text-setting-cipher']").val();
    const plain = $("input[name='text-setting-plain']").val();
    const type = $(".process-btn").text().toLowerCase();
    const text = $("#plaintext-area").val();
    let dat = {"type": type, "sub": sub, "text": text, "plain": plain};
    $.ajax({
        url: "/api/cipher/mono/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(dat),
        success: function(result) {
          $("#ciphertext-area").val(result.output);
        }
    });
  });
});