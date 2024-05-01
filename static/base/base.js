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


document.addEventListener('DOMContentLoaded', function () {
  var menuToggle = document.getElementById('menu-toggle');
  var menu = document.querySelector('.nav-menu');

  menuToggle.addEventListener('click', function () {
      menu.classList.toggle('active');
  });

  document.addEventListener('click', function(event) {
      if (!menu.contains(event.target) && !menuToggle.contains(event.target)) {
          menu.classList.remove('active');
          menuToggle.checked = false;
      }
  });

  window.addEventListener('scroll', function() {
      if (menu.classList.contains('active')) {
          menu.classList.remove('active');
          menuToggle.checked = false;
      }
  });
});