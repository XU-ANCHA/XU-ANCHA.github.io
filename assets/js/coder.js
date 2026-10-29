const body = document.body;
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

function storedTheme() {
  return localStorage.getItem("colorscheme");
}

function syncThemeChoices(theme) {
  document.querySelectorAll(".theme-choice").forEach(function (button) {
    const active = button.getAttribute("data-theme") === theme;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
  });
}

function setTheme(theme, persist) {
  const next = theme === "dark" || theme === "light" || theme === "auto" ? theme : "auto";
  body.classList.remove("colorscheme-light", "colorscheme-dark", "colorscheme-auto");

  if (next === "auto") {
    body.classList.add("colorscheme-auto");
    document.documentElement.style.colorScheme = "light dark";
  } else {
    body.classList.add("colorscheme-" + next);
    document.documentElement.style.colorScheme = next;
  }

  syncThemeChoices(next);

  if (persist) {
    localStorage.setItem("colorscheme", next);
  }

  document.dispatchEvent(new Event("themeChanged"));
}

function isMobileNav() {
  return window.matchMedia("(max-width: 768px)").matches;
}

function syncThemeMenu() {
  document.querySelectorAll(".theme-switcher details").forEach(function (details) {
    if (isMobileNav()) {
      details.open = true;
    }
  });
}

setTheme(storedTheme() || "auto", false);

document.addEventListener("click", function (event) {
  const button = event.target.closest(".theme-choice");
  if (button) {
    event.preventDefault();
    setTheme(button.getAttribute("data-theme"), true);
    const details = button.closest("details");
    if (details && !isMobileNav()) {
      details.open = false;
    }
    return;
  }
  if (!isMobileNav() && !event.target.closest(".theme-switcher")) {
    document.querySelectorAll(".theme-switcher details").forEach(function (details) {
      details.open = false;
    });
  }
});

if (typeof darkModeMediaQuery.addEventListener === "function") {
  darkModeMediaQuery.addEventListener("change", function () {
    if ((storedTheme() || "auto") === "auto") {
      setTheme("auto", false);
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const node = document.querySelector(".preload-transitions");
  if (node) {
    node.classList.remove("preload-transitions");
  }
  syncThemeChoices(storedTheme() || "auto");
  syncThemeMenu();
});

window.addEventListener("resize", syncThemeMenu);
