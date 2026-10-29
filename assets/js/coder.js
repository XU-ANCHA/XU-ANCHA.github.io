const body = document.body;
const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
const palettes = ["warm-stone", "sage", "slate", "zinc", "ink"];
const themes = ["light", "dark", "auto"].concat(palettes);
const defaultTheme = "warm-stone";

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

function clearThemeClasses() {
  body.classList.remove("colorscheme-light", "colorscheme-dark", "colorscheme-auto", "palette-mist");
  palettes.forEach(function (name) {
    body.classList.remove("palette-" + name);
  });
}

function setTheme(theme, persist) {
  const next = themes.indexOf(theme) >= 0 ? theme : defaultTheme;
  clearThemeClasses();

  if (next === "auto") {
    body.classList.add("colorscheme-auto");
    document.documentElement.style.colorScheme = "light dark";
  } else if (next === "dark") {
    body.classList.add("colorscheme-dark");
    document.documentElement.style.colorScheme = "dark";
  } else if (next === "light") {
    body.classList.add("colorscheme-light", "palette-mist");
    document.documentElement.style.colorScheme = "light";
  } else {
    body.classList.add("colorscheme-light", "palette-" + next);
    document.documentElement.style.colorScheme = "light";
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

setTheme(storedTheme() || defaultTheme, false);

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
    if (storedTheme() === "auto") {
      setTheme("auto", false);
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const node = document.querySelector(".preload-transitions");
  if (node) {
    node.classList.remove("preload-transitions");
  }
  syncThemeChoices(storedTheme() || defaultTheme);
  syncThemeMenu();
});

window.addEventListener("resize", syncThemeMenu);
