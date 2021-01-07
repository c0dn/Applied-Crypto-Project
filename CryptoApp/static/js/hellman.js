$(document).ready(function(){
  $(".process-btn").click(function () {
    const n = $("input[name='number-n-setting']").val();
    const g = $("input[name='number-g-setting']").val();
    let dat = {"n": n, "g": g};
    $.ajax({
        url: "/api/cipher/hellman/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(dat),
        success: function(result) {
          $("#ciphertext-area").val(result.output.join("\n"));
          console.log(result.output);
        }
    });
  });
});