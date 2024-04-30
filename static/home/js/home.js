document.addEventListener('keydown', function(event) {
  if (event.ctrlKey || event.metaKey) {
    switch (event.key) {
      case 'c': // Ctrl+C hoặc Command+C
      case 'x': // Ctrl+X hoặc Command+X
      case 'v': // Ctrl+V hoặc Command+V
        event.preventDefault();
        break;
    }
  }
});

// Ngăn chặn sự kiện chuột phải trên toàn bộ trang
document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
}, false);

document.querySelectorAll('.social-links a[href*="instagram.com"]').forEach(function(link) {
  link.addEventListener('mouseover', function(e) {
    e.preventDefault();
  });
});

// JavaScript để xử lý sự kiện click cho menu toggle
document.addEventListener('DOMContentLoaded', function () {
  var menuToggle = document.getElementById('menu-toggle');
  var menu = document.querySelector('.nav-menu');

  menuToggle.addEventListener('click', function () {
      menu.classList.toggle('active');
  });
});







