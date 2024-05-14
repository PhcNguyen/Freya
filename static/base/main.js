document.addEventListener('keydown', function(event) {
  if (event.ctrlKey || event.metaKey) {
      switch (event.key) {
      case 'c':
      case 'x': 
      case 'v': 
          event.preventDefault();
          break;
      }
  }
});


// Ngăn chặn sự kiện chuột phải trên toàn bộ trang
document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
}, false);
var lastScrollTop = 0;
navbar = document.getElementById("navbar");
window.addEventListener("scroll", function () {
var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

if (scrollTop > lastScrollTop) {
  navbar.style.top = "-100px";
} else {
  navbar.style.top = "0";
  if (scrollTop === 0) {
      navbar.classList.remove("scrolled"); 
  } else {
      navbar.classList.add("scrolled"); 
      }
  }
lastScrollTop = scrollTop;
}
);

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
      var panel = this.nextElementSibling;
      var isActive = this.classList.contains("active");

      // Close all accordion panels

      for (var j = 0; j < acc.length; j++) {
          var otherPanel = acc[j].nextElementSibling;
          if (otherPanel !== panel) {
              otherPanel.style.maxHeight = null;
              acc[j].classList.remove("active");
          }
      }

      if (isActive) {
          this.classList.remove("active");
          panel.style.maxHeight = null;
      } else {
          this.classList.add("active");
          panel.style.maxHeight = panel.scrollHeight + "px";
          }
      }
  );
}