(function () {
  function wrapArticle(article) {
    if (article.dataset.modulesReady) {
      return;
    }

    const elements = Array.from(article.children).filter(function (el) {
      return el.tagName !== "HEADER";
    });
    if (!elements.length) {
      return;
    }

    const groups = [];
    let current = [];
    elements.forEach(function (el) {
      if (el.tagName === "H2" && current.length) {
        groups.push(current);
        current = [el];
      } else {
        current.push(el);
      }
    });
    if (current.length) {
      groups.push(current);
    }

    groups.forEach(function (group) {
      const wrap = document.createElement("section");
      wrap.className = group[0].tagName === "H2" ? "module" : "module module-lead";
      group[0].parentNode.insertBefore(wrap, group[0]);
      group.forEach(function (el) {
        wrap.appendChild(el);
      });
    });

    article.dataset.modulesReady = "true";
  }

  function init() {
    document.querySelectorAll(".page article").forEach(wrapArticle);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
