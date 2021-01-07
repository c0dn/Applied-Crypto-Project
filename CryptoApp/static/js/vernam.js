$(document).ready(function(){
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
    const key = $("input[name='text-setting-key']").val();
    const type = $(".process-btn").text().toLowerCase();
    const text = $("#plaintext-area").val();
    if (key.length !== text.length) {
      window.alert("Key is not same length as plaintext/ciphertext");
    } else {
      let dat = {"type": type, "key": key, "text": text};
      $.ajax({
          url: "/api/cipher/vernam/",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify(dat),
          success: function(result) {
            $("#ciphertext-area").val(result.output);
          }
      });
    }
  });
});