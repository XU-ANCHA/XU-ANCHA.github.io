(function () {
  const count = document.getElementById("vercount_value_site_pv");
  const box = document.querySelector(".site-hits");
  if (!count || !box) {
    return;
  }

  function reveal() {
    if (box.classList.contains("is-ready")) {
      return true;
    }
    const text = (count.textContent || "").replace(/,/g, "").trim();
    if (!text || text.toLowerCase() === "loading" || !/^\d+$/.test(text)) {
      return false;
    }
    const total = parseInt(text, 10);
    count.textContent = total.toLocaleString("en-US");
    box.hidden = false;
    box.classList.add("is-ready");
    return true;
  }

  if (reveal()) {
    return;
  }

  const observer = new MutationObserver(function () {
    if (reveal()) {
      observer.disconnect();
    }
  });
  observer.observe(count, { childList: true, characterData: true, subtree: true });

  let tries = 0;
  const timer = setInterval(function () {
    tries += 1;
    if (reveal() || tries > 40) {
      clearInterval(timer);
      observer.disconnect();
    }
  }, 250);
})();
