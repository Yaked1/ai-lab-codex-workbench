(function () {
  "use strict";
  const input = document.getElementById("site-search");
  const results = document.getElementById("search-results");
  if (!input || !results) return;
  const items = Array.isArray(window.WORKBENCH_SEARCH_INDEX) ? window.WORKBENCH_SEARCH_INDEX : [];

  function render(query) {
    const normalized = query.trim().toLowerCase();
    results.replaceChildren();
    if (!normalized) {
      results.setAttribute("hidden", "");
      return;
    }
    const matches = items.filter((item) =>
      `${item.title} ${item.description}`.toLowerCase().includes(normalized)
    ).slice(0, 8);
    for (const item of matches) {
      const li = document.createElement("li");
      const link = document.createElement("a");
      link.href = item.url;
      link.textContent = item.title;
      const detail = document.createElement("span");
      detail.textContent = item.description;
      li.append(link, detail);
      results.append(li);
    }
    if (!matches.length) {
      const li = document.createElement("li");
      li.textContent = "No local guide matched that search.";
      results.append(li);
    }
    results.removeAttribute("hidden");
  }

  input.addEventListener("input", () => render(input.value));
})();
