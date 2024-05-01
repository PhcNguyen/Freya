document.addEventListener('DOMContentLoaded', function () {
    var logo = document.querySelector('.logo-base a');
    
    logo.addEventListener('click', function (event) {
      // Kiểm tra nếu URL hiện tại là trang chủ
      if (window.location.pathname === '/') {
        event.preventDefault(); // Ngăn chặn hành vi mặc định của thẻ <a>
      }
    });
  });