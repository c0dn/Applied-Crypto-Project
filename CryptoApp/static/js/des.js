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
    const bytes_size = 64 / 8;
    const selected_mode = $("select[name='mode-setting']").children("option:selected").val();
    const type = $(".process-btn").text().toLowerCase();
    const text = $("#plaintext-area").val();
    const key = $("input[name='text-setting-key']").val();
    if (key.length !== bytes_size) {
      window.alert("Invalid key length. It must be "+ bytes_size + " bytes");
    } else {
     let dat = {"type": type, "key": key, "text": text, "mode": selected_mode};
      $.ajax({
          url: "/api/crypto/des/",
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