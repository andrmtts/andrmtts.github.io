(function () {
  "use strict";

  document.getElementById("year").textContent = new Date().getFullYear();

  /* ---------- Mobile nav toggle ---------- */
  var navToggle = document.getElementById("navToggle");
  var mainNav = document.getElementById("mainNav");

  navToggle.addEventListener("click", function () {
    var isOpen = mainNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  mainNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      mainNav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- Scroll-spy active nav link ---------- */
  var navLinks = document.querySelectorAll("a[data-nav]");
  var sections = Array.prototype.map.call(navLinks, function (link) {
    return document.querySelector(link.getAttribute("href"));
  }).filter(Boolean);

  function updateActiveNav() {
    var scrollPos = window.scrollY + 120;
    var current = null;
    sections.forEach(function (section) {
      if (section.offsetTop <= scrollPos) current = section;
    });
    navLinks.forEach(function (link) {
      link.classList.toggle("active", !!current && link.getAttribute("href") === "#" + current.id);
    });
  }
  window.addEventListener("scroll", updateActiveNav, { passive: true });
  updateActiveNav();
})();
